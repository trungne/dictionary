import requests

r = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/go')
my_obj = r.json()
# print(my_obj)
num = 0
for i in my_obj[0]['phonetics']:
    print(f"{num}==============================")
    print(type(i))
    print(i)
    num += 1

# for item in my_obj[0].items():
#     print(item)hello