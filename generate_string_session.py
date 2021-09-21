from pyrogram import Client

API_KEY = int(input("8600325"))
API_HASH = input("1f8c1ff9f8a8b1b07b43900d21ae4eac")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
