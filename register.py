import json
import os
from record import record_voice

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")  # ✅ normal input

    file_path = "users.json"

    # Load users safely
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                users = json.load(f)
        except:
            users = {}
    else:
        users = {}

    if username in users:
        print("❌ User already exists")
        return

    # Record voice
    voice_file = f"{username}.wav"
    record_voice(voice_file)

    # Save user
    users[username] = {
        "password": password,
        "voice": voice_file
    }

    with open(file_path, "w") as f:
        json.dump(users, f, indent=4)

    print("✅ User registered successfully!")