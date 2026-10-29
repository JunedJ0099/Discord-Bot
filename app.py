from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your actual Discord Webhook URL
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1565078321132212354/Ke7TRuPAOpV_9yVQeSTVZl9IoDGBAxnYG2g8OOsyMoUIVDd1zekFw7xSe6OrU65KoZ5S/github'

@app.route('/webhook', methods=['POST'])
def github_webhook():
    payload = request.json
    
    # Check if the payload is a Pull Request event
    if 'pull_request' in payload:
        action = payload['action']
        title = payload['pull_request']['title']
        url = payload['pull_request']['html_url']
        message = f"Pull Request {action}: {title}\n{url}"
    else:
        message = "Received a new GitHub event."

    # Send the message to Discord
    response = requests.post(DISCORD_WEBHOOK_URL, json={'content': message})

    if response.status_code == 204:
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'failed'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)