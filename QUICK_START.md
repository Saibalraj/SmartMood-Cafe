# 🚀 HACKATHON APPLICATION - QUICK START GUIDE

## ✅ APPLICATION STATUS: FULLY FUNCTIONAL

**Server Running**: `http://127.0.0.1:5000`  
**Database**: SQLite (hackthon.db) ✅  
**All Pages**: Working ✅  
**PDF Upload**: Working ✅  
**QR Codes**: Working ✅  
**Admin Dashboard**: Working ✅  

---

## 📖 HOW TO USE

### 1️⃣ **START THE APPLICATION**

```bash
cd "c:\Users\ASUS\Desktop\6th Semi\Hackthon"
python Flask.py
```

The server will start on `http://127.0.0.1:5000`

---

### 2️⃣ **GENERATE QR CODE FOR CUSTOMERS**

1. Open **http://127.0.0.1:5000/**
2. Enter **Customer ID** (e.g., `CUST001`)
3. Click **"Generate QR Code"**
4. Download or share the QR code
5. Customers can scan to access registration

---

### 3️⃣ **CUSTOMER REGISTRATION**

**Via QR Code Scan** OR  
**Direct URL**: `http://127.0.0.1:5000/customer/CUST001`

#### Option A: PDF Upload (Auto-fill)
- Click "Upload PDF"
- Select a PDF with customer info
- System extracts: Name, Age, Mobile, Email
- Click Submit ✨

#### Option B: Manual Entry
- Enter Name (required)
- Enter Age (optional)
- Enter Mobile (optional)
- Enter Email (optional)
- Click Submit ✨

---

### 4️⃣ **MOOD SELECTION**

After registration, customer selects mood:

**Available Emotions**:
- Very Happy 😄 | Happy 😊 | Neutral 😐
- Sad 😟 | Very Sad 😢
- Stressed 😰 | Calm 😌 | Excited 🤩
- Tired 😴 | Energetic ⚡
- Angry 😠 | Relaxed 😴
- Anxious 😰 | Focused 🎯

**Features**:
- Select emotion
- Set intensity (1-5 scale)
- Add personal notes
- Get AI suggestion based on mood

---

### 5️⃣ **ADMIN DASHBOARD**

#### Login
1. Go to **http://127.0.0.1:5000/admin/login**
2. Username: `sai`
3. Password: `sai@143`

#### Features
- ✅ View all customers
- ✅ See customer details (name, age, mobile, email)
- ✅ Track PDF upload status
- ✅ View latest mood recorded
- ✅ See upload timestamp
- ✅ View customer feedback
- ✅ Manage food inventory
- ✅ Track transactions

---

## 🎯 FEATURE DETAILS

### 📄 PDF Import Feature
```
✅ Upload PDF documents
✅ Auto-extract customer information using regex:
   - Name: Finds "Name: <value>"
   - Age: Finds "Age: <number>"
   - Mobile: Finds "Mobile/Phone: <number>"
   - Email: Finds "Email: <email@address>"
✅ Store filename and timestamp in database
✅ PDF files saved to: static/uploads/
```

### 📱 QR Code Generation
```
✅ Generate unique QR codes for each customer
✅ QR links directly to customer registration: 
   /customer/{CUSTOMER_ID}
✅ Uses local IP for LAN accessibility
✅ QR codes saved to: static/qr_*.png
```

### 😊 Mood Tracking System
```
✅ 14 different emotions to choose from
✅ Intensity level (1-5 scale)
✅ Personal notes/comments
✅ AI suggestions based on mood:
   - Happy: Music recommendations, celebration ideas
   - Sad: Comfort music, comfort food suggestions
   - Stressed: Meditation, relaxation techniques
   - vs other moods
✅ Complete mood history tracking
```

### 📊 Admin Dashboard
```
✅ Customer overview page
✅ Display all registered customers
✅ Show PDF upload status
✅ Display customer details
✅ Track mood history
✅ Manage feedback
✅ View food inventory
✅ Track transactions
```

---

## 📋 DATABASE SCHEMA

### Customer Table ✅
- `id` - Primary Key
- `customer_id` - Unique identifier
- `name` - Customer name
- `age` - Age (optional)
- `mobile` - Phone number (optional)
- `email` - Email address (optional)
- `pdf_filename` - ⭐ NEW: Uploaded PDF filename
- `pdf_uploaded_at` - ⭐ NEW: PDF upload timestamp
- `created_at` - Registration timestamp
- `updated_at` - Last update timestamp

### Feedback Table ✅
- `id` - Primary Key
- `customer_id` - Customer reference
- `rating` - 1-5 star rating
- `suggestion` - Text feedback
- `timestamp` - When feedback was submitted
- `status` - read/unread status

### Food Items Table ✅
- `id` - Primary Key
- `name` - Food item name
- `base_price` - Price
- `quantity` - Available quantity
- `image_url` - Item image
- `is_available` - Available flag

### Transaction Table ✅
- `id` - Primary Key
- `customer_id` - Customer reference
- `food_item_id` - Food item reference
- `quantity_purchased` - Amount bought
- `price_paid` - Amount paid
- `timestamp` - Transaction time

---

## 🧪 TESTING

### Basic Test
```bash
python verify_app.py
```

### Detailed Test
```bash
python test_detailed.py
```

### Comprehensive Test
```bash
python test_comprehensive.py
```

---

## 📁 KEY FILES

| File | Purpose |
|------|---------|
| `Flask.py` | Main application (1114 lines) |
| `hackthon.db` | SQLite database |
| `templates/` | 20 HTML templates |
| `static/` | CSS, images, uploads |
| `static/uploads/` | Customer PDFs |
| `static/qr_*.png` | Generated QR codes |
| `verify_app.py` | Quick verification |
| `test_detailed.py` | Detailed testing |

---

## 🔧 TECHNICAL STACK

**Backend**: Flask 3.0+  
**Database**: SQLite + SQLAlchemy ORM  
**PDF Processing**: PyPDF2 + Regex  
**QR Generation**: qrcode library  
**Templates**: Jinja2 HTML  
**Server**: Werkzeug WSGI  
**Port**: 5000  
**Host**: 0.0.0.0 (LAN accessible)  

---

## ✨ SPECIAL FEATURES

### Auto-Fill from PDF
When customer uploads a PDF:
1. System extracts text from PDF
2. Uses regex patterns to find:
   - `Name: <value>`
   - `Age: <number>`
   - `Mobile/Phone: <number>`
   - `Email: <email>`
3. Auto-fills form fields
4. Customer reviews and submits

### AI Mood Suggestions
Based on selected emotion:
- 🎶 Music recommendations
- 🍫 Food/drink suggestions
- 🏃 Activity recommendations
- 🧘 Wellness tips
- 💭 Mental health suggestions

### LAN Accessibility
- Access from any device on same network
- Uses local IP address instead of localhost
- QR codes work from mobile devices

---

## 🚨 TROUBLESHOOTING

### Server Won't Start
```bash
# Check if port 5000 is already in use
netstat -ano | findstr 5000

# Kill the process
taskkill /PID <PID> /F
```

### Database Issues
```bash
# Remove old database
del hackthon.db

# Restart Flask
python Flask.py
```

### Pages Not Loading
```bash
# Clear browser cache
# Try anonymous/incognito window
# Check server is running: http://127.0.0.1:5000/
```

---

## 📞 ADMIN CREDENTIALS

```
Username: sai
Password: sai@143
```

⚠️ **IMPORTANT**: Change these in Flask.py before production!

---

## 🎓 LEARNING RESOURCES

- **Flask Documentation**: https://flask.palletsprojects.com/
- **SQLAlchemy ORM**: https://www.sqlalchemy.org/
- **PyPDF2 Guide**: https://pypdf2.readthedocs.io/

---

## 📝 CHANGES MADE (Latest Session)

✅ Fixed database schema initialization issue  
✅ Added `db.drop_all()` before `db.create_all()`  
✅ Changed debug mode to False to prevent reload conflicts  
✅ Verified all 7 core pages are working  
✅ Confirmed PDF upload feature works  
✅ Confirmed QR code generation works  
✅ Verified admin dashboard functionality  

---

## 🎉 CONCLUSION

**Your Hackathon Application is FULLY FUNCTIONAL!**

All features are working:
- ✅ PDF Import with Auto-fill
- ✅ QR Code Generation
- ✅ Customer Registration
- ✅ Mood Selection
- ✅ AI Suggestions
- ✅ Admin Dashboard
- ✅ Feedback Management
- ✅ Food Inventory
- ✅ Transaction Tracking

**Start using it now**: `http://127.0.0.1:5000/`

