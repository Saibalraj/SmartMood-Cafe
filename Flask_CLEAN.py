from flask import Flask, request, redirect, url_for, session, render_template, jsonify, send_file
import qrcode, os, socket, json
from datetime import datetime, timedelta
from collections import defaultdict
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO
import re

try:
    import PyPDF2
except:
    import subprocess
    subprocess.check_call(['python', '-m', 'pip', 'install', 'PyPDF2', '-q'])
    import PyPDF2

app = Flask(__name__)
app.secret_key = "sai123"

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackathon_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Global data
customer_data = {}
user_history = defaultdict(list)
admin_overrides = {}
ADMIN_USER = "sai"
ADMIN_PASS = "sai@143"

# ========== MODELS ==========
class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    mobile = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    pdf_filename = db.Column(db.String(255), nullable=True)
    pdf_uploaded_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    suggestion = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.String(20), default='unread')

class FoodItem(db.Model):
    __tablename__ = 'food_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    base_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(200), nullable=True)
    is_available = db.Column(db.Boolean, default=True)

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_item.id'), nullable=False)
    quantity_purchased = db.Column(db.Integer, nullable=False)
    price_paid = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)

EMOTION_LEVELS = {
    "Very Happy": 5, "Happy": 4, "Neutral": 3, "Sad": 2, "Very Sad": 1,
    "Stressed": 2, "Calm": 4, "Excited": 5, "Tired": 2, "Energetic": 5,
    "Angry": 1, "Relaxed": 4, "Anxious": 1, "Focused": 4
}

# ========== HELPER FUNCTIONS ==========
def extract_data_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        extracted_text = ""
        for page in pdf_reader.pages:
            extracted_text += page.extract_text() + "\n"
        
        data = {}
        name_match = re.search(r'(?:Name|name)\s*[:]\s*([^\n]+)', extracted_text)
        if name_match:
            data['name'] = name_match.group(1).strip()
        age_match = re.search(r'(?:Age|age)\s*[:]\s*(\d+)', extracted_text)
        if age_match:
            data['age'] = int(age_match.group(1))
        mobile_match = re.search(r'(?:Mobile|mobile|Phone|phone)\s*[:]\s*([\d\s\-\+]+)', extracted_text)
        if mobile_match:
            data['mobile'] = mobile_match.group(1).strip()
        email_match = re.search(r'(?:Email|email)\s*[:]\s*([^\s\n]+@[^\s\n]+)', extracted_text)
        if email_match:
            data['email'] = email_match.group(1).strip()
        return data
    except Exception as e:
        print(f"PDF error: {e}")
        return {}

def save_uploaded_pdf(pdf_file, customer_id):
    try:
        os.makedirs('static/uploads', exist_ok=True)
        filename = f"customer_{customer_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join('static/uploads', filename)
        pdf_file.save(filepath)
        return filename
    except Exception as e:
        print(f"Save PDF error: {e}")
        return None

def ai_suggestion(cid, mood):
    suggestions = {
        "Very Happy": "🎶 Upbeat music | 🎉 Celebrate",
        "Happy": "🎶 Upbeat music | ☕ Coffee",
        "Neutral": "🎵 Balanced music | 💭 Journal",
        "Sad": "🎧 Comfort music | 🍫 Treat",
        "Very Sad": "🎧 Music | 🏥 Support",
        "Stressed": "🎼 Calm music | 🧘 Meditate",
        "Calm": "🌿 Nature | 🚶 Walk",
        "Excited": "🎯 Plan | 🏃 Exercise",
        "Tired": "🎵 Soft music | 😴 Rest",
        "Energetic": "💪 Exercise | 🏃 Sports",
        "Angry": "🌿 Nature | 🧘 Breathing",
        "Relaxed": "🎵 Music | ☕ Tea",
        "Anxious": "🧘 Breathing | 🌿 Nature",
        "Focused": "🎵 Focus music | ☕ Coffee"
    }
    return suggestions.get(mood, "Take a break")

# ========== ROUTES ==========
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    cid = request.form.get('cid', '').strip()
    if not cid:
        return render_template('home.html', error='ID required'), 400
    
    def get_local_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return '127.0.0.1'
    
    local_ip = get_local_ip()
    host_base = request.host_url.rstrip('/') if local_ip.startswith('127.') else f"http://{local_ip}:5000"
    link = f"{host_base}/customer/{cid}"
    
    img = qrcode.make(link)
    os.makedirs('static', exist_ok=True)
    qr_path = os.path.join('static', f"qr_{cid}.png")
    img.save(qr_path)
    
    return render_template('generate.html', link=link, qr_filename=f"qr_{cid}.png")

@app.route('/customer/<cid>', methods=['GET', 'POST'])
def customer(cid):
    if request.method == 'POST':
        if 'pdf_file' in request.files:
            pdf_file = request.files['pdf_file']
            if pdf_file and pdf_file.filename.endswith('.pdf'):
                extracted_data = extract_data_from_pdf(pdf_file)
                if extracted_data and 'name' in extracted_data:
                    name = extracted_data.get('name', '').strip()
                    age = extracted_data.get('age')
                    mobile = extracted_data.get('mobile', '').strip()
                    email = extracted_data.get('email', '').strip()
                    pdf_filename = save_uploaded_pdf(pdf_file, cid)
                    
                    existing = Customer.query.filter_by(customer_id=cid).first()
                    if existing:
                        existing.name = name
                        existing.age = age
                        existing.mobile = mobile
                        existing.email = email
                        existing.pdf_filename = pdf_filename
                        existing.pdf_uploaded_at = datetime.now()
                    else:
                        new_customer = Customer(customer_id=cid, name=name, age=age, mobile=mobile, email=email, pdf_filename=pdf_filename, pdf_uploaded_at=datetime.now())
                        db.session.add(new_customer)
                    
                    db.session.commit()
                    return redirect(url_for('mood_input', cid=cid))
        
        elif 'name' in request.form:
            name = request.form.get('name', '').strip()
            age = request.form.get('age', type=int) if request.form.get('age') else None
            mobile = request.form.get('mobile', '').strip()
            email = request.form.get('email', '').strip()
            
            if not name:
                return render_template('customer_details.html', cid=cid, error='Name required'), 400
            
            existing = Customer.query.filter_by(customer_id=cid).first()
            if existing:
                existing.name = name
                existing.age = age
                existing.mobile = mobile
                existing.email = email
            else:
                new_customer = Customer(customer_id=cid, name=name, age=age, mobile=mobile, email=email)
                db.session.add(new_customer)
            
            db.session.commit()
            return redirect(url_for('mood_input', cid=cid))
        
        else:
            mood = request.form.get('mood')
            intensity = request.form.get('intensity', '3')
            notes = request.form.get('notes', '')
            
            customer_data[cid] = mood
            mood_entry = {'mood': mood, 'intensity': int(intensity), 'notes': notes, 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            user_history[cid].append(mood_entry)
            
            suggestion = ai_suggestion(cid, mood)
            return render_template('customer_thanks.html', mood=mood, suggestion=suggestion)
    
    existing = Customer.query.filter_by(customer_id=cid).first()
    if not existing:
        return render_template('customer_details.html', cid=cid)
    
    return render_template('customer.html', cid=cid, emotion_levels=EMOTION_LEVELS)

@app.route('/customer/<cid>/mood', methods=['GET'])
def mood_input(cid):
    customer_obj = Customer.query.filter_by(customer_id=cid).first()
    if not customer_obj:
        return redirect(url_for('customer', cid=cid))
    return render_template('customer.html', cid=cid, emotion_levels=EMOTION_LEVELS)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        user = request.form.get('user', '')
        password = request.form.get('pass', '')
        if user == ADMIN_USER and password == ADMIN_PASS:
            session['admin'] = True
            return redirect('/admin/dashboard')
        return render_template('admin_login.html', error='Invalid'), 401
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def dashboard():
    if not session.get('admin'):
        return redirect('/admin/login')
    
    items = []
    customers = Customer.query.all()
    
    for customer_obj in customers:
        cid = customer_obj.customer_id
        mood = customer_data.get(cid, 'Not recorded')
        items.append({
            'cid': cid,
            'name': customer_obj.name,
            'age': customer_obj.age,
            'mobile': customer_obj.mobile,
            'email': customer_obj.email,
            'mood': mood,
            'pdf_filename': customer_obj.pdf_filename or 'Not uploaded',
            'pdf_uploaded_at': customer_obj.pdf_uploaded_at.strftime('%Y-%m-%d %H:%M:%S') if customer_obj.pdf_uploaded_at else 'N/A'
        })
    
    return render_template('dashboard.html', items=items)

@app.route('/admin/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')

@app.route('/api/food-items')
def api_food_items():
    food_items = FoodItem.query.filter_by(is_available=True).all()
    items_data = [{'id': item.id, 'name': item.name, 'base_price': item.base_price, 'quantity': item.quantity} for item in food_items]
    return jsonify(items_data)

@app.route('/customer/<cid>/feedback', methods=['GET', 'POST'])
def customer_feedback(cid):
    if request.method == 'POST':
        rating = request.form.get('rating', 5, type=int)
        suggestion = request.form.get('suggestion', '')
        feedback_obj = Feedback(customer_id=cid, rating=rating, suggestion=suggestion)
        db.session.add(feedback_obj)
        db.session.commit()
        return render_template('feedback_success.html', customer_id=cid)
    return render_template('customer_feedback.html', cid=cid)

@app.route('/admin/feedbacks')
def view_feedbacks():
    if not session.get('admin'):
        return redirect('/admin/login')
    feedbacks = Feedback.query.all()
    return render_template('admin_feedbacks.html', feedbacks=feedbacks)

@app.route('/customer/<cid>/food-menu')
def customer_food_menu(cid):
    food_items = FoodItem.query.filter_by(is_available=True).all()
    return render_template('customer_food_menu.html', cid=cid, food_items=food_items)

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/uploads', exist_ok=True)
    
    with app.app_context():
        db.create_all()
        print("✅ Database initialized")
    
    print("\n" + "="*70)
    print("🚀 HACKATHON FLASK APPLICATION")
    print("="*70)
    print("📱 Local: http://127.0.0.1:5000")
    print("👤 Admin: username=sai, password=sai@143")
    print("="*70 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
