from flask import Flask, redirect, url_for
# from application import app
from application.controllers.user_controller import user_bp
import os


app = Flask(__name__)
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'application', 'views')
app.register_blueprint(user_bp)

@app.route('/')
def base():
    return redirect(url_for('user.read'))
  
if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')