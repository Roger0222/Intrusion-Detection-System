from twilio.rest import Client
account_sid = 'AC0a9e572fd75b2afa716d207774f5573d'
auth_token = '67ac279cfdb9c054af2d5069ed39c7fa'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
        from_='+19842764295',
        body='ALERT!!!',
        to='+639632618615'
    )
    print("SMS sent successfully:", message.sid)