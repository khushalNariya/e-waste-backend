# from django.db import transaction
# from app_8_Reward_Rules.models import Reward_Rule_model
# from app_10_E_Waste_Submission.E_Waste_Submission__API__1.models import (
#     E_Waste_Submission_Model,
# )
# from django.db import connection


# # =========================================================
# # 🔥 CALCULATE POINTS FUNCTION
# # =========================================================
# def calculate_points(submission):
#     """
#     👉 This function calculates reward points
#     based on category + condition + unit
#     """

#     # Get rule using category + final_condition
#     try:
#         rule = Reward_Rule_model.objects.get(
#             category=submission.category,
#             condition=submission.final_condition,
#             is_active=True,
#         )
#     except Reward_Rule_model.DoesNotExist:
#         raise Exception("No reward rule found")

#     # CASE 1: unit = item
#     if rule.unit == "item":
#         return rule.points

#     # CASE 2: unit = kg
#     elif rule.unit == "kg":
#         if not submission.weight:
#             raise Exception("Weight is required for kg based reward")

#         return submission.weight * rule.points

#     return 0


# # =========================================================
# # 🔥 CREATE TRANSACTION
# # =========================================================
# def create_reward_transaction(user_id, submission_id, points):
#     """
#     👉 Insert record into reward_transactions table
#     """

#     with connection.cursor() as cursor:
#         cursor.execute(
#             """
#             INSERT INTO reward_transactions
#             (user_id, submission_id, points, type, description)
#             VALUES (%s, %s, %s, 'credit', 'Recycling Reward')
#         """,
#             [user_id, submission_id, points],
#         )


# # =========================================================
# # 🔥 UPDATE WALLET
# # =========================================================
# def update_wallet(user_id, points):
#     # from django.db import connection

#     with connection.cursor() as cursor:

#         # 🔍 Check wallet exist
#         cursor.execute("SELECT id FROM user_wallet WHERE user_id = %s", [user_id])
#         result = cursor.fetchone()

#         if result:
#             # ✅ Update existing
#             cursor.execute(
#                 """
#                 UPDATE user_wallet
#                 SET total_points = total_points + %s
#                 WHERE user_id = %s
#             """,
#                 [points, user_id],
#             )
#         else:
#             # ✅ Create new wallet
#             cursor.execute(
#                 """
#                 INSERT INTO user_wallet (user_id, total_points)
#                 VALUES (%s, %s)
#             """,
#                 [user_id, points],
#             )


# # =========================================================
# # 🔥 MAIN FUNCTION (ALL IN ONE)
# # =========================================================
# @transaction.atomic
# def process_reward(submission):
#     """
#     👉 This function handles full reward process
#     """

#     # ❌ Check already rewarded
#     if submission.status == "rewarded":
#         return

#     # ❌ Final condition required
#     if not submission.final_condition:
#         raise Exception("Final condition required")

#     # 🔥 Step 1: Calculate points
#     points = calculate_points(submission)

#     # 🔥 Step 2: Create transaction
#     create_reward_transaction(submission.user_id, submission.id, points)

#     # 🔥 Step 3: Update wallet
#     update_wallet(submission.user_id, points)

#     # 🔥 Step 4: Update status → rewarded
#     submission.status = "rewarded"
#     submission.save()

#     return points


# reward_logic.py

from app_8_Reward_Rules.models import Reward_Rule_model
from app_11_User_Rewards.User_Rewards__API__1.models import (
    Reward_Transaction_Model,
    User_Wallet_Model,
)


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

    # if weight is None:
    #     print("❌ Reward skipped: weight missing")
    #     return

    # =====================================================
    # 🔥 REMOVE OLD TRANSACTIONS (SAFE VERSION)
    # =====================================================
    old_transactions = Reward_Transaction_Model.objects.filter(submission=submission)

    wallet, created = User_Wallet_Model.objects.get_or_create(
        user=user, defaults={"total_points": 0}
    )

    # 👉 subtract all old points
    for txn in old_transactions:
        wallet.total_points -= txn.points

     # ❗ safety
    if wallet.total_points < 0:
        wallet.total_points = 0


    wallet.save()
    # 👉 delete all old transactions
    old_transactions.delete()

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

    print("===== DEBUG START =====")
    print("Rule Unit:", rule.unit)
    print("Rule Unit Type:", type(rule.unit))
    print("Weight:", weight)
    print("Final Condition:", final_condition)
    print("Category:", category)
    print("===== DEBUG END =====")

    # =====================================================
    # 🔹 CALCULATION
    # =====================================================
    weight = int(weight)

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
    # 🔹 DESCRIPTION BUILD
    # =====================================================
    if bonus > 0:
        description = (
            f"Base: {rule.points} × {weight}kg = {base_points} | "
            f"Bonus: {extra_kg}kg extra → {blocks}×50 = {bonus} | "
            f"Total = {total_points}"
        )
    else:
        description = f"Base: {rule.points} × {weight}kg = {total_points}"
    
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
