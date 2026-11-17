
import math

# Step 1: Common weak passwords
common_passwords = ["123456", "password", "admin",
                    "qwerty", "12345678", "abc123"]

# Step 2: Take password from user
password = input("Enter your password: ")

# Step 3: Check password conditions
length = len(password)
has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(not ch.isalnum() for ch in password)

# Step 4: Calculate character pool
pool = 0

if has_lower:
    pool += 26

if has_upper:
    pool += 26

if has_digit:
    pool += 10

if has_special:
    pool += 32

# Step 5: Calculate entropy
if pool > 0:
    entropy = length * math.log2(pool)
else:
    entropy = 0

# Step 6: Check password strength
score = 0

if length >= 8:
    score += 1

if length >= 12:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

if password.lower() in common_passwords:
    strength = "Weak"

elif score <= 2 or length < 8:
    strength = "Weak"

elif score <= 4:
    strength = "Moderate"

elif score == 5:
    strength = "Strong"

else:
    strength = "Exceptional"

# Step 7: Display result
print("\n----- PASSWORD SECURITY REPORT -----")

print("Password Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Digits:", has_digit)
print("Special Characters:", has_special)

print("Entropy:", round(entropy, 2), "bits")
print("Security Score:", score, "/ 6")
print("Password Strength:", strength)

# Step 8: Give suggestions
print("\nSuggestions:")

if length < 12:
    print("- Use at least 12 characters.")

if not has_upper:
    print("- Add uppercase letters.")

if not has_lower:
    print("- Add lowercase letters.")

if not has_digit:
    print("- Add numbers.")

if not has_special:
    print("- Add special characters.")

if password.lower() in common_passwords:
    print("- Avoid common passwords.")

if score == 6 and password.lower() not in common_passwords:
    print("- Good! All basic checks are passed.")

print("------------------------------------")
