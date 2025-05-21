import time
import os
from instagrapi import Client
import openpyxl

# Save session to avoid logging in every time
SESSION_FILE = "session.json"

cl = Client()

# Load existing session if available
if os.path.exists(SESSION_FILE):
    cl.load_settings(SESSION_FILE)

try:
    cl.get_timeline_feed()  # Check if session is still valid
except:
    # Login again if needed
    username = "momscraftteam"
    password = "Home@0110"
    cl.login(username, password)
    cl.dump_settings(SESSION_FILE)  # Save session after login

# Load Excel file
wb = openpyxl.load_workbook("users.xlsx")
sheet = wb.active

# Loop through each user/message
for row in sheet.iter_rows(min_row=2, values_only=True):  # skip header
    user, message = row
    try:
        print(f"Looking up {user}...")
        user_id = cl.user_id_from_username(user)

        # Optional: check if user follows you (safer delivery)
        # friendship = cl.user_friendship(user_id)
        # if not friendship.following:
        #     print(f"⚠️ {user} is not following you. Skipping.")
        #     continue

        cl.direct_send(message, [user_id])
        print(f"✅ Message sent to {user}")

        # Delay to avoid spam detection
        time.sleep(5)

    except Exception as e:
        print(f"❌ Failed to message {user}: {e}")
