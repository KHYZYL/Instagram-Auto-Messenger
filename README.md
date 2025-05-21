# 📩 Instagram Auto Messenger

This tool allows you to automatically send messages to multiple Instagram users, based on details provided in an Excel sheet.

---

## ✅ Features

- Send personalized messages to multiple users  
- Easy-to-use with an Excel sheet  
- One-click execution via Python

---

## ⚙️ How to Use

### 📝 1. Prepare Your Excel File

- Create an Excel file (`.xlsx` format).
- In **Column A**, enter Instagram usernames.  
- In **Column B**, enter the message you want to send to each user.

**Example:**

| Username    | Message                   |
|-------------|---------------------------|
| john_doe    | Hey John! How are you?    |
| jane_smith  | Hello Jane, check this!   |

---

### 🔐 2. Add Your Credentials

- Open the `main.py` file.  
- Find the section where you can enter your Instagram username and password.

```python
username = "your_instagram_username"
password = "your_instagram_password"

##▶️ 3. Run the App
Make sure all required Python packages are installed.

Run the script by executing the following command in your terminal or IDE:

bash
Copy
Edit
python main.py
The script will log in to your Instagram account and start sending the messages listed in your Excel file.

##📌 Notes
Avoid spamming users, as Instagram may temporarily block your messaging.

Keep your login credentials safe.
Do not share your script with your username/password filled in.

Use at your own risk. This script is not affiliated with Instagram.

##📧 Contact
For help or feedback, feel free to reach out!