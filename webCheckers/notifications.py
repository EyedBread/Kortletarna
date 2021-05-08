import json
import requests


product_url = "mall" # Product page
amount = 0

#OBS!! Needs webhook adress to work (which can't be posted on gitHub)
webhook_url = "insert_webhook_url_here" # Slack bot

def notification_slack(product_url, amount):
    # Create message
    message = str(amount) + " cards in stock: " + product_url
    slack_data = {'text': message}
    data = json.dumps(slack_data)

    # Post message
    response = requests.post(
        webhook_url, data,
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
    )

notification_slack(product_url, amount)