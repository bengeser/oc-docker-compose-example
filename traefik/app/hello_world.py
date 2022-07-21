from concurrent.futures import thread
from flask import Flask
import time
import threading
app = Flask(__name__) # Flask instance named app

@app.route("/")
@app.errorhandler(404)
def hello(*arg, **kwarg):
    name = threading.current_thread().getName()
    print(f"current thread: {name}")
    time.sleep(3)
    return "Hallo von Flask"


if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8000, threaded=False)