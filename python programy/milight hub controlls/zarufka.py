import requests
import json
import os

k = 0
copy_to = 0
copy_from = 0

url = "http://192.168.1.50/"

def show_current_devices():
    k = 0
    for device in devices_key_list:
            print("[" + str(k) + "]" + device)
            k += 1

def get_user_input():
    while True:
        os.system("cls")
        show_current_devices()
        print("Copy from:")
        global copy_from
        try:
            copy_from = int(input())
        except:
            print("Podaj właściwy numer z listy")
            os.system("pause")
            continue
        if copy_from + 1 > len(devices_key_list) or copy_from < 0:
            print("Wybierz liczbę z właściwego zakresu")
            os.system("pause")
            continue
        print("Copy to:")
        global copy_to
        try:
            copy_to = int(input())
        except:
            print("Podaj właściwy numer z listy")
            os.system("pause")
            continue
        if copy_to + 1 > len(devices_key_list) or copy_to < 0:
            print("Wybierz liczbę z właściwego zakresu")
            os.system("pause")
            continue
        if copy_from == copy_to:
            print("Wybierz różne urządzenia")
            os.system("pause")
            continue
        if copy_from != copy_to:
            break

r = requests.get(url + "settings").text

gayson = json.loads(r)

devices_dict = gayson["group_id_aliases"]

devices_key_list = list(devices_dict.keys())

devices_values_list = list(devices_dict.values())

get_user_input()

devices_settings = {}
z = 0
for device in devices_key_list:
    smaller_list = list(devices_values_list[z])
    settings = requests.get(url + "gateways/" + str(smaller_list[1]) + "/" + str(smaller_list[0]) + "/" + str(smaller_list[2])).text
    greg = json.loads(settings)
    devices_settings[devices_key_list[z]] = greg
    z =+ 1

copy_from_setting = devices_settings.setdefault(devices_key_list[int(copy_from)])

headerInfo = {'Content-type': 'application/json'}
payload = copy_from_setting
jLoad = json.dumps(payload)
send_list = list(devices_values_list[copy_to])
response = requests.post(url + "gateways/" + str(send_list[1]) + "/" + str(send_list[0]) + "/" + str(send_list[2]), headers=headerInfo, data=jLoad)

os.system("cls")
print(response.text)
os.system("pause")
