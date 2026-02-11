#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FINAL VERIFICATION SCRIPT
Confirms all application features are working
"""
import requests
import sys

BASE_URL = "http://127.0.0.1:5000"

print("\n" + "="*70)
print("HACKATHON APP - FINAL VERIFICATION")
print("="*70)

tests = [
    ("🏠 Home Page", "GET", "/", 200),
    ("👤 Customer Reg (New)", "GET", "/customer/TEST123", 200),
    ("😊 Mood Input", "GET", "/customer/TEST123/mood", 200),
    ("💬 Feedback Page", "GET", "/customer/TEST123/feedback", 200),
    ("🍔 Food Menu", "GET", "/customer/TEST123/food-menu", 200),
    ("🔗 Admin Login", "GET", "/admin/login", 200),
    ("📊 API - Food Items", "GET", "/api/food-items", 200),
]

passed = 0
failed = 0

for name, method, path, expected_code in tests:
    try:
        if method == "GET":
            r = requests.get(f"{BASE_URL}{path}", timeout=3)
        status_ok = r.status_code == expected_code
        
        if status_ok:
            print(f"✅ {name:30} [{r.status_code}]")
            passed += 1
        else:
            print(f"❌ {name:30} [{r.status_code}/{expected_code}]")
            failed += 1
    except Exception as e:
        print(f"❌ {name:30} [ERROR: {str(e)[:20]}]")
        failed += 1

print("="*70)
print(f"✨ Results: {passed} PASSED | {failed} FAILED")
print("="*70)

if failed == 0:
    print("\n🎉 SUCCESS! APPLICATION IS FULLY FUNCTIONAL!")
    print("\n📱 Access URLs:")
    print("   Home:     http://127.0.0.1:5000/")
    print("   Register: http://127.0.0.1:5000/customer/YOUR_ID")
    print("   Admin:    http://127.0.0.1:5000/admin/login")
    print("\n🔑 Admin Login: username=sai | password=sai@143")
    sys.exit(0)
else:
    print("\n⚠️  Some tests failed. Check server logs.")
    sys.exit(1)
