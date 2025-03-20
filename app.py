from flask import Flask
import os
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop_endpoint():
    # Fetch system information
    name = "G.UDAY KRISHNA"  
    username = os.getenv("USER", "codespace")
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput("top -b -n 1")

    # Prepare response HTML
    response = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>TOP Output:\n{top_output}</pre>
    """
    return response

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)