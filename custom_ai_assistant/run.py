import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_message():
    data = request.get_json()
    message = data.get("message", "")
    print(f"Received from HA: {message}")

    try:
        resp = requests.post("http://192.168.178.75:5000/process", json={"message": message}, timeout=10)
        reply = resp.json().get("response", "Keine Antwort vom Server erhalten.")
    except Exception as e:
        reply = f"Fehler: {e}"

    print(f"Reply from Flask Server: {reply}")
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8124)
