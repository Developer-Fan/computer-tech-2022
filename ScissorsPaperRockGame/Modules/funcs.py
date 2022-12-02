import json


def calcLetters(word):
    return len(word)*16


def cCalcLetters(word, length):
    return len(word)*16*length/20


def write_to_user_data(word, data):
    with open("./user.json", "r+") as f:
        content = f.read()
        jsoncontent = json.loads(content)
        jsoncontent[word] = data
        f.seek(0)
        f.truncate(0)
        f.write(json.dumps(jsoncontent))
        f.close()


def read_from_user_data(word):
    with open("./user.json", "r") as f:
        content = f.read()
        jsoncontent = json.loads(content)
        f.close()
        return jsoncontent[word]
