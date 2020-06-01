import random
import string
import sys
import requests

# Variables
host = "http://localhost:8081"

# Methods
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def prettyPrint(map):
    for field in map:
        if not field["empty"]:
            print(field["meeple"]["name"] + " ID: " + str(field["meeple"]["id"]) + " at: " + str(field["coordinate"]["xcoordinate"]) + "/" + str(field["coordinate"]["ycoordinate"]))
        

if __name__ == '__main__':
    user = sys.argv[1]
    if(user == None):
        user = randomString

    # I generate random strings as Username
    register = requests.post(host + '/user/register/' + user).json()
    print(register)
    login = requests.post(host + '/user/login', auth=(register['username'], register['clearPassword'])).json()
    print(login)

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


