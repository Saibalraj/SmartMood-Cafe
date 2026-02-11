# 🚀 Quick Setup Guide

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Flask-SQLAlchemy (database ORM)
- qrcode (QR code generation)
- Pillow (image processing)
- matplotlib (charts and graphs)

---

## Step 2: Run the Application

```bash
python Flask.py
```

You should see output like:
```
* Running on http://0.0.0.0:5000/
```

---

## Step 3: Access the Application

Open your browser and go to:

**Home Page:** `http://localhost:5000/`

**Admin Login:** `http://localhost:5000/admin/login`
- Username: `sai`
- Password: `sai@143`

---

## Step 4: Test the Features

### Generate a Customer QR Code
1. Go to home page
2. Enter a Customer ID (e.g., "CUSTOMER_001")
3. Click "Generate QR"
4. Scan the QR code or click the link

### Add Feedback
1. On the customer page (`/customer/<cid>`), click "📝 Give Feedback"
2. Rate the experience (1-5 stars)
3. Add any suggestions
4. Click "Send Feedback"

### Add Food Items (Admin)
1. Login as admin
2. Go to "Food Management"
3. Add food items with:
   - Food Name
   - Price (₹)
   - Quantity (Units)
4. Click "Add Food Item"

### Customer Purchases Food
1. On customer page, click "🍔 View Food Menu"
2. Select quantity and click "Buy Now"
3. View purchase receipt

### View Feedbacks (Admin)
1. Click "Feedbacks" in admin panel
2. See all customer feedback with ratings
3. Mark as read or delete

### View Transactions (Admin)
1. Click "Transactions" in admin panel
2. See all customer purchases
3. View total revenue and items sold

---

## 📊 Database

The application uses SQLite with automatic setup:
- **Database File:** `hackthon.db` (created automatically)
- **Tables:** Feedback, FoodItem, Transaction
- **Persistence:** All data persists between app restarts

---

## ⚙️ Features Included

### Customer Features
✅ Submit mood/emotion
✅ Give feedback with star rating
✅ Browse food menu
✅ Purchase food items
✅ View purchase receipts

### Admin Features
✅ View customer emotions and suggestions
✅ Manage customer feedbacks
✅ Add/Edit/Delete food items
✅ Manage food inventory/pricing
✅ View all customer transactions
✅ Track revenue and sales
✅ Search and filter data
✅ View mood analytics and trends

---

## 🔐 Admin Credentials

- **Username:** sai
- **Password:** sai@143

---

## 📞 Troubleshooting

**Port 5000 is already in use?**
- Edit Flask.py last line: `app.run(host='0.0.0.0', port=5001)`

**Flask-SQLAlchemy not installing?**
```bash
pip install Flask-SQLAlchemy==2.5.1
```

**Database issues?**
- Delete `hackthon.db` file and restart the app

**Can't scan QR on mobile?**
- Make sure your phone and computer are on the same network
- Use the IP address shown in the Flask output instead of localhost

---

## 📁 Directory Structure

```
Hackthon/
├── Flask.py                    (Main application)
├── requirements.txt            (Dependencies)
├── hackthon.db                 (Database - created on first run)
├── templates/                  (HTML files - 18 templates)
│   ├── home.html
│   ├── customer.html
│   ├── customer_feedback.html  (NEW)
│   ├── feedback_success.html   (NEW)
│   ├── customer_food_menu.html (NEW)
│   ├── purchase_success.html   (NEW)
│   ├── purchase_error.html     (NEW)
│   ├── admin_login.html
│   ├── dashboard.html
│   ├── admin_feedbacks.html    (NEW)
│   ├── admin_food_management.html (NEW)
│   ├── admin_transactions.html (NEW)
│   └── ... (other existing templates)
└── static/                     (Images, CSS, generated QR codes)
    └── ... (auto-generated)
```

---

## 🎯 Next Steps

1. **Install dependencies** → `pip install -r requirements.txt`
2. **Run the app** → `python Flask.py`
3. **Access home page** → `http://localhost:5000/`
4. **Generate QR and test features!**

---

Enjoy your enhanced Flask application! 🎉
