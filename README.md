 
# OLX Project Security Features

This document provides an overview of the security features implemented in our Django project.

## Features

### 1. User Authentication
- Implemented Django's built-in authentication system for managing user accounts.
- Users can sign up, log in, and log out securely.
- Passwords are hashed and securely stored.

### 2. Message Encryption
- All user messages are encrypted in the database.
- Used the `cryptography` library to encrypt and decrypt messages.
- Encryption keys are securely managed via environment variables.

### 3. CSRF Protection
- Enabled Django's built-in CSRF protection for all forms.
- Ensures that POST requests are only accepted from authenticated sessions.

### 4. Secure Form Handling
- Used Django forms to securely handle user input.
- Server-side validation of all form data to prevent injection attacks.

### 5. Error Handling
- Implemented global and view-level exception handling.
- Ensures graceful handling of errors and prevents sensitive information leakage.

## 6. Google Captcha 
- Implemented google capthca when logging in to avoid spam and bots.

## How We Made It Secure

- **User Authentication:** Leveraged Django's authentication framework to ensure secure handling of user credentials and sessions.
- **Message Encryption:** Implemented Fernet symmetric encryption to encrypt messages stored in the database, enhancing data privacy.
- **CSRF Protection:** Used Django's CSRF tokens in forms to protect against Cross-Site Request Forgery attacks.
- **Secure Form Handling:** Django forms are used to validate and sanitize user input, guarding against SQL injection and other forms of attacks.
- **Error Handling:** Custom middleware and view-level try-except blocks are used to handle exceptions without exposing sensitive information.

## Additional Notes

- Regular updates to Django and its dependencies are essential to maintain security.
- Environment variables are used to manage sensitive information like database credentials and encryption keys.

---

 