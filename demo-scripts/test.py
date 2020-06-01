import random
import string

import requests


# Variables
host = "http://localhost:8081"
admin = 'admin'
admin_pw = '123'

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def prettyPrint(map):
    for field in map:
        if not field["empty"]:
            print(field["meeple"]["name"] + " ID: " + str(field["meeple"]["id"]) + " at: " + str(field["coordinate"]["xcoordinate"]) + "/" + str(field["coordinate"]["ycoordinate"]))
        

if __name__ == '__main__':
    # I generate random strings as Username, so i don't need to restart the server for testing
    register = requests.post(host + '/user/register/' + 'TetrisIQ').json()
    print(register)
    login = requests.post(host + '/user/login', auth=(register['username'], register['clearPassword'])).json()
    print(login)

    # Admin starts the Game
    adminreq = requests.put(host + '/admin/start', auth=(admin, admin_pw))
    print(adminreq.status_code)

    #test if its my Turn
    turn = False
    while not turn:
        res = requests.get(host + '/game/myturn', auth=(register['username'], register['clearPassword']))
        if(res.status_code == 200):
            turn = True
    print(res.status_code)

    # Get the map informations
    map = requests.get(host + '/game', auth=(register['username'], register['clearPassword'])).json()
    print(prettyPrint(map))

    #i = 0
    #meeple = map[i]
    #while meeple["empty"]:
    #    i+=1
    #    meeple = map[i]

    #print(meeple)
    #print(host + '/game/' + str(meeple["meeple"]["id"])+ '/'+ str(meeple['coordinate']['xcoordinate'] +1) +'/' +str(meeple['coordinate']['ycoordinate']))    
    #move = requests.put(host + '/game/' + str(meeple["meeple"]["id"])+ '/'+ str(meeple['coordinate']['xcoordinate'] + 1) +'/' +str(meeple['coordinate']['ycoordinate']), auth=(register['username'], register['clearPassword']))
    #print(move.status_code)
    #if(move.status_code != 200):
    #    print(move.json())



