from main import app

@app.route('/test')
def home():
    return 'test'