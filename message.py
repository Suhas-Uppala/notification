from twilio.rest import Client

# Twilio credentials
account_sid = ''  # Replace with your Twilio Account SID
auth_token = ''    # Replace with your Twilio Auth Token
client = Client(account_sid, auth_token)

# Message details
message_body = "Your delivery has been scheduled between 10-11am. If you'd like to change the time, click here: https://notificationoptideliver.vercel.app/"
sms_recipient = ''  # Replace with recipient's phone number
whatsapp_recipient = ''  # Replace with recipient's WhatsApp number
twilio_sms_sender = ''  # Replace with your Twilio SMS number
twilio_whatsapp_sender = ''  # Twilio's WhatsApp sandbox number

# Send SMS
sms_message = client.messages.create(
    body=message_body,
    from_=twilio_sms_sender,
    to=sms_recipient
)
print(f"SMS sent with SID: {sms_message.sid}")

# Send WhatsApp message
whatsapp_message = client.messages.create(
    body=message_body,
    from_=twilio_whatsapp_sender,
    to=whatsapp_recipient
)
print(f"WhatsApp message sent with SID: {whatsapp_message.sid}")
