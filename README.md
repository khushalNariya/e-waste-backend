# ♻️ E-Waste Drop Point & Recycling Incentive Platform (Backend API)

Welcome to the backend server of the **E-Waste Drop Point & Recycling Incentive Platform**. This robust, secure, and modular Django REST Framework (DRF) application powers an environment-friendly platform where users can responsibly drop off e-waste, earn incentive points based on dynamic rules, and redeem their points for premium rewards.

---

## 🚀 Tech Stack
*   **Framework:** Django & Django REST Framework (DRF)
*   **Database:** MySQL (Structured relational data storage)
*   **Authentication:** JSON Web Tokens (JWT) via Simple JWT
*   **Environment Configuration:** `django-environ` (Secure credential handling)
*   **Image Handling:** Pillow (Custom local upload paths per module)

---

## ✨ Core Features & Module Structure
The backend is structured into specialized Django apps for maximum scalability and clean auditing:

### 👤 1. Authentication & Users (`app_1`)
*   Secure registration and login endpoints.
*   Token-based stateful authentication using JWT.

### 📍 2. E-Waste Facility Finder (`app_2` & `app_3` & `app_6` & `app_7`)
*   Mapping drop point facilities and recycling centers.
*   Category-to-brand relationships mapping for granular item recycling.

### 💰 3. Dynamic Incentives & Reward Catalog (`app_8` & `app_9` & `app_11`)
*   **Dynamic Rules Engine:** Calculates reward points based on category, brand, and weight/item count.
*   **Reward Catalog:** Lists premium products available for redemption.
*   **Points Wallet:** Tracks credited, pending, and redeemed user points.

### 📸 4. E-Waste Submission with Proofs (`app_10`)
*   Allows users to file e-waste drop/pickup requests.
*   Supports uploading multiple verification photos with automated, structured paths.
*   Status history log for full audit tracking.

### 🛒 5. E-Commerce Rewards Loop (`app_12` & `app_13`)
*   **Reward Cart:** Add, remove, and manage items in cart.
*   **Order Checkout:** Converts cart to order, registers delivery addresses, processes virtual payments, and generates order status histories.

### 🔄 6. Return & Replacement Support (`app_14` & `app_15`)
*   **Returns Management:** Form submission for returning products with mandatory image proofs, pickup schedules, status history, and points refund options.
*   **Replacement Management:** Automated workflows for product replacement requests, proof logs, and admin pickups.

---

## 📁 Project Directory Structure

```text
e_waste_recycling/
│
├── e_waste_recycling/              # Core project configurations (settings, routing, wsgi/asgi)
│
├── apps/                           # Modular backend applications grouped by function
│   │
│   ├── authentication/             # User profiles, Registration, Login & JWT Auth
│   │   └── app_1_users/
│   │
│   ├── core/                       # Core recycling and submission logic
│   │   ├── app_2_e_Facility/       # Drop point facilities
│   │   ├── app_3_Recycling_info/   # Public recycling resource portal
│   │   ├── app_5_Home/             # Banners & hero image configurations
│   │   └── app_10_E_Waste_Submission/# E-waste deposit workflows & proofs
│   │
│   ├── rewards/                    # Reward shopping cart & orders loop
│   │   ├── app_8_Reward_Rules/     # Points calculation logic
│   │   ├── app_9_Reward_Products/  # Points redeemable catalog
│   │   ├── app_11_User_Rewards/    # User wallet & transaction history
│   │   ├── app_12_Reward_Cart/     # Rewards shopping cart
│   │   ├── app_13_reward_orders/   # Reward checkouts & status tracking
│   │   ├── app_14_reward_returns/  # Rewards returns with proof uploads
│   │   └── app_15_reward_replaces/ # Rewards replacements with proof uploads
│   │
│   └── setup_data/                 # Category, Brand & Education datasets
│       ├── app_4_Education/        # Educational articles
│       ├── app_6_Brands/           # Registered brands
│       └── app_7_Category_Brand_Mapping/ # Category-brand-model relationship mappings
│
├── media/                          # Dedicated folder for user uploaded dynamic images
├── static/                         # Folder for static CSS and JavaScript files
├── manage.py                       # Django CLI tool
├── requirements.txt                # List of Python dependencies
└── .gitignore                      # Git ignored files configuration
```
---

## 🛠️ Local Installation & Setup

Follow these steps to run the backend server locally:

### 1. Prerequisites
Ensure you have **Python 3.10+** and **MySQL** installed on your system.

### 2. Setup Virtual Environment
Clone the repository and navigate inside the backend root folder:
```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database & Environment Setup
Create a `.env` file in the root folder (mirroring `.env.example`) and fill in your MySQL database credentials:
```env
DEBUG=True
SECRET_KEY=your_django_secret_key

DB_NAME=e_waste_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

### 5. Run Migrations & Server
```bash
# Run database migrations
python manage.py migrate

# Start the server
python manage.py runserver
```
The server will start running at `http://127.0.0.1:8000/`.

---

## 🛡️ License
Distributed under the MIT License. See `LICENSE` for more information.
