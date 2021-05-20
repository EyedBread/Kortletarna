import json
import requests


product_url = "mall" # Product page
amount = 0

#OBS!! Needs webhook adress to work (which can't be posted on gitHub)
webhook_base = "https://hooks.slack.com/services/" # Slack bot
webhook_identifier = "T020Y6B76FQ/B021B7N4AR1/0qr6MpkHIBHfXNVVHDo4MnWh"
webhook_url = webhook_base + webhook_identifier

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