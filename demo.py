import requests
import json

params = {'message': '你是？'}
botIp = '192.168.204.120'
botPort = '5005'
# rasa使用rest channel
# https://rasa.com/docs/rasa/user-guide/connectors/your-own-website/#rest-channels
# POST /webhooks/rest/webhook
rasaUrl = "http://{0}:{1}/webhooks/rest/webhook".format(botIp, botPort)
# rasaUrl = 'https://e8ec-218-94-115-131.ngrok-free.app/webhooks/rest/webhook'
reponse = requests.post(
    rasaUrl,
    data=json.dumps(params),
    headers={'Content-Type': 'application/json'}
)
result = json.loads(reponse.content)
print(result)
