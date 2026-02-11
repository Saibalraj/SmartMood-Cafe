# 📚 API Documentation & Database Schema

## 🗄️ Database Schema

### Feedback Table
```sql
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id VARCHAR(50) NOT NULL,
    rating INTEGER NOT NULL,           -- 1-5 stars
    suggestion TEXT,                   -- optional text feedback
    timestamp DATETIME DEFAULT NOW(),
    status VARCHAR(20) DEFAULT 'unread' -- 'unread' or 'read'
);
```

**Indexes:** customer_id, status, timestamp

---

### FoodItem Table
```sql
CREATE TABLE food_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    base_price FLOAT NOT NULL,
    quantity INTEGER DEFAULT 0,        -- available units
    image_url VARCHAR(200),
    is_available BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT NOW()
);
```

**Indexes:** name, is_available

---

### Transaction Table
```sql
CREATE TABLE transaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id VARCHAR(50) NOT NULL,
    food_item_id INTEGER NOT NULL,    -- Foreign Key to FoodItem
    quantity_purchased INTEGER NOT NULL,
    price_paid FLOAT NOT NULL,
    timestamp DATETIME DEFAULT NOW()
);
```

**Indexes:** customer_id, food_item_id, timestamp

---

## 🔌 REST API Endpoints

### Customer Feedback Endpoints

#### GET - View Feedback Form
```
GET /customer/<cid>/feedback
```
**Response:** HTML form for feedback submission
**Parameters:** 
- `cid` (path) - Customer ID

---

#### POST - Submit Feedback
```
POST /customer/<cid>/feedback
Content-Type: application/x-www-form-urlencoded

rating=5&suggestion=Great+service!
```
**Parameters:**
- `cid` (path) - Customer ID
- `rating` (form) - 1-5 star rating
- `suggestion` (form) - Optional text feedback

**Response:** Redirect to feedback success page

---

### Food Management Endpoints

#### GET - View Food Menu
```
GET /customer/<cid>/food-menu
```
**Response:** HTML page with available food items

---

#### POST - Purchase Food
```
POST /customer/<cid>/buy-food
Content-Type: application/x-www-form-urlencoded

food_item_id=1&quantity=2
```
**Parameters:**
- `cid` (path) - Customer ID
- `food_item_id` (form) - Food item ID
- `quantity` (form) - Quantity to purchase

**Response:** Purchase receipt or error page

---

#### GET - API Get Food Items
```
GET /api/food-items
```
**Response:** JSON array
```json
[
    {
        "id": 1,
        "name": "Biryani",
        "base_price": 199.99,
        "quantity": 50,
        "image_url": "https://..."
    }
]
```

---

### Admin Feedback Management Endpoints

#### GET - View All Feedbacks
```
GET /admin/feedbacks
```
**Auth:** Admin session required
**Response:** HTML dashboard with all feedbacks

---

#### POST - Mark Feedback as Read
```
POST /admin/feedback/<feedback_id>/mark-read
Content-Type: application/json
```
**Auth:** Admin session required
**Response:**
```json
{"status": "success"}
```

---

#### POST - Delete Feedback
```
POST /admin/feedback/<feedback_id>/delete
Content-Type: application/json
```
**Auth:** Admin session required
**Response:**
```json
{"status": "success"}
```

---

### Admin Food Management Endpoints

#### GET - Food Management Dashboard
```
GET /admin/food-management
```
**Auth:** Admin session required
**Response:** HTML with food items and management forms

---

#### POST - Add Food Item
```
POST /admin/food/add
Content-Type: application/json

{
    "name": "Biryani",
    "base_price": 199.99,
    "quantity": 50,
    "image_url": "https://..."
}
```
**Auth:** Admin session required
**Response:**
```json
{
    "status": "success",
    "id": 1,
    "message": "Food item added successfully"
}
```

---

#### POST - Update Food Item
```
POST /admin/food/<food_id>/update
Content-Type: application/json

{
    "name": "Biryani",
    "base_price": 199.99,
    "quantity": 50,
    "image_url": "https://..."
}
```
**Auth:** Admin session required
**Response:**
```json
{"status": "success", "message": "Food item updated successfully"}
```

---

#### POST - Delete Food Item
```
POST /admin/food/<food_id>/delete
Content-Type: application/json
```
**Auth:** Admin session required
**Response:**
```json
{"status": "success", "message": "Food item deleted"}
```

---

### Admin Transaction Endpoints

#### GET - View All Transactions
```
GET /admin/transactions
```
**Auth:** Admin session required
**Response:** HTML with transaction table and statistics

---

## 🔐 Authentication

All admin endpoints require:
```python
if not session.get('admin'):
    return redirect('/admin/login')
```

**Admin Credentials:**
- Username: `sai`
- Password: `sai@143`

---

## 📋 Response Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 301 | Redirect (e.g., to login) |
| 400 | Bad request (insufficient inventory) |
| 401 | Unauthorized (not admin) |
| 404 | Not found (item doesn't exist) |

---

## 💾 Data Examples

### Feedback Entry
```python
{
    "id": 1,
    "customer_id": "CUSTOMER_001",
    "rating": 5,
    "suggestion": "Great service, very happy with the food!",
    "timestamp": "2026-02-10 15:30:45",
    "status": "unread"
}
```

### Food Item Entry
```python
{
    "id": 1,
    "name": "Biryani",
    "base_price": 199.99,
    "quantity": 50,
    "image_url": "https://example.com/biryani.jpg",
    "is_available": True,
    "created_at": "2026-02-10 10:00:00",
    "updated_at": "2026-02-10 15:30:00"
}
```

### Transaction Entry
```python
{
    "id": 1,
    "customer_id": "CUSTOMER_001",
    "food_item_id": 1,
    "quantity_purchased": 2,
    "price_paid": 399.98,
    "timestamp": "2026-02-10 15:45:30"
}
```

---

## 🔄 Business Logic

### Feedback Workflow
1. Customer submits feedback with rating (1-5) and optional suggestion
2. Feedback stored in DB with `status='unread'`
3. Admin views dashboard showing unread count
4. Admin clicks "Mark as Read" to change `status='read'`
5. Admin can delete feedback if needed

### Purchase Workflow
1. Customer views available food items (`is_available=True`, `quantity>0`)
2. Customer selects quantity (max = item.quantity)
3. System creates transaction record
4. System reduces item quantity by purchased amount
5. If quantity becomes 0, set `is_available=False`
6. Customer receives receipt with total price

### Admin Inventory Management
1. Admin adds food item (base_price, quantity, name)
2. System automatically sets `is_available=True` if quantity > 0
3. Admin can edit price and quantity
4. When quantity becomes 0 via edit, set `is_available=False`
5. Admin can delete item completely

---

## 📊 Queries

### Get All Unread Feedbacks
```python
unread = Feedback.query.filter_by(status='unread').all()
```

### Get Total Revenue
```python
total = db.session.query(func.sum(Transaction.price_paid)).scalar()
```

### Get Available Food Items
```python
items = FoodItem.query.filter_by(is_available=True).all()
```

### Get Customer Transactions
```python
transactions = Transaction.query.filter_by(customer_id=cid).all()
```

### Update Inventory After Purchase
```python
food_item.quantity -= quantity_purchased
if food_item.quantity == 0:
    food_item.is_available = False
db.session.commit()
```

---

## 🛡️ Error Handling

### Purchase Errors
- ❌ Item not found → 404
- ❌ Insufficient quantity → 400
- ❌ Not available → 400

### Admin Errors
- ❌ Not authenticated → Redirect to login
- ❌ Item not found → 404 JSON

---

## 📈 Future Enhancements

- [ ] Payment gateway integration
- [ ] Email notifications for feedback
- [ ] Inventory alerts for low stock
- [ ] Advanced search filters
- [ ] Export data to CSV
- [ ] Dashboard analytics charts
- [ ] Customer order history
- [ ] Product ratings/reviews

---

For more information, see `FEATURES_GUIDE.md` and `SETUP_GUIDE.md`
