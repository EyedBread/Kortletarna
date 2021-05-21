import json
import requests
from config import WEBHOOK


product_url = "mall" # Product page
amount = 0
webhook_url = WEBHOOK

def notification_slack(product_url, amount):
    # Create message
    message = str(amount) + " or more cards in stock: " + product_url
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