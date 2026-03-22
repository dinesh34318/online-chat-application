import bcrypt
import re
from database import get_users_collection

def validate_phone(phone):
    v = phone.strip()
    if not v:
        return False, "Phone Number is required."
    if not re.match(r"^\+?[0-9]{10,15}$", v):
        return False, "Enter a valid phone number (10-15 digits)."
    return True, ""

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[^A-Za-z0-9]", password):
        return False, "Password must contain at least one special character (@, #, $ ...)."
    return True, ""

def validate_name(name, field):
    if not name.strip():
        return False, f"{field} is required."
    if len(name.strip()) < 2:
        return False, f"{field} must be at least 2 characters."
    if not re.match(r"^[A-Za-z\s'-]+$", name.strip()):
        return False, f"{field} can only contain letters, spaces, hyphens, apostrophes."
    return True, ""

def signup_user(first_name, last_name, phone, password, confirm_password, role="user"):
    errors = []
    ok, msg = validate_name(first_name, "First Name")
    if not ok: errors.append(msg)
    ok, msg = validate_name(last_name, "Last Name")
    if not ok: errors.append(msg)
    ok, msg = validate_phone(phone)
    if not ok: errors.append(msg)
    ok, msg = validate_password(password)
    if not ok: errors.append(msg)
    if password != confirm_password:
        errors.append("Passwords do not match.")
    if role not in ("admin", "user"):
        errors.append("Invalid role.")
    if errors:
        return False, "\n".join(errors)

    users = get_users_collection()
    if users.find_one({"phone": phone.strip()}):
        return False, "An account with this phone number already exists."

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users.insert_one({
        "first_name":    first_name.strip(),
        "last_name":     last_name.strip(),
        "phone":         phone.strip(),
        "password_hash": hashed,
        "role":          role,
    })
    return True, "Signup successful!"

def login_user(phone, password):
    if not phone.strip():
        return False, "Phone Number is required.", None
    if not password:
        return False, "Password is required.", None

    users = get_users_collection()
    user = users.find_one({"phone": phone.strip()})
    if not user:
        return False, "No account found with that phone number.", None
    if not bcrypt.checkpw(password.encode(), user["password_hash"]):
        return False, "Incorrect password.", None

    return True, "Login successful!", {
        "first_name": user["first_name"],
        "last_name":  user["last_name"],
        "role":       user["role"],
    }
