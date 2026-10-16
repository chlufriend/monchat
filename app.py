from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)


app.config["SECRET_KEY"] = "classroom-demo-secret"


socketio = SocketIO(app)

@app.router("/")
def home():
  return render_template("index.html")


@socketio.on("chat_message")
def handle_message(data):
  {
    name: "  Jeremy  ",
    message: "Bonjour!"
  }

name = str(data.get("name","Student"))[:20].strip()

message = str(data.get("message",""))[:500].strip()

if not message:
  return

emit(

  "chat_message",
  {
    "name": name or "Student",
    "message": message
  },
  broadcast=True
)

if __name__ == "__main__":
  socketio.run(
    app,
    host="0.0.0.0",
    port=5000,
    debug=False
  )


