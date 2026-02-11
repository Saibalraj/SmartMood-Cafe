# Flask Hackathon App - Updated Features

## New Features Added

This update adds comprehensive **Customer Feedback** and **Food/Money Management** features with database integration.

---

## 🎯 Features Overview

### 1. **Customer Feedback System**
Customers can now provide ratings (1-5 stars) and written feedback/suggestions to the admin.

**Customer Side:**
- Navigate to: `/customer/<cid>/feedback`
- Provide a star rating (1-5)
- Write feedback/suggestions (optional)
- All feedback is stored in the database

**Admin Side:**
- View all customer feedback at: `/admin/feedbacks`
- See unread feedback count
- Mark feedback as read
- Delete feedback
- Filter by unread/read/all feedbacks

---

### 2. **Food Menu & Purchase System**
Complete food inventory management with customer purchasing capabilities.

**Customer Side:**
- Browse food menu at: `/customer/<cid>/food-menu`
- View food items with prices and availability
- Select quantity and purchase
- View purchase receipt with total price
- All purchases are tracked in database

**Admin Side:**
- Manage food items at: `/admin/food-management`
- **Add new food items** with name, price, quantity, image URL
- **Edit existing items** - update price and quantity
- **Delete items** - remove from menu
- **Real-time inventory management**
- View available/unavailable status

---

### 3. **Transaction Tracking**
Complete record of all customer purchases.

**Admin Dashboard:**
- View all transactions at: `/admin/transactions`
- See transaction ID, customer ID, food item, quantity, price
- Calculate total revenue
- Track total items sold
- Search transactions by customer ID

---

## 📊 Database Models

### **Feedback Table**
```
- id (Primary Key)
- customer_id
- rating (1-5)
- suggestion (text feedback)
- timestamp
- status (unread/read)
```

### **FoodItem Table**
```
- id (Primary Key)
- name
- base_price
- quantity
- image_url
- is_available
- created_at
- updated_at
```

### **Transaction Table**
```
- id (Primary Key)
- customer_id
- food_item_id (Foreign Key)
- quantity_purchased
- price_paid
- timestamp
```

---

## 🚀 How to Use

### **Installation**
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure `Flask-SQLAlchemy>=2.5.1` is installed (added to requirements.txt)

3. Run the Flask app:
```bash
python Flask.py
```

The database will be automatically created on first run as `hackthon.db`

---

### **Customer Workflow**

1. **Generate QR Code** - Admin generates QR for customer
2. **Submit Mood** - Customer enters emotion at `/customer/<cid>`
3. **Give Feedback** - Click "📝 Give Feedback" button
   - Rate experience (1-5 stars)
   - Write suggestions
   - Submit
4. **View Food Menu** - Click "🍔 View Food Menu"
   - Browse available items
   - Select quantity
   - Complete purchase
   - Get receipt

---

### **Admin Workflow**

1. **Login** - Admin logs in at `/admin/login`
2. **Dashboard** - View main admin dashboard at `/admin/dashboard`
3. **Manage Feedbacks** - Go to `/admin/feedbacks`
   - View all customer feedback
   - See ratings and suggestions
   - Mark as read/delete
4. **Food Management** - Go to `/admin/food-management`
   - Add new food items
   - Edit prices and quantities
   - Delete items
5. **View Transactions** - Go to `/admin/transactions`
   - See all purchases
   - Track revenue
   - Search by customer ID

---

## 📁 New Templates Added

1. `customer_feedback.html` - Customer feedback form with star rating
2. `feedback_success.html` - Success page after feedback submission
3. `admin_feedbacks.html` - Admin feedback management dashboard
4. `customer_food_menu.html` - Food menu display for customers
5. `purchase_success.html` - Purchase receipt page
6. `purchase_error.html` - Error handling for failed purchases
7. `admin_food_management.html` - Admin food item management
8. `admin_transactions.html` - Admin transactions/sales report

---

## 🔧 Updated Components

### Flask.py
- Added SQLAlchemy ORM setup
- Created 3 database models (Feedback, FoodItem, Transaction)
- Added 12+ new routes for feedback and food management
- Database auto-initialization on startup

### customer.html
- Added "📝 Give Feedback" button
- Added "🍔 View Food Menu" button

### dashboard.html
- Updated navigation with new menu items
- Added links to Feedbacks, Food Management, Transactions

### requirements.txt
- Added `Flask-SQLAlchemy>=2.5.1`

---

## 💡 Key Features

✅ **Database Persistence** - All data stored in SQLite database
✅ **Real-time Inventory** - Food quantities update automatically
✅ **Feedback Management** - Mark as read/unread, filter options
✅ **Revenue Tracking** - Automatic revenue calculation
✅ **Search Functionality** - Filter transactions by customer ID
✅ **Responsive Design** - Works on desktop and mobile
✅ **Error Handling** - Graceful error messages for purchase failures

---

## 📝 Notes

- The database file `hackthon.db` is created automatically in the project root
- All data persists between app restarts
- Admin credentials: `user: sai` | `pass: sai@143`
- Star rating is 1-5, with 5 as default
- Food quantity must be greater than 0 for purchase

---

## 🐛 Troubleshooting

**Error: "ModuleNotFoundError: No module named 'flask_sqlalchemy'"**
- Run: `pip install Flask-SQLAlchemy`

**Database issues:**
- Delete `hackthon.db` and restart the app to recreate

**Port already in use:**
- Change port in Flask.py: `app.run(host='0.0.0.0', port=5001, debug=True)`

---

## 🎨 Styling

All new pages include:
- Modern gradient backgrounds
- Responsive grid layouts
- Interactive buttons and forms
- Card-based design
- Mobile-friendly navigation
- Color-coded status badges

---

Enjoy your enhanced Flask application! 🚀
