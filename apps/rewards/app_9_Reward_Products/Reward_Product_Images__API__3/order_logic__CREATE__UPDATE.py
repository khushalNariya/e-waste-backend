from django.db import models, transaction
from django.conf import settings
import os
import shutil
from .models import Reward_Product_Image_model

# ===========================================================================
# ================== CREATE ORDER LOGIC =====================================
# ===========================================================================

@transaction.atomic
def handle_create_order(product, display_order):
    """
    👉 CREATE logic: 
    1. Agar order diya hai -> Check unique, else Error.
    2. Agar order nahi diya -> Auto-increment.
    """
    from rest_framework import serializers

    # CASE 1: No order given → auto assign next
    if display_order is None:
        last = (
            Reward_Product_Image_model.objects.filter(product=product)
            .order_by("-display_order")
            .first()
        )
        return (last.display_order + 1) if last else 1

    # CASE 2: Order given → Check uniqueness
    if Reward_Product_Image_model.objects.filter(
        product=product, display_order=display_order
    ).exists():
        raise serializers.ValidationError(
            {"display_order": f"Order number {display_order} is already taken for this product."}
        )

    return display_order


# ===========================================================================
# ================== UPDATE ORDER LOGIC =====================================
# ===========================================================================

@transaction.atomic
def handle_update_order(instance, new_order):
    """
    👉 Handles drag & drop reorder system
    👉 Use atomic to prevent data inconsistency
    """

    if not new_order or new_order == instance.display_order:
        return instance.display_order

    product = instance.product
    old_order = instance.display_order

    # 1️⃣ Temporarily set current record to None (to avoid Unique collision while shifting others)
    Reward_Product_Image_model.objects.filter(id=instance.id).update(display_order=None)

    # 2️⃣ Shift other records
    if new_order > old_order:
        # MOVE DOWN: Shift intermediate items UP (-1)
        Reward_Product_Image_model.objects.filter(
            product=product, display_order__gt=old_order, display_order__lte=new_order
        ).update(display_order=models.F("display_order") - 1)

    else:
        # MOVE UP: Shift intermediate items DOWN (+1)
        Reward_Product_Image_model.objects.filter(
            product=product, display_order__gte=new_order, display_order__lt=old_order
        ).update(display_order=models.F("display_order") + 1)

    # 3️⃣ Return new_order (Serializer will save it to instance.display_order)
    return new_order


# ===========================================================================
# ================== UPDATE (PRODUCT CHANGE) ORDER LOGIC =====================
# ===========================================================================

@transaction.atomic
def handle_product_change_order(instance, new_product, new_order):
    """
    👉 ONLY for UPDATE when product changes
    """
    from django.db.models import F

    if new_order is None:
        last = (
            Reward_Product_Image_model.objects.filter(product=new_product)
            .order_by("-display_order")
            .first()
        )
        return (last.display_order + 1) if last else 1

    # 👉 SHIFT existing records in NEW product
    Reward_Product_Image_model.objects.filter(
        product=new_product,
        display_order__gte=new_order
    ).update(display_order=F("display_order") + 1)

    return new_order


def move_image(instance, new_product):
    """
    👉 Physically move old file to new product folder.
    """
    from .models import product_image_upload_path

    if not instance.image or not hasattr(instance.image, 'path'):
        return

    old_path = instance.image.path
    if not os.path.exists(old_path):
        return

    filename = os.path.basename(instance.image.name)

    # Calculate NEW relative path (Using temporary product switch)
    old_product = instance.product
    instance.product = new_product
    new_rel_path = product_image_upload_path(instance, filename)
    new_abs_path = os.path.join(settings.MEDIA_ROOT, new_rel_path)
    instance.product = old_product # restore

    # Physical Move
    os.makedirs(os.path.dirname(new_abs_path), exist_ok=True)
    
    try:
        shutil.move(old_path, new_abs_path)
        # Update DB path reference
        instance.image.name = new_rel_path
    except Exception as e:
        print(f"File Move Error: {e}")