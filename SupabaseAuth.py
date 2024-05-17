from supabase import create_client
from flask import Flask, request

app = Flask(__name__)
# supabase 2.4.0

url = 'http://localhost:8000'
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q"
#key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJhbm9uIiwKICAgICJpc3MiOiAic3VwYWJhc2UtZGVtbyIsCiAgICAiaWF0IjogMTY0MTc2OTIwMCwKICAgICJleHAiOiAxNzk5NTM1NjAwCn0.dc_X5iR_VP_qT0zsiyj_I_OZ2T9FtRU2BBNWN8Bu4GE'

supabase = create_client(url, key)


@app.route('/get_login', methods=['GET'])
def login_rqst():
    if request.method == 'GET':
        global password_sign
        global email_sign
        args = request.args
        password_sign = args.get("password")
        email_sign = args.get("email")
        try:
            login()
            user = supabase.auth.get_user()
            user_id = user.dict().get("user").get("id")
            return user_id
        except Exception as e:
            return f"Error {e}"


@app.route('/get_reg', methods=['GET'])
def register_rqst():
    if request.method == 'GET':
        global password_create
        global email_create
        args = request.args
        password_create = args.get("password")
        email_create = args.get("email")
        try:
            register()
            #user = supabase.auth.get_user()
            #user_id = user.dict().get("user").get("id")
            #return user_id
            return "login"
        except Exception as e:
            return f"Error {e}"


@app.route('/get_unl', methods=['GET'])
def logout_rqst():
    if request.method == 'GET':
        try:
            user = supabase.auth.get_user()
            user_id = user.dict().get("user").get("id")
            return f"Saiu {user_id}"
            logout()
        except Exception as e:
            return f"Error {e}"


def login():
    sin = supabase.auth.sign_in_with_password({
        "email": email_sign,
        "password": password_sign
    })


def logout():
    res = supabase.auth.sign_out()


def register():
    cas = supabase.auth.admin.create_user({
        "email": email_create,
        "password": password_create,
    })
    gnr = supabase.auth.verify_otp({
        "type": "signup",
        "token_hash": "HASH123456",
        "email": email_create,
    })