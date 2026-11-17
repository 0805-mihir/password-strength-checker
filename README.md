# password-strength-checker
Python Password Strength Checker Cyber Security Project
Project Overview

The Password Strength Checker is a Python-based cybersecurity project that evaluates the strength of a password. It checks different password conditions, estimates password entropy, identifies common weak passwords, and provides suggestions to improve password security.

🎯 Project Objectives

To understand basic password security concepts.

To check password length and character combinations.

To calculate estimated password entropy.

To identify common weak passwords.

To classify passwords based on their strength.

To provide suggestions for creating stronger passwords.

✨ Features

Checks password length.

Detects uppercase and lowercase letters.

Detects numbers and special characters.

Calculates estimated password entropy in bits.

Checks against a small list of common weak passwords.

Assigns a security score out of 6.

Classifies passwords as Weak, Moderate, Strong, or Exceptional.

Provides suggestions to improve password security.

🛠️ Technologies Used

Python

Math Module

Command Prompt (CMD)

GitHub

How to Run the Project

Step 1: Install Python on your computer.

Step 2: Download or clone this repository.

git clone https://github.com/0805-mihir/password-strength-checker.git

Step 3: Open the project folder.

cd password-strength-checker

Step 4: Run the Python program.

python password_checker.py

Step 5: Enter a password when prompted and view the security report.

📊 Sample Output

Enter your password: Mihir@12345

----- PASSWORD SECURITY REPORT -----
Password Length: 11
Uppercase: True
Lowercase: True
Digits: True
Special Characters: True
Entropy: 72.1 bits
Security Score: 5 / 6
Password Strength: Strong

Suggestions:
- Use at least 12 characters.
------------------------------------

Note: The entropy value is an estimate and may vary depending on the password.

📸 Project Screenshots

The repository includes command-line screenshots demonstrating four password strength levels:

Weak Password

Moderate Password

Strong Password

Exceptional Password

⚠️ Limitations

Uses a small local list of common weak passwords.

Does not check real leaked-password databases.

Entropy is an estimate based on the character pool.

It is a command-line-based application.

🚀 Future Enhancements

Integrate a larger common-password database.

Add a graphical user interface (GUI).

Improve password security analysis.

Add secure password generation.

👨‍💻 Developer

Mihir Koshti

Cyber Security Internship Project – Workora

📄 Conclusion

This project demonstrates basic password security checking using Python. It helps users understand password strength, entropy, and the importance of creating strong passwords.

🔗 GitHub Repository

https://github.com/0805-mihir/password-strength-checker
