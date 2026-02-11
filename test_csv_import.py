#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test CSV import with proper authentication and POST request
"""
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

print("\nTesting CSV Import Feature\n" + "="*50)

# Step 1: Login
print("\n1. Admin Login...")
session = requests.Session()
login_data = {'user': 'sai', 'pass': 'sai@143'}
r = session.post(f"{BASE_URL}/admin/login", data=login_data)
print(f"   Status: {r.status_code}")

# Step 2: Test CSV Import
print("\n2. Testing CSV Import...")

csv_content = "name,base_price,quantity,image_url\n"
csv_content += "Biryani,150.00,20,\n"
csv_content += "Pizza,250.00,15,\n"
csv_content += "Burger,100.00,30,\n"

files = {'csv_file': ('foods.csv', csv_content, 'text/csv')}
r = session.post(f"{BASE_URL}/admin/food/csv-import", files=files)

print(f"   Status: {r.status_code}")
print(f"   Response: {r.text[:200]}")

if r.status_code == 200:
    try:
        result = r.json()
        print(f"\n✅ CSV Import Success!")
        print(f"   Message: {result.get('message', 'Success')}")
        print(f"   Imported: {result.get('imported', 0)} items")
    except:
        print(f"\n⚠️  Response received but not JSON")
        print(f"   Raw: {r.text[:100]}")
elif r.status_code == 401:
    print(f"\n❌ Unauthorized - Login failed")
elif r.status_code == 404:
    print(f"\n❌ Endpoint not found - Route may not be registered")
elif r.status_code == 405:
    print(f"\n❌ Method Not Allowed - Check HTTP method")
else:
    print(f"\n❌ Error: {r.status_code}")

# Step 3: Verify food items
print("\n3. Checking Food Items API...")
r = session.get(f"{BASE_URL}/api/food-items")
if r.status_code == 200:
    items = r.json()
    print(f"✅ Food items found: {len(items)}")
    for item in items[:3]:
        print(f"   - {item['name']}: ₹{item['base_price']}")
else:
    print(f"❌ API Error: {r.status_code}")

print("\n" + "="*50 + "\n")
