from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return f"Your IP address is: {ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
