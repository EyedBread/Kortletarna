MSG_SEND_SLACK = True
MSG_POPUP_GUI = True
WEBHOOK = "Insert_webhook_here"
# Remove all code below this point before running


#OBS!! This is a developer webhook, should be removed for personal use.
webhook_base = "https://hooks.slack.com/services/" # Slack bot
webhook_identifier = "T020Y6B76FQ/B021B7N4AR1/0qr6MpkHIBHfXNVVHDo4MnWh"
webhook_url = webhook_base + webhook_identifier
WEBHOOK = webhook_url
