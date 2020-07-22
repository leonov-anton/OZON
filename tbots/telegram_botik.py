import requests
import json

token = "1329196465:AAEulFiMHlk4msfrQ6LdnkckpbedJPBTQRs"  # нужно ввести токен

url = str('https://api.telegram.org/bot' + token + '/')


def polling():
    while True:
        try:
            off_set = req['result'][0]['update_id']
            off_set += 1
            msg = {'offset': off_set, 'timeout': 60, 'limit': 1}
            req_update = requests.post(str(url + 'getUpdates'), data=msg)
            req = req_update.json()
            msg = {'chat_id': req['result'][0]['message']['from']['id'],
                   'text': 'Я ничего не умею, отстань'}
            send_msg = requests.post(str(url + 'sendMessage'), data=msg)
        except IndexError and UnboundLocalError:
            msg = {'timeout': 60, 'limit': 1}
            req_update = requests.post(str(url + 'getUpdates'), data=msg)
            req = req_update.json()
            msg = {'chat_id': req['result'][0]['message']['from']['id'],
                   'text': 'Привет!'}
            send_msg = requests.post(str(url + 'sendMessage'), data=msg)
        print(req)


polling()