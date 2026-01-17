from flask import Flask, request
import requests
import os

app = Flask(__name__)

def trigger_github():
    # URL check kar lein: maliknabeel22347 / TIKTOK-AUTOMATION
    url = "https://api.github.com/repos/maliknabeel22347/TIKTOK-AUTOMATION/dispatches"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}"
    }
    data = {"event_type": "youtube_upload"}
    r = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {r.status_code}")

@app.route('/webhook', methods=['GET'])
def verify():
    challenge = request.args.get('hub.challenge', "No challenge")
    return challenge, 200

@app.route('/webhook', methods=['POST'])
def callback():
    print("New Video Notification Received!")
    trigger_github()
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
