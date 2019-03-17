from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC869b2241aa94d2e5353c321cfbcb6657"
# Your Auth Token from twilio.com/console
auth_token = "5937389911ef5d9a2673c9d42ba185ca"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+77773080547",
    from_="+12028049178",
    body="Hello, my name is Yerlan!")

print(message.sid)
