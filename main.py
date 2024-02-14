from jsonpath_rw_ext import parse
import json


def readJson(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
    
def extractUsernames(jsondata):
    json_username_expression = parse('$..value')
    usernames = [match.value for match in json_username_expression.find(jsondata)]
    return usernames

followers = extractUsernames(readJson('followers.json'))
following = extractUsernames(readJson('following.json'))
followers_old = extractUsernames(readJson('followers-old.json'))


def notFollowingMe():
    count = 0
    for fol in following:
        if fol not in followers:
            count = count + 1
            print(count, fol)

def unfollowedMe():
    count = 0
    for fol in followers_old:
        if fol not in followers:
            count = count + 1
            print(count, fol)


def notFollowingBack():
    count = 0
    for fol in followers:
        if  fol not in following:
            count = count + 1
            print(count, fol)

def newFollowers():
    count = 0
    for fol in followers:
        if fol not in  followers_old:
            count += 1
            print(count, fol)


while (True):
    print(''' 
1. Ακολουθώ αλλά δε με ακολουθούν
2. Με ξε-ακολούθησαν
3. Με ακολουθούν αλλά δεν ακολουθώ
4. Νέοι ακόλουθοι
0. Έξοδος
          ''')
    command = int(input("Δώσε ενέργεια: "))

    if (command == 1):
        notFollowingMe()
    elif (command == 2):
        unfollowedMe()
    elif (command == 3):
        notFollowingBack()
    elif (command == 4):
        newFollowers()
    elif(command == 0):
        break
    else:
        print("Μη έγκυρη ενέργεια.")

    print("------------------------------")
