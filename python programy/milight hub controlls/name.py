#copy rgb profile and set it on all devices

import requests
import json

url = requests.get("http://192.168.2.198/settings").text

#devices_file = open("devices.txt", "w+")

#devices_file.close

list = []
name_list = []
id_list = []
group_list = []
remote_list = []
settings_list = []

devices_place = url.find("group_id_aliases")
devices_str = url[devices_place +19 :-2]

split_point = "],"
name_split_point = '":'

def input_device_id():
    while True:
        try:
            user_input_from = int(input("nr urządzenia do skopiowania"))
            user_input_to = int(input("nr urządzenia do którego będziemy kopiować"))
            break
        except:
            print("podaj prawidłowy nr urządzenia")

while True:
    index = devices_str.find(split_point)
    if index == -1:
        list.append(devices_str)
        break
    list.append(devices_str[ : index + 1])
    devices_str = devices_str[index + 2 : ]

for device in list:
    r = device.find(name_split_point)
    device_name = device[1: r]
    name_list.append(device_name)
    d = device.find('["')
    c = device.find('",')
    device_remote = device[d + 2: c]
    remote_list.append(device_remote)
    f = device[c+2:]
    g = f.find(",")
    device_id = f[ :g]
    id_list.append(device_id)
    device_group = f[g+1:-1]
    group_list.append(device_group)
    device_settings = requests.get("http://192.168.2.198/gateways/" + device_id + "/" + device_remote + "/" + device_group).text
    settings_list.append(device_settings)

user_input = 0
user_input_to = 0
user_input_from = 0

input_device_id()

headerInfo = {'Content-type': 'application/json'}
payload = {"brightness":2}
#payload = settings_list[user_input_from]
jLoad = json.dumps(payload)
response = requests.post("http://192.168.2.198/gateways/" + id_list[user_input_to] + "/" + remote_list[user_input_to] + "/" + group_list[user_input_to], headers=headerInfo, data=jLoad)


print(response.text)
print(list)
print(name_list)
print(id_list)
print(group_list)
print(remote_list)
print(settings_list)