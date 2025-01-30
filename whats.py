from twilio.rest import Client
import time

def send_whatsapp_notification():
    # Twilio credentials
    account_sid = '' #Your account sid
    auth_token = '' #Your auth token

    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # Message content with properly formatted link
        message_body = """Your delivery has been scheduled between 10-11am. 
If you'd like to change the time, click here:
https://notificationoptideliver.vercel.app"""  # Link on separate line for better clickability

        # Format numbers properly for WhatsApp
        recipient_number = '' #Your recipient number
        sender_number = '' #Your twilio number

        # Send message with error handling
        message = client.messages.create(
            from_=sender_number,
            body=message_body,
            to=recipient_number
        )

        print(f"Message sent! SID: {message.sid}")

        # Monitor delivery status
        attempts = 0
        while attempts < 10:
            current_status = client.messages(message.sid).fetch().status
            print(f"Message status: {current_status}")

            if current_status == 'delivered':
                print("✓ Message delivered successfully!")
                return True
            elif current_status in ['failed', 'undelivered']:
                print(f"✗ Delivery failed. Status: {current_status}")
                return False

            attempts += 1
            time.sleep(2)

    except Exception as e:
        print(f"Error sending message: {str(e)}")
        print("\nTroubleshooting Guide:")
        print("1. Send 'join plenty-drawn' to +14155238886")
        print("2. Wait for sandbox confirmation")
        print("3. Check your WhatsApp number")
        return False

if __name__ == "__main__":
    print("Sending WhatsApp notification...")
    send_whatsapp_notification()