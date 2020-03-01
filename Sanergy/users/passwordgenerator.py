import random
import string


def generatePassword(length):
    alphaNum = string.ascii_letters + string.digits * 2
    password = ""
    for x in range(0,length):
        randomChar = random.randrange(0,len(alphaNum))
        password += alphaNum[randomChar]
    # print (password)
    return(password)

generatePassword(15)
# print(type("generatePassword(15)"))