# Flask Application - Enhanced Features Documentation

## 🎯 New Features Added

### 1. **Customer Details Capture** 
After scanning the QR code, customers are prompted to enter:
- **Name** (required)
- **Age** (optional)
- **Mobile Number** (optional, 10 digits format)
- **Email** (optional)

All customer details are stored in the database with timestamps.

---

### 2. **PDF Report Generation**
**Admin Dashboard Feature:**
- Each customer card now has a **"📄 Download PDF"** button
- PDF includes:
  - Complete customer information (Name, Age, Mobile, Email)
  - Create date
  - Last 10 mood history entries with timestamps
  - Professional formatting with tables

**Route:** `/admin/customer/<cid>/pdf`

**File:** Downloads as `customer_<CID>_<DATE>.pdf`

---

### 3. **Excel Export**
**Location:** Dashboard - "📊 Export All Customers (Excel)" button

**Features:**
- Exports **ALL customers** to a single Excel sheet
- Includes columns:
  - Customer ID
  - Name
  - Age
  - Mobile Number
  - Email
  - Current Mood
  - Total Mood Entries
  - Created Date
- Auto-formatted columns with proper styling
- Blue header row with white text

**Route:** `/admin/export-excel`

**File:** Downloads as `customers_<TIMESTAMP>.xlsx`

---

### 4. **Excel Import**
**Location:** Dashboard - "📁 Import Customers (Excel)" button

**Features:**
- Bulk upload customer data via Excel file
- Drag & drop interface for easy file selection
- Validates data before import:
  - Required fields: Customer ID, Name
  - Mobile number must be 10 digits
  - Age must be numeric
- Shows import results with success/error counts
- Detailed error messages for failed rows

**Supported Formats:** .xlsx, .xls

**Route:** `/admin/import-excel` (GET and POST)

**Excel Template Structure:**
```
| Customer ID | Name          | Age | Mobile     | Email              |
|-------------|---------------|-----|------------|-------------------|
| C001        | John Doe      | 28  | 9876543210 | john@example.com  |
| C002        | Jane Smith    | 32  | 9876543211 | jane@example.com  |
```

---

## 📊 Admin Dashboard Updates

The admin dashboard now displays:
1. **Customer Information Section** (with blue background)
   - Name
   - Age (if provided)
   - Mobile Number (if provided)
   - Email (if provided)

2. **Action Buttons**
   - 📄 Download PDF - Generate PDF report for individual customer
   - 📜 View History - See full mood history
   - ❌ Remove Override - Delete custom suggestion

3. **Top Navigation Buttons** (New)
   - 📊 Export All Customers (Excel)
   - 📁 Import Customers (Excel)

---

## 🗄️ Database Schema

### New Table: `Customer`
```python
id (Integer, Primary Key)
customer_id (String, Unique, Not Null)
name (String, Not Null)
age (Integer, Nullable)
mobile (String, Nullable)
email (String, Nullable)
created_at (DateTime, Default: Now)
updated_at (DateTime, Default: Now)
```

---

## 🔄 Customer Journey Flow

1. **Customer Scans QR Code**
   - Redirected to `/customer/<cid>`

2. **Enters Customer Details** (NEW)
   - Form: `customer_details.html`
   - Saves to Customer database table
   - Validates mobile format

3. **Records Mood**
   - Form: `customer.html`
   - Mood, Intensity, and Notes recorded

4. **Gets AI Suggestion**
   - Based on mood and history

5. **Admin Views Details**
   - Dashboard shows all customer info
   - Can download PDF report
   - Can export data to Excel

---

## 🛠️ Technical Details

### New Dependencies
- **reportlab** - PDF generation with tables and formatting
- **openpyxl** - Excel file handling (import/export)
- **re** - Regular expressions for validation

### New Routes
| Method | Route | Purpose |
|--------|-------|---------|
| GET, POST | `/customer/<cid>` | Customer details form |
| GET | `/customer/<cid>/mood` | Mood input after details |
| GET | `/admin/customer/<cid>/pdf` | Generate PDF |
| GET | `/admin/export-excel` | Download Excel |
| GET, POST | `/admin/import-excel` | Import Excel |

### Data Validation
- **Name:** Required, max 100 characters
- **Age:** Optional, numeric, 1-120
- **Mobile:** Optional, exactly 10 digits
- **Email:** Optional, valid email format

---

## 📝 Error Handling

### Excel Import Validation
- File must be .xlsx or .xls format
- Validates each row before import
- Shows detailed error messages with row numbers
- Continues importing valid rows even if some fail
- Displays success count and error list

### PDF Generation
- Handles missing customer data gracefully
- Shows "N/A" for empty fields
- Truncates long notes in tables

---

## 🎨 UI Improvements

### Customer Details Form
- Professional gradient background
- Input validation with visual feedback
- Required field indicators
- Mobile-responsive design
- Success/error messages with colored backgrounds

### Admin Import Page
- Drag & drop file upload
- Excel template example shown
- Detailed instructions
- Progress feedback during upload
- Error list with row numbers

### Dashboard Updates
- Customer details card with blue background
- Action buttons for PDF and Excel operations
- Clear visual hierarchy
- Color-coded buttons for different actions

---

## 🚀 Usage Examples

### Export Customer Data
1. Click **"📊 Export All Customers (Excel)"** on dashboard
2. File downloads as `customers_20260211_143025.xlsx`
3. Open with Excel/Google Sheets

### Import Customer Data
1. Click **"📁 Import Customers (Excel)"** on dashboard
2. Use template format or drag & drop Excel file
3. System validates and imports data
4. See success message with count

### Generate PDF Report
1. Click **"📄 Download PDF"** on customer card
2. PDF downloads with all customer details
3. Share with stakeholders or store for records

---

## 🔐 Security Notes
- All operations require admin login (except customer entry)
- Validation prevents invalid data in database
- PDF routes protected by admin session check
- Excel import validates email and mobile formats

---

## 📱 Mobile Compatibility
- Customer details form is fully responsive
- Works on mobile devices via QR code scan
- Admin dashboard responsive for tablet viewing
- Excel import works on all devices

---

**Created:** February 11, 2026
**Version:** 2.0
