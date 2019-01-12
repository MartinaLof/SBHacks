# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC25792ec11c9aecc8f7ad246ed613d0cd'
auth_token = 'ec50ca2e8cd825a862fac6c132b7bae3'
client = Client(account_sid, auth_token)

key = client.keys('SKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX').fetch()

print(key.friendly_name)