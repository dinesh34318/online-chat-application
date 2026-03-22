import uuid
import csv
import os
from datetime import datetime

USERS_CSV = "users.csv"
USERS_FIELDS = ["user_id", "username", "created_at"]


def init_users_csv():
    if not os.path.exists(USERS_CSV):
        with open(USERS_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=USERS_FIELDS)
            writer.writeheader()


def create_user(username: str) -> dict:
    """Create a new user with a unique UUID and store in users.csv."""
    init_users_csv()
    user_id = str(uuid.uuid4())
    user = {
        "user_id": user_id,
        "username": username.strip(),
        "created_at": datetime.now().isoformat(),
    }
    with open(USERS_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=USERS_FIELDS)
        writer.writerow(user)
    return user


def get_user_by_id(user_id: str) -> dict | None:
    init_users_csv()
    with open(USERS_CSV, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["user_id"] == user_id:
                return row
    return None


def get_all_users() -> list[dict]:
    init_users_csv()
    with open(USERS_CSV, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))