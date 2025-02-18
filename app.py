from flask import Flask
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = subprocess.run(['whoami'], capture_output=True, text=True).stdout.strip()
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S.%f')

    top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout

    response = (
        f"Name: Nitish K\n"
        f"Username: {username}\n"
        f"Server Time (IST): {ist_time}\n"
        f"TOP output:\n{top_output}"
    )

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)