import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_waste_recycling.settings')
django.setup()

from django.db import connection


# ================================================================
# TABLE 1: reward_order_replace_requests
# PURPOSE : Main table for Replace Requests (like Amazon/Flipkart).
#           User yahan se replace request submit karta hai.
#           Ek order ke liye ek replace request allowed hai.
#           'replace_status' field poora replace flow track karta hai.
# ================================================================
query_replace_requests = """
CREATE TABLE IF NOT EXISTS reward_order_replace_requests (

    id INT AUTO_INCREMENT PRIMARY KEY
    COMMENT 'Unique ID for each replace request (auto-generated)',

    replace_number VARCHAR(50) NOT NULL UNIQUE
    COMMENT 'Human-readable unique replace ID. Example: REP-2025-001. Admin aur user dono is number se track karte hain.',

    order_id INT NOT NULL
    COMMENT 'Links replace request to original order. FK to reward_orders.id. Sirf delivered orders pe replace allowed hai.',

    user_id INT NOT NULL
    COMMENT 'Links replace request to the user who submitted it. FK to auth_user.id.',

    replace_status VARCHAR(30) NOT NULL DEFAULT 'requested'
    COMMENT 'Current status of this replace request. Flow: requested → approved → replacement_dispatched → replacement_delivered → quality_checked → closed. Exit state: rejected.',

    replace_reason VARCHAR(255) NOT NULL
    COMMENT 'Primary reason for replacement. Example: wrong_item_delivered, defective, damaged_packaging, wrong_color.',

    replace_note TEXT NULL
    COMMENT 'Optional extra note from user explaining the issue. Example: I ordered blue color but received red.',

    replace_type VARCHAR(30) NOT NULL DEFAULT 'same_item'
    COMMENT 'Type of replacement requested. Values: same_item (exact same product), different_variant (different size/color of same product).',

    replace_date DATETIME NULL
    COMMENT 'Scheduled date-time for replacement delivery + old item pickup. Admin sets this after approving. Both happen in one trip (Amazon style).',

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    COMMENT 'Timestamp when replace request was first submitted by user.',

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    COMMENT 'Timestamp of last status or field update.',

    -- If the original order is deleted, all its replace requests are also deleted
    FOREIGN KEY (order_id)
    REFERENCES reward_orders(id)
    ON DELETE CASCADE,

    -- If the user account is deleted, their replace requests are also deleted
    FOREIGN KEY (user_id)
    REFERENCES auth_user(id)
    ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='Main table storing all Replace Requests. Amazon-style flow: New item delivers first, old item picked up at same time, warehouse inspects after.';
"""


# ================================================================
# TABLE 2: reward_order_replace_items
# PURPOSE : Stores which specific item(s) are being replaced.
#           Links to the original order_item for reference.
#           Also stores what the replacement product will be
#           (same or different variant).
# ================================================================
query_replace_items = """
CREATE TABLE IF NOT EXISTS reward_order_replace_items (

    id INT AUTO_INCREMENT PRIMARY KEY
    COMMENT 'Unique ID for each replace item row (auto-generated)',

    replace_request_id INT NOT NULL
    COMMENT 'Links this item to its parent replace request. FK to reward_order_replace_requests.id.',

    order_item_id INT NOT NULL
    COMMENT 'Links to the original order item being replaced. FK to reward_order_items.id. Used for history and audit.',

    product_id INT NOT NULL
    COMMENT 'FK to reward_products table. Refers to the ORIGINAL product the user received and wants to replace.',

    product_name VARCHAR(255) NOT NULL
    COMMENT 'Snapshot of the original product name at the time of request. Stored separately in case product name changes later.',

    quantity INT NOT NULL DEFAULT 1
    COMMENT 'How many units of this product the user wants to replace.',

    points INT NOT NULL
    COMMENT 'Points value per unit of this product at time of order.',

    subtotal_points INT NOT NULL
    COMMENT 'Total points for this item: quantity × points.',

    item_condition VARCHAR(100) NULL
    COMMENT 'Condition or issue reported by user for this item. Values: wrong_item, defective, damaged, wrong_color, wrong_size.',

    replacement_product_id INT NULL
    COMMENT 'FK to reward_products. The NEW product to be sent as replacement. NULL if same product is requested (replace_type = same_item).',

    replacement_product_name VARCHAR(255) NULL
    COMMENT 'Snapshot of the replacement product name. NULL if same item. Stored separately for history.',

    -- Deleting a replace request removes all its associated items
    FOREIGN KEY (replace_request_id)
    REFERENCES reward_order_replace_requests(id)
    ON DELETE CASCADE,

    -- Deleting an original order item cascades here
    FOREIGN KEY (order_item_id)
    REFERENCES reward_order_items(id)
    ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='Stores item-level details of each replace request. Tracks which product is being replaced, its condition, and what replacement product will be sent.';
"""


# ================================================================
# TABLE 3: reward_order_replace_pickups
# PURPOSE : Tracks courier/pickup details for the replace request.
#           In Amazon-style flow, delivery boy comes once:
#             - Delivers NEW replacement item to user
#             - Picks up OLD faulty item at the same time
#           This table stores both delivery + pickup info together.
# ================================================================
query_replace_pickups = """
CREATE TABLE IF NOT EXISTS reward_order_replace_pickups (

    id INT AUTO_INCREMENT PRIMARY KEY
    COMMENT 'Unique ID for each pickup record (auto-generated)',

    replace_request_id INT NOT NULL
    COMMENT 'Links this pickup record to its parent replace request. FK to reward_order_replace_requests.id.',

    order_address_id INT NOT NULL
    COMMENT 'Address where OLD item will be picked up from. FK to reward_order_address.id. Usually same as delivery address.',

    pickup_status VARCHAR(30) NOT NULL DEFAULT 'scheduled'
    COMMENT 'Status of the old-item pickup. Values: scheduled → picked_up. Or: failed, rescheduled if courier could not collect.',

    delivery_address_id INT NULL
    COMMENT 'Address where NEW replacement item will be delivered. FK to reward_order_address.id. Usually same as pickup address. NULL if not yet decided.',

    courier_name VARCHAR(100) NULL
    COMMENT 'Name of the courier/logistics partner. Example: BlueDart, Delhivery, DTDC. Set by admin when dispatching replacement.',

    tracking_number VARCHAR(100) NULL
    COMMENT 'Tracking ID for the replacement shipment. Set when replacement item is dispatched. User can use this to track delivery.',

    -- Deleting the replace request removes the pickup record too
    FOREIGN KEY (replace_request_id)
    REFERENCES reward_order_replace_requests(id)
    ON DELETE CASCADE,

    -- Address reference - restrict delete if address is in use
    FOREIGN KEY (order_address_id)
    REFERENCES reward_order_address(id)
    ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='Tracks pickup and delivery details for Amazon-style replace. One trip: delivery boy delivers new item AND collects old item simultaneously.';
"""


# ================================================================
# TABLE 4: reward_order_replace_images
# PURPOSE : Stores proof images uploaded by user when submitting
#           replace request. Example: photo of wrong color received,
#           damaged box, defective product.
#           Follows same pattern as reward_order_return_images.
# ================================================================
query_replace_images = """
CREATE TABLE IF NOT EXISTS reward_order_replace_images (

    id INT AUTO_INCREMENT PRIMARY KEY
    COMMENT 'Unique ID for each replace image (auto-generated)',

    replace_request_id INT NOT NULL
    COMMENT 'Links this image to its parent replace request. FK to reward_order_replace_requests.id. One request can have multiple images.',

    image_path VARCHAR(255) NOT NULL
    COMMENT 'File system path where image is stored. Format: app15_reward_replaces/user_{id}_{name}/replace_{id}/{date}/{filename}',

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NULL
    COMMENT 'Timestamp when this image was uploaded by user.',

    -- Delete images automatically if the replace request is deleted
    FOREIGN KEY (replace_request_id)
    REFERENCES reward_order_replace_requests(id)
    ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='Stores proof photos uploaded by user for replace request. Admin reviews these images before approving or rejecting the request.';
"""


# ================================================================
# TABLE 5: reward_order_replace_status_history
# PURPOSE : Full audit trail of every status change in a replace
#           request. Every time replace_status changes, a new row
#           is added here. Admin ya user dono ka track rehta hai.
#           Follows same pattern as reward_order_return_status_history.
# ================================================================
query_replace_status_history = """
CREATE TABLE IF NOT EXISTS reward_order_replace_status_history (

    id INT AUTO_INCREMENT PRIMARY KEY
    COMMENT 'Unique ID for each status history log entry (auto-generated)',

    replace_request_id INT NOT NULL
    COMMENT 'Links this log entry to its parent replace request. FK to reward_order_replace_requests.id.',

    status VARCHAR(50) NOT NULL
    COMMENT 'The new status this request was changed TO. Example: requested, approved, replacement_dispatched, replacement_delivered, quality_checked, closed, rejected.',

    changed_by INT NULL
    COMMENT 'FK to auth_user.id. Who made this status change — could be user (initial submit) or admin (approve/dispatch/close). NULL if system-generated.',

    remarks TEXT NULL
    COMMENT 'Internal note or reason for this status change. Example: Approved - wrong color confirmed from photos. Visible only to admin.',

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    COMMENT 'Timestamp when this status change was logged.',

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    COMMENT 'Timestamp of last update to this log entry.',

    -- Delete history logs when parent replace request is deleted
    FOREIGN KEY (replace_request_id)
    REFERENCES reward_order_replace_requests(id)
    ON DELETE CASCADE,

    -- Keep log even if admin user account is deleted
    FOREIGN KEY (changed_by)
    REFERENCES auth_user(id)
    ON DELETE SET NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='Full audit trail of all status changes for replace requests. Every status transition is recorded here with who changed it and why.';
"""


# ================================================================
# RUN ALL TABLE CREATION QUERIES IN ORDER
# ORDER MATTERS: replace_requests must be created first because
# all other tables have FK references to it.
# ================================================================

tables = [
    ("reward_order_replace_requests",     query_replace_requests),
    ("reward_order_replace_items",        query_replace_items),
    ("reward_order_replace_pickups",      query_replace_pickups),
    ("reward_order_replace_images",       query_replace_images),
    ("reward_order_replace_status_history", query_replace_status_history),
]

print("=" * 60)
print("  Creating App 15 - Replace Request Tables")
print("  Database: e_waste_recycling (MySQL)")
print("=" * 60)

all_success = True

for table_name, query in tables:
    print(f"\n>>  Creating table: {table_name} ...")
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
        print(f"   [OK]  '{table_name}' created successfully!")
    except Exception as e:
        print(f"   [ERROR]  Error creating '{table_name}':")
        print(f"            {str(e)}")
        all_success = False

print("\n" + "=" * 60)
if all_success:
    print("  [SUCCESS]  All 5 tables created successfully!")
    print("  Ready for App 15 - reward_replaces development.")
else:
    print("  [WARNING]  Some tables had errors. Check above messages.")
print("=" * 60)
