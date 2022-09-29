import hashlib
from urllib.request import urlopen


# Defining Functions
def readWordFile(url):
    wListFile = urlopen(url).read()
    return wListFile


def hash(password):
    res = hashlib.sha1(password.encode())
    return res.hexdigest()

    
def BruteForce(Glist, Ahash ):
    for word in Glist:
        if Ahash == hash(word):
            print("pass: ", word)
            print("your pass is not secure.")
            quit()

            
#seeting the info for the attack
url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
#Making the raw words into a list that the BruteForce func can use (for loop)
wlist = readWordFile(url).decode('UTF-8')
RList = wlist.split('\n')

#finally running the program to check pass
password = input("Enter your password to check: ")
passhash = hash(password)
BruteForce(RList, passhash)
# succsess 
print("your pass is secure.")
