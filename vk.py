#!/usr/bin/env python3

import requests, time

ACCESS_TOKEN_LIST = [
    # ТОКЕНЫ ПОЛУЧЕННЫЕ ПО ССЫЛКЕ НА САЙТЕ S2E0058.RU, ИЛИ ЧЕРЕЗ СВОЁ ПРИЛОЖЕНИЕ
    # ПОЛЬЗОВАТЕЛЬСКИЕ ТОКЕНЫ АКТИВНЫ ТОЛЬКО В ТЕЧЕНИИ СУТОК
    'b7dce387418a389cd55b3c7e74e5d6df8522ae72813c5032ad113aff8f5f890fa652472a94056ac981687',
]

if ACCESS_TOKEN_LIST:
    while True:
        try:
            for ACCESS_TOKEN in ACCESS_TOKEN_LIST:
                URL = 'https://api.vk.com/method/account.setOnline?voip=0&access_token=' + ACCESS_TOKEN + '&v=5.101'
                REQUEST = requests.request('GET', URL)
                RSP = REQUEST.json()
                try:
                    if RSP['response'] == 1:
                        print('TOKEN:' + ACCESS_TOKEN, time.strftime('%H:%M:%S'), 'OK')
                except KeyError:
                    print('TOKEN:' + ACCESS_TOKEN + ' просрочен')
                    ACCESS_TOKEN_LIST.remove(ACCESS_TOKEN)
            time.sleep(300)
        except KeyboardInterrupt:
            print(' ЗАВЕРШЕНИЕ РАБОТЫ СКРИПТА')
            break
else:
    print('ACCESS TOKEN LIST ПУСТ')
