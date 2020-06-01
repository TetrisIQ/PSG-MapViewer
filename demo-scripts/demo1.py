import requests

# This demo client is not the smartest one, it will always skip his turn.
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

if __name__ == '__main__':
    # register a random user
    register = requests.post(host + '/user/register/' + 'xxXDemoUser_OneXxx')
    if(register.status_code == 226):
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
            ednTurn(register)