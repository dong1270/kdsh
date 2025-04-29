import json

def installer():
    filePath = "/Users/kangdongseong/myLib/kdsh/repository.json"
    json_data = open(filePath, 'r')

    data = json.load(json_data)

    json_data.close()

    print(data['site'])