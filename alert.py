from twilio.rest import Client

account_sid = 'ACbb00a4601d77a1db52bb86a2dbcf5da8'
auth_token = '2293e9036a0a90724b5824335055bc01'
client = Client(account_sid, auth_token)
message = client.messages.create(
  messaging_service_sid='MG5888f47d5b9dbb014c3b5b41bfea365f',
  body='⚠️ ALERTE ⚠️ : ❌ Coupure de courant ⚡️',
  to='+33635796139'
)
print(message.sid)