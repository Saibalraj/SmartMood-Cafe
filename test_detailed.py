#!/usr/bin/env python
"""
Detailed test script with error reporting
"""
import requests
import sys

BASE_URL = "http://127.0.0.1:5000"

print("="*70)
print("🧪 DETAILED FLASK APPLICATION TEST")
print("="*70 + "\n")

# Test 1: Home Page
print("1️⃣  Testing Home Page...")
try:
    r = requests.get(f"{BASE_URL}/", timeout=5)
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        print("   ✅ Home page works\n")
    else:
        print(f"   ❌ Error: {r.text[:200]}\n")
except Exception as e:
    print(f"   ❌ Exception: {e}\n")

# Test 2: Customer Page (GET - should work)
print("2️⃣  Testing Customer Registration Page (GET)...")
try:
    r = requests.get(f"{BASE_URL}/customer/TEST001", timeout=5)
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        if "Customer" in r.text or "Name" in r.text or "Email" in r.text:
            print("   ✅ Customer page loads correctly\n")
        else:
            print("   ⚠️  Page loaded but content might be incomplete\n")
    else:
        print(f"   ❌ Error response\n")
        # Print first 500 chars of error
        print(f"   Response: {r.text[:500]}\n")
except Exception as e:
    print(f"   ❌ Exception: {e}\n")

# Test 3: Mood Input Page
print("3️⃣  Testing Mood Input Page (GET)...")
try:
    r = requests.get(f"{BASE_URL}/customer/TEST001/mood", timeout=5)
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        if "emotion" in r.text.lower() or "mood" in r.text.lower():
            print("   ✅ Mood page loads correctly\n")
        else:
            print("   ⚠️  Page loaded but might be incomplete\n")
    else:
        print(f"   ❌ Error response: {r.status_code}\n")
except Exception as e:
    print(f"   ❌ Exception: {e}\n")

# Test 4: Admin Login
print("4️⃣  Testing Admin Login Page (GET)...")
try:
    r = requests.get(f"{BASE_URL}/admin/login", timeout=5)
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        if "Admin" in r.text or "Login" in r.text:
            print("   ✅ Admin login page works\n")
        else:
            print("   ⚠️  Page loaded but content might be incomplete\n")
    else:
        print(f"   ❌ Error: {r.status_code}\n")
except Exception as e:
    print(f"   ❌ Exception: {e}\n")

# Test 5: API Test
print("5️⃣  Testing Food Items API...")
try:
    r = requests.get(f"{BASE_URL}/api/food-items", timeout=5)
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        print("   ✅ API works\n")
    else:
        print(f"   ❌ Error: {r.status_code}\n")
except Exception as e:
    print(f"   ❌ Exception: {e}\n")

print("="*70)
print("✅ DETAILED TEST COMPLETE")
print("="*70)
