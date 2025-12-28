from flask import Flask, request, jsonify

from api.routes.auth_routes import auth_bp

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)