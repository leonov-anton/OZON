import requests
import json

token = "-"  # нужно ввести токен

url = str('https://api.telegram.org/bot' + token + '/')


def main():
    while True:
        try:
            off_set = req['result'][0]['update_id']
            off_set += 1
            msg = {'offset': off_set, 'timeout': 60, 'limit': 1}
            req_update = requests.post(str(url + 'getUpdates'), data=msg)
            req = req_update.json()
            answer(req)
        except IndexError and UnboundLocalError:
            msg = {'timeout': 60, 'limit': 1}
            req_update = requests.post(str(url + 'getUpdates'), data=msg)
            req = req_update.json()
            answer(req)


def set_list_creating(set_name):
    msg = {'name': set_name}
    req_sticker = requests.post(str(url + 'getStickerSet'), data=msg).json()
    sticker_list = []
    for sticker in req_sticker['result']['stickers']:
        sticker_list.append(sticker['file_id'])
    file = open(f'sets_lists/{set_name}.json', 'w')
    json.dump(sticker_list, file, indent=1)
    file.close()


def answer(req):
    try:
        set_name = req['result'][0]['message']['sticker']['set_name']
        set_list_creating(set_name)
        msg = {'chat_id': req['result'][0]['message']['from']['id'],
                'text': 'Ваш список стикеров готов'}
        send_msg = requests.post(str(url + 'sendMessage'), data=msg)
    except:
        msg = {'chat_id': req['result'][0]['message']['from']['id'],
                'text': 'Я принимаю только стикеры'}
        send_msg = requests.post(str(url + 'sendMessage'), data=msg)


main()

