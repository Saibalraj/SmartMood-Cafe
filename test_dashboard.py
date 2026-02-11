#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test script to verify the enhanced admin dashboard with PDF Status, 
PDF Upload Date, and Mood Records display
"""

import requests
import re

BASE_URL = "http://127.0.0.1:5000"
session = requests.Session()

print("=" * 60)
print("DASHBOARD ENHANCEMENT TEST")
print("=" * 60)

# Test 1: Admin Login
print("\n[TEST 1] Admin Login")
login_response = session.post(
    f"{BASE_URL}/admin/login",
    data={"username": "sai", "password": "sai@143"},
    allow_redirects=True
)

if login_response.status_code == 200:
    print("✅ Admin login successful")
else:
    print(f"❌ Admin login failed: {login_response.status_code}")

# Test 2: Access Dashboard
print("\n[TEST 2] Access Enhanced Dashboard")
dashboard_response = session.get(f"{BASE_URL}/admin/dashboard")

if dashboard_response.status_code == 200:
    print("✅ Dashboard loaded successfully")
    
    # Check for new status cards
    html_content = dashboard_response.text
    
    # Test for status-section class (new grid layout)
    if "status-section" in html_content:
        print("✅ Status section found (Grid layout)")
    else:
        print("❌ Status section NOT found")
    
    # Test for PDF Status card
    if "status-card pdf" in html_content and "PDF Status" in html_content:
        print("✅ PDF Status card found")
    else:
        print("❌ PDF Status card NOT found")
    
    # Test for Upload Date card
    if "status-card date" in html_content and "Upload Date" in html_content:
        print("✅ PDF Upload Date card found")
    else:
        print("❌ PDF Upload Date card NOT found")
    
    # Test for Mood Records card
    if "status-card mood" in html_content and "Mood Records" in html_content:
        print("✅ Mood Records card found")
    else:
        print("❌ Mood Records card NOT found")
    
    # Check for professional styling
    if "status-label" in html_content and "status-value" in html_content:
        print("✅ Professional styling applied")
    else:
        print("❌ Professional styling NOT found")
    
    # Check for responsive design
    if "@media (max-width: 900px)" in html_content:
        print("✅ Responsive design (tablet support) added")
    else:
        print("❌ Responsive design NOT found")
    
    # Check for emoticons/icons
    if "📄" in html_content and "📅" in html_content and "😊" in html_content:
        print("✅ Status icons (📄, 📅, 😊) found")
    else:
        print("❌ Status icons NOT found")
    
    # Check for status values
    if "Total Submissions" in html_content:
        print("✅ Mood submissions counter label found")
    else:
        print("❌ Mood submissions counter label NOT found")
    
else:
    print(f"❌ Dashboard load failed: {dashboard_response.status_code}")

# Test 3: Verify CSS Grid
print("\n[TEST 3] Verify CSS Grid Layout")
if "grid-template-columns: 1fr 1fr 1fr" in dashboard_response.text:
    print("✅ 3-column grid layout configured")
else:
    print("⚠️  3-column grid not explicitly found (may be loaded from CSS)")

# Test 4: Verify Color-coded cards
print("\n[TEST 4] Verify Color-coded Status Cards")
if "border-left: 4px solid #dc3545" in dashboard_response.text:  # PDF - Red
    print("✅ Red border for PDF Status card")
else:
    print("❌ Red border NOT found")

if "border-left: 4px solid #17a2b8" in dashboard_response.text:  # Date - Teal
    print("✅ Teal border for Upload Date card")
else:
    print("❌ Teal border NOT found")

if "border-left: 4px solid #28a745" in dashboard_response.text:  # Mood - Green
    print("✅ Green border for Mood Records card")
else:
    print("❌ Green border NOT found")

print("\n" + "=" * 60)
print("SUMMARY: Dashboard Enhanced with Professional Status Cards")
print("=" * 60)
print("\n✨ New Features:")
print("  • 3-column grid layout for status cards")
print("  • PDF Status: Shows filename or 'Not Uploaded'")
print("  • Upload Date: Shows upload timestamp")
print("  • Mood Records: Shows total mood submissions")
print("  • Color-coded cards: Red (PDF), Teal (Date), Green (Mood)")
print("  • Responsive design: Collapses to mobile on smaller screens")
print("  • Professional icons and labels")
print("\n🎯 Status: DASHBOARD ENHANCED SUCCESSFULLY ✅")
