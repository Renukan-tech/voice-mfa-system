import sqlite3
from datetime import datetime
from comparison import compare_voices
from record import record_voice

def login_user():
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    # Connect database
    conn = sqlite3.connect("authentication.db")
    cursor = conn.cursor()

    # Check user
    cursor.execute(
        "SELECT password, voice_file FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    if not user:
        print("❌ User not found")
        conn.close()
        return

    stored_password = user[0]
    stored_voice = user[1]

    # Check password
    if password != stored_password:
        print("❌ Incorrect password")
        conn.close()
        return

    # Record test voice
    test_voice = "test_voice.wav"
    record_voice(test_voice)

    # Compare voices
    result = compare_voices(stored_voice, test_voice)

    if result:
        print("✅ Login successful!")

        # Save login log
        cursor.execute(
    "INSERT INTO logs (username, login_time, status) VALUES (?, datetime('now'), ?)",
    (username, "Success")
)

        conn.commit()

    else:
        print("❌ Voice does not match")

    conn.close()