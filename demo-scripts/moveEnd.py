import random
import string
import sys

import requests


# Variables
host = "http://localhost:8081"
admin = 'admin'
admin_pw = '123'

if __name__ == '__main__':
        # Get the map informations
    #user = sys.argv[1]
    #pw = sys.argv[2]
    user = "TetrisIQ"
    pw = "7b13984732384f60854f0fe451d01241"
    id = sys.argv[1]
    x = sys.argv[2]
    y = sys.argv[3]

    move = requests.put(host + '/game/' + str(id)+ '/'+ str(x) +'/' +str(y), auth=(user, pw))
    print(move.status_code)
    if(move.status_code != 200):
        print(move.json())
    
    end = requests.put(host + '/game/endturn' , auth=(user, pw))
    print(end.status_code)
    if(end.status_code != 200):
        print(end.json())

