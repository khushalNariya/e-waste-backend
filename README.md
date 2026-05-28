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
├── e_waste_recycling/          # Project settings, routing (urls.py) and wsgi
├── app_1_users/                # Auth & User Profiles
├── app_2_e_Facility/           # Drop Point Facility Management
├── app_3_Recycling_info/       # Recycling tips & resources
├── app_4_Education/            # Educational articles
├── app_5_Home/                 # Banner & dynamic home content
├── app_6_Brands/               # Brand entities
├── app_7_Category_Brand_Map/   # Core product mapping logic
├── app_8_Reward_Rules/         # Point calculation formulas
├── app_9_Reward_Products/      # Redeemable rewards catalog
├── app_10_E_Waste_Submission/  # E-waste deposit submissions
├── app_11_User_Rewards/        # Points tracking
├── app_12_Reward_Cart/         # Reward checkout cart
├── app_13_reward_orders/       # Order tracking & processing
├── app_14_reward_returns/      # Order returns with proofs
├── app_15_reward_replaces/     # Order replacements with proofs
│
├── manage.py                   # Django CLI
├── requirements.txt            # Package dependencies
└── .gitignore                  # Git untracked registry
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
