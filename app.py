from flask import Flask
app = Flask(__name__)
app_version = "1.1"

@app.route('/')
def home():
    return f"Hello from the CI/CD pipeline! App version is {app_version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
