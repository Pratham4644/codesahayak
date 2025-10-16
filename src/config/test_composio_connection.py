"""
Test Composio connection
"""
from composio import ComposioToolSet, App
from dotenv import load_dotenv
import os

load_dotenv()

print("🔍 Testing Composio Connection...\n")

# Initialize Composio
api_key = os.getenv("COMPOSIO_API_KEY")
print(f"API Key: {api_key[:10]}...\n")

try:
    toolset = ComposioToolSet(api_key=api_key)
    print("✅ Composio connected successfully!")
    
    # Get available apps
    print("\n📦 Some available integrations:")
    apps = [
        "GITHUB",
        "NOTION", 
        "GOOGLECALENDAR",
        "GMAIL",
        "SLACK"
    ]
    
    for app in apps:
        print(f"  ✓ {app}")
    
    print("\n🎉 Ready to build agents!")
    
except Exception as e:
    print(f"❌ Error: {e}")