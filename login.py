import datetime
import json
import os
import random
from record import record_voice
from comparison import compare_audio

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")  # ✅ normal input

    file_path = "users.json"

    if not os.path.exists(file_path):
        print("❌ No users found")
        return

    with open(file_path, "r") as f:
        users = json.load(f)

    if username not in users:
        print("❌ User not found")
        return

    if users[username]["password"] != password:
        print("❌ Incorrect password")
        return

    print("🔐 Password verified")

    file1 = os.path.join("voices", users[username]["voice"])

    # 🔁 Voice attempts
    attempts = 0
    success = False

    while attempts < 3:
        print(f"\n🎤 Voice Attempt {attempts + 1}/3")
        temp_file = "temp.wav"
        record_voice(temp_file)

        file2 = os.path.join("voices", temp_file)
        score = compare_audio(file1, file2)

        print(f"Distance Score: {score:.2f}")

        if score < 30:
            print("✅ Voice Match - Access Granted")
            success = True
            break
        else:
            print("❌ Voice not matched")
            attempts += 1

    # 🔢 OTP fallback
    if not success:
        print("\n⚠️ Voice verification failed 3 times")
        print("🔢 OTP verification required")

        otp = random.randint(100000, 999999)
        print(f"Your OTP is: {otp}")  # demo

        user_otp = input("Enter OTP: ")

        if str(otp) == user_otp:
            print("✅ OTP Verified - Access Granted")
            success = True
        else:
            print("❌ OTP Incorrect - Access Denied")
            success = False

    # 📜 Logging
    log_entry = {
        "username": username,
        "time": str(datetime.datetime.now()),
        "status": "Success" if success else "Failed"
    }

    log_file = "logs.json"

    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    else:
        logs = []

    logs.append(log_entry)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)