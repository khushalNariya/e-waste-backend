from app_8_Reward_Rules.models import Reward_Rule_model
from app_11_User_Rewards.User_Rewards__API__1.models import (
    Reward_Transaction_Model,
    User_Wallet_Model,
)
from django.db import transaction

@transaction.atomic
def process_reward(submission, old_instance=None):
    """
    🔥 Handles:
    1. First time reward
    2. Recalculate reward (if already rewarded)
    """

    # =====================================================
    # ❗ MUST: Only rewarded status
    # =====================================================
    if submission.status != "rewarded":
        print("⛔ Reward skipped: status not rewarded")
        return

    user = submission.user
    category = submission.category
    final_condition = submission.final_condition
    weight = submission.weight

    # =====================================================
    # ❌ VALIDATION
    # =====================================================
    if not final_condition:
        print("❌ Reward skipped: final_condition missing")
        return

    # ❌ ❌ OLD CODE (REMOVE KAR DIYA)
    # if weight is None:
    #     print("❌ Reward skipped: weight missing")
    #     return

    # =====================================================
    # 🔹 FIND RULE
    # =====================================================
    rule = Reward_Rule_model.objects.filter(
        category=category,
        condition=final_condition,
        is_active=True
    ).first()

    if not rule:
        print("❌ Reward skipped: rule not found")
        return

    # =====================================================
    # 🔥 ✅ NEW CHANGE (IMPORTANT)
    # =====================================================
    if rule.unit.lower() == "kg":
        if weight is None:
            print("❌ Reward skipped: weight required for kg based reward")
            return
        weight = int(weight)
    else:
        weight = 0  # 👉 item case me ignore

    # =====================================================
    # 🔥 REMOVE OLD TRANSACTIONS
    # =====================================================
    old_transactions = Reward_Transaction_Model.objects.filter(submission=submission)

    wallet, created = User_Wallet_Model.objects.get_or_create(
        user=user, defaults={"total_points": 0}
    )

    # 👉 subtract old points
    for txn in old_transactions:
        wallet.total_points -= txn.points

    # ❗ safety
    if wallet.total_points < 0:
        wallet.total_points = 0

    wallet.save()

    # 👉 delete old transactions
    old_transactions.delete()

    # =====================================================
    # 🔹 CALCULATION
    # =====================================================
    if rule.unit.lower() == "kg":
        base_points = rule.points * weight
    else:
        base_points = rule.points

    total_points = base_points

    # =====================================================
    # 🔹 BONUS
    # =====================================================
    bonus = 0
    extra_kg = 0
    blocks = 0

    if rule.unit.lower() == "kg" and weight > 50:
        extra_kg = weight - 50
        blocks = extra_kg // 10
        bonus = blocks * 50

    total_points += bonus

    # =====================================================
    # 🔥 ✅ DESCRIPTION FIX (NEW CHANGE)
    # =====================================================
    if rule.unit.lower() == "kg":
        if bonus > 0:
            description = (
                f"Base: {rule.points} × {weight}kg = {base_points} | "
                f"Bonus: {extra_kg}kg extra → {blocks}×50 = {bonus} | "
                f"Total = {total_points}"
            )
        else:
            description = f"Base: {rule.points} × {weight}kg = {total_points}"
    else:
        description = f"Base: {rule.points} (per item)"

    # =====================================================
    # 🔹 CREATE TRANSACTION
    # =====================================================
    Reward_Transaction_Model.objects.create(
        user=user,
        submission=submission,
        points=total_points,
        type="credit",
        description=description
    )

    # =====================================================
    # 🔹 UPDATE WALLET
    # =====================================================
    wallet.total_points += total_points
    wallet.save()

    print(f"✅ Reward Processed: {total_points} points added")
