from flask import Flask
import os
from datetime import datetime
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        full_name = "Chinmay Kothari"  
        username = os.environ.get('USER') or os.environ.get('USERNAME')  
        server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') 
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_used = memory_info.used / (1024 ** 2)  
        memory_total = memory_info.total / (1024 ** 2) 
        memory_available = memory_info.available / (1024 ** 2) 
        response = f"""
        <h1>Name: {full_name}</h1>
        <h2>Username: {username}</h2>
        <h3>Server Time (IST): {server_time}</h3>
        <h3>CPU Usage: {cpu_usage}%</h3>
        <h3>Memory Used: {memory_used:.2f} MB</h3>
        <h3>Memory Total: {memory_total:.2f} MB</h3>
        <h3>Memory Available: {memory_available:.2f} MB</h3>
        """
        return response
    except Exception as e:
        return f"<h1>Error:</h1><p>{str(e)}</p>", 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
