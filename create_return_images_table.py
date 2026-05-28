import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_waste_recycling.settings')
django.setup()

from django.db import connection

query = """
CREATE TABLE IF NOT EXISTS reward_order_return_images (
    id INT AUTO_INCREMENT PRIMARY KEY 
    COMMENT 'Unique ID for each return image',

    return_request_id INT NOT NULL 
    COMMENT 'Links image to return request. FK to reward_order_return_requests.id',

    image_path VARCHAR(255) NOT NULL 
    COMMENT 'File path or URL where image is saved',

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP 
    COMMENT 'Time when the image was uploaded',

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 
    COMMENT 'Time when the image was updated',

    -- Delete images automatically if the return request is deleted
    FOREIGN KEY (return_request_id) 
    REFERENCES reward_order_return_requests(id) 
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

print("Connecting to the database and creating reward_order_return_images table...")
try:
    with connection.cursor() as cursor:
        cursor.execute(query)
    print("Table 'reward_order_return_images' created successfully in MySQL!")
except Exception as e:
    print("An error occurred:")
    print(str(e))
