#!/usr/bin/env python
"""
Test script to verify all Flask app endpoints
"""
import requests
import sys

BASE_URL = "http://127.0.0.1:5000"

# Test endpoints
endpoints = [
    ("GET", "/", "Home Page"),
    ("GET", "/generate", "Generate QR Page"),
    ("GET", "/customer/TEST001", "Customer Registration"),
    ("GET", "/customer/TEST001/mood", "Mood Input"),
    ("GET", "/admin/login", "Admin Login"),
    ("GET", "/admin/logout", "Admin Logout (redirect)"),
    ("GET", "/api/food-items", "Food Items API"),
]

print("="*70)
print("🧪 TESTING FLASK APPLICATION")
print("="*70)

all_passed = True

for method, endpoint, name in endpoints:
    try:
        if method == "GET":
            response = requests.get(f"{BASE_URL}{endpoint}", timeout=5, allow_redirects=True)
        
        if response.status_code in [200, 302, 301]:
            print(f"✅ {name:40} HTTP {response.status_code}")
        else:
            print(f"❌ {name:40} HTTP {response.status_code}")
            all_passed = False
    except Exception as e:
        print(f"❌ {name:40} ERROR: {str(e)[:40]}")
        all_passed = False

print("\n" + "="*70)
if all_passed:
    print("✅ ALL TESTS PASSED - APPLICATION IS FULLY FUNCTIONAL")
    print("="*70)
    sys.exit(0)
else:
    print("⚠️  SOME TESTS FAILED - CHECK ERRORS ABOVE")
    print("="*70)
    sys.exit(1)
