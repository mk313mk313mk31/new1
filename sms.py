from sms3 import send, nonblocking_send

# result is a json server response. see docs for details
result = send('+989160855428', 'The server is down!')
print(result)