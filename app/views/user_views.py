from app import app

@app.route('/')
def welcome():
    return "Welcome to Karibu!"