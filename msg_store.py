import uuid
import csv
import os
from datetime import datetime

MESSAGES_CSV = "messages.csv"
MESSAGES_FIELDS = ["message_id", "user_id", "username", "content", "timestamp"]


def init_messages_csv():
    if not os.path.exists(MESSAGES_CSV):
        with open(MESSAGES_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=MESSAGES_FIELDS)
            writer.writeheader()


def save_message(user_id: str, username: str, content: str) -> dict:
    """Save a chat message to messages.csv and return the saved record."""
    init_messages_csv()
    message = {
        "message_id": str(uuid.uuid4()),
        "user_id": user_id,
        "username": username,
        "content": content.strip(),
        "timestamp": datetime.now().isoformat(),
    }
    with open(MESSAGES_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=MESSAGES_FIELDS)
        writer.writerow(message)
    return message


def load_messages(limit: int = 100) -> list[dict]:
    """Load the most recent `limit` messages from messages.csv."""
    init_messages_csv()
    with open(MESSAGES_CSV, "r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows[-limit:]


def load_messages_by_user(user_id: str) -> list[dict]:
    """Return all messages sent by a specific user_id."""
    init_messages_csv()
    with open(MESSAGES_CSV, "r", newline="", encoding="utf-8") as f:
        return [row for row in csv.DictReader(f) if row["user_id"] == user_id]