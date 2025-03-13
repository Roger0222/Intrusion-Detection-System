import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Twilio credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

def sendSms():
    message = client.messages.create(
        from_='+19842764295',
        body='ALERT!!!',
        to='+my num'
    )
    print("SMS sent successfully:", message.sid)

# Call the function to send SMS
sendSms()