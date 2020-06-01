import requests

# This demo client is not the smartest one, it will always walk diagonal left down.
# It is good for developing a own client.

host = 'http://localhost:8081'


def ednTurn(register):
    end = requests.put(host + '/game/endturn', auth=(register['username'], register['clearPassword']))
    if (end.status_code != 200):
        # Error case
        print(end.json())
    else:
        # normal case
        print("Next players turn")


def getMapInformation(register):
    return requests.get(host + '/game', auth=(register['username'], register['clearPassword'])).json()


def getAllMeepleFromMap(map):
    ret = []
    for field in map:
        if (field['meeple'] != None):
            # meeple is here
            ret.append(field)
    return ret


def move(meeple, register):
    # meeple example:
    # {'id': 13, 'coordinate': {'id': 14, 'xcoordinate': 1, 'ycoordinate': 0}, 'meeple': {'id': 15, 'name': 'Starfighter', 'color': '#0033ff', 'username': 'xx'}, 'empty': False}
    x = meeple['coordinate']['xcoordinate'] + 1
    y = meeple['coordinate']['ycoordinate'] + 1
    id = meeple['meeple']['id']

    url = host + '/game/' + str(id) + '/' + str(x) + '/' + str(y)
    move = requests.put(url, auth=(register['username'], register['clearPassword']))
    if (move.status_code != 200):
        print(move.json()['message'])


if __name__ == '__main__':
    # register a random user
    register = requests.post(host + '/user/register/' + 'XxXMeisterXxX')
    if (register.status_code == 226):
        print("Username is already taken")
        exit(-1)
    else:
        register = register.json()
    print('Password for user: ' + register['clearPassword'])
    register = register
    # log in the user
    login = requests.post(host + '/user/login', auth=(register['username'], register['clearPassword']))
    print("login successful" if login.status_code == 200 else "login not successful")
    # test if its my Turn
    turn = False
    while not turn:
        res = requests.get(host + '/game/myturn', auth=(register['username'], register['clearPassword']))
        if (res.json().__eq__("OK")):
            # It's my turn
            map = getMapInformation(register)
            # map example:
            # [{'id': 91, 'coordinate': {'id': 92, 'xcoordinate': 39, 'ycoordinate': 0}, 'meeple': None, 'empty': True}, {'id': 19, 'coordinate': {'id': 20, 'xcoordinate': 3, 'ycoordinate': 0}, 'meeple': None, 'empty': True}, {'id': 13, 'coordinate': {'id': 14, 'xcoordinate': 1, 'ycoordinate': 0}, 'meeple': {'id': 15, 'name': 'Starfighter', 'color': '#0033ff', 'username': 'xx'}, 'empty': False}, {'id': 11, 'coordinate': {'id': 12, 'xcoordinate': 0, 'ycoordinate': 0}, 'meeple': None, 'empty': True}, {'id': 16, 'coordinate': {'id': 17, 'xcoordinate': 2, 'ycoordinate': 0}, 'meeple': {'id': 18, 'name': 'Transporter', 'color': '#0033ff', 'username': 'xx'}, 'empty': False}]
            meeple = getAllMeepleFromMap(map)
            print(len(meeple))
            for m in meeple:
                move(m, register)
            ednTurn(register)
