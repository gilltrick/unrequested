from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)

@socketio.on("connect")
def WebSocketConnect():
    try:
        file = open("text.txt", "r")
        data = file.read()
        file.close()
        temp = {"counter":int(json.loads(data).get("counter")) + 1}
        emit("user", temp, broadcast=True)
        file = open("text.txt", "w")
        file.write(json.dumps(temp))
        file.close()
    except:
        file = open("text.txt", "w")
        file.write(json.dumps({"counter":0}))
        file.close()
        emit("user", {"counter":0}, broadcast=True)

@socketio.on("disconnect")
def WebSocketDisconnect():
    file = open("text.txt", "r")
    data = file.read()
    file.close()
    temp = {"counter":int(json.loads(data).get("counter")) - 1}
    
    file = open("text.txt", "w")
    file.write(json.dumps(temp))
    file.close()
    emit("user", temp, broadcast=True)

@app.route("/", methods=["get"])
def Home():
    file = open("text.txt", "r")
    data = file.read()
    data = {"counter": int(json.loads(data).get("counter"))}
    return render_template("index.html", data=data)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5575)