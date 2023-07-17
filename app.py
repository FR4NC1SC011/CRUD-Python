from flask import Flask, Response, json
# from application import app
from application.controllers.user_controller import user_bp
import os


app = Flask(__name__)
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'application', 'views')
app.register_blueprint(user_bp)

@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')
  
if __name__ == '__main__':
    app.run(debug=True, port=5001, host='127.0.0.1')