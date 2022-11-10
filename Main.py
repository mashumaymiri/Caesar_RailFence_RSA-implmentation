import math
import os
import random
import sympy

import numpy as np

# save to txt file
def SaveToFile(array, folder, fileName):
    file = open(os.getcwd()+"\\"+folder+"\\"+fileName+".txt", "w")
    file.write(''.join(str(x) for x in array))
    file.close()
    print("Succesfully encrypted message.")
    print("Encrypted message: "+''.join(str(x) for x in array))
    print("Saved cipher text to "+fileName+".txt.")

# Caesar Algorithm
def CreateKeyList(messageList, key): 
    keyList = np.zeros(shape=len(messageList), dtype= str) 
    n = 0
    for char in messageList:
        keyList[n] = key[n % len(key)]
        n = n + 1
    return keyList

def CaesarAlgorithmEncryption(message, key):
    message = message.replace(" ", "")
    
    LTN = {"A": 0,"B": 1,"C": 2,"D": 3,"E": 4,"F": 5,"G": 6, "H": 7,"I": 8,"J": 9,"K": 10,"L": 11,"M": 12,"N": 13,"O": 14,"P": 15,"Q": 16,"R": 17,"S": 18,"T": 19,"U": 20,"V": 21,"W": 22,"X": 23,"Y": 24,"Z": 25}
    NTL = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F", 6 : "G", 7 : "H", 8 : "I", 9 : "J", 10 : "K",11 : "L",12 : "M",13 : "N",14 : "O",15 : "P",16 : "Q",17 : "R",18 : "S",19 : "T",20 : "U",21 : "V",22 : "W",23 : "X",24 : "Y",25 : "Z",}
        
    messageList = np.array(list(message))

    # Create key list.
    keyList = CreateKeyList(messageList, key)

    # Encrypt the message
    cryptedList = np.zeros(shape=len(messageList), dtype= str) 
    n = 0
    for char in messageList:
        cryptedList[n] = NTL[(LTN[char.upper()] + LTN[keyList[n].upper()]) % 26]
        n = n + 1

    # save to txt file
    SaveToFile(cryptedList, "Caesar Algorithm", "Cipher-text")

def CaesarAlgorithmDecryption(Cipher, key):
    LTN = {"A": 0,"B": 1,"C": 2,"D": 3,"E": 4,"F": 5,"G": 6, "H": 7,"I": 8,"J": 9,"K": 10,"L": 11,"M": 12,"N": 13,"O": 14,"P": 15,"Q": 16,"R": 17,"S": 18,"T": 19,"U": 20,"V": 21,"W": 22,"X": 23,"Y": 24,"Z": 25}
    NTL = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F", 6 : "G", 7 : "H", 8 : "I", 9 : "J", 10 : "K",11 : "L",12 : "M",13 : "N",14 : "O",15 : "P",16 : "Q",17 : "R",18 : "S",19 : "T",20 : "U",21 : "V",22 : "W",23 : "X",24 : "Y",25 : "Z",}
        
    CipherList = np.array(list(Cipher))

    # Create key list.
    keyList = CreateKeyList(Cipher, key)

    # Decrypt the message
    messageList = np.zeros(shape=len(CipherList), dtype= str) 
    n = 0
    for char in CipherList:
        messageList[n] = NTL[(LTN[char.upper()] - LTN[keyList[n].upper()]) % 26]
        n = n + 1

    # Print a success message if the original text is the same as the decrypted text
    file = open(os.getcwd()+"\Caesar Algorithm\Plain-text.txt", "r")
    message = file.readlines()[0]
    file.close()

    if ''.join(str(x) for x in messageList).upper() == message.replace(" ", "").upper():
        print("Successfully decrypted message.")
        print("Decrypted message: "+''.join(str(x) for x in messageList))
    else:
        print("Error in decrpyting the message, the key is not correct.")

# Rail fence cipher 
def RailFenceCipherEncryption(message):
    message = message.replace(" ", "")
    # Create Lists
    oddList = []
    evenList = []

    # move messages into lists based on even or odd
    n = 0 
    for char in message:
        if n % 2 == 1:
            oddList.append(char)
        else:
            evenList.append(char)
        n = n + 1
    oddList = np.array(oddList)
    evenList = np.array(evenList)
    print(evenList)
    print(oddList)
    cipherList = np.concatenate((evenList, oddList))

    # save to txt file
    SaveToFile(cipherList, "Rail fence cipher", "Cipher-text")

def RailFenceCipherDecryption(cipher):
    n = len(cipher)
    evenList = np.array(list(cipher[0:math.ceil(n/2)]))
    oddList = np.array(list(cipher[math.ceil(n/2):n]))
    print(evenList)
    print(oddList)
    messageList = []
    for k in range(math.ceil(n/2)):
        if k < len(evenList):
            messageList.append(evenList[k])
        if k < len(oddList):
            messageList.append(oddList[k])

    # Print a success message if the original text is the same as the decrypted text
    file = open(os.getcwd()+"\Rail fence cipher\Plain-text.txt", "r")
    message = file.readlines()[0]
    file.close()

    if ''.join(str(x) for x in messageList).upper() == message.replace(" ", "").upper():
        print("Successfully decrypted message.")
        print("Decrypted message: "+''.join(str(x) for x in messageList))
    else:
        print("Error in decrpyting the message, the key is not correct.")

# RSA
def inputPrimeNumber(p):
    print("1- Random prime number")
    print("2- Custom prime number")
    while True: 
        try:
            x = int(input("Random/Custom: "))
            if x > 2 or x < 1: 
                print("Error! Enter number must be between 1 and 2.")
            else: 
                break
        except:
            print('Invalid, please enter a number')

    if x == 1: 
        print("Enter max number")
        while True: 
            try:
                x = int(input("Max number: "))
                break
            except:
                print('Invalid, please enter a number')
        print("Selecting random prime number between 0 and "+str(x)+" .....")
        while True:
            x = sympy.randprime(0, x)
            if x != p:
                break
        
        print("your prime number is "+str(x))
    elif x == 2:
        print("Enter prime number")
        while True: 
            try:
                x = int(input("Prime number: "))
                if x == p: 
                    print("WARNING: Choosing the same prime number for p and q is not secure and not supported!")
                else:
                    if not sympy.isprime(x): 
                        print("Error! Enter number must be prime.")
                    else: 
                        break
            except:
                print('Invalid, please enter a number')
    return x

def inputCoprimeNumber(p, q):
    phiN = (p-1)*(q-1)
  
    
    print("Valid numbers for e:")
    validEs = []
    for x in range(2, phiN):
        if math.gcd(x, phiN) == 1:
            validEs.append(x)
    print(','.join(str(y) for y in validEs))
    print("Enter coprime number")
    while True: 
        try:
            x = int(input("coprime number: "))
            if x == 0:
                x = random.choice(validEs)
                print("your coprime number is "+str(x))
                break

            if not sympy.isprime(x): 
                print("Error! Enter number must be prime.")
            else: 
                break
        except:
            print('Invalid, please enter a number')
    return x

def RSAKeyGeneration():
    print("**Key generation**")
    print("Enter prime number p: ")
    p = inputPrimeNumber(-1)
    print("Enter prime number q: ")
    q = inputPrimeNumber(p)
    print("p = "+str(p))
    print("q = "+str(q))
    n = str(p*q)
    print("n = "+n)
    phiN = (p-1)*(q-1)
    print("phiN = "+str(phiN))
    e = inputCoprimeNumber(p, q)
    print("e = "+str(e))
    print("** Key details**")
    print("p = "+str(p))
    print("q = "+str(q))
    print("n = "+n)
    print("phiN = "+str((p-1)*(q-1)))
    print("e = "+str(e))
    d = pow(e, -1, phiN)
    print("d = "+str(d))
    print("Public key: ("+str(e)+", "+str(n)+")")
    print("Private key: ("+str(d)+", "+str(n)+")")
    return n, e, d

def RSAKeySelection():
    n, e, d = 0, 0, 0
    while True: 
        n, e, d = 0, 0, 0
        while True: 
            try:
                n = int(input("enter n: "))
                break
            except:
                print('Invalid, please enter a number')
                
        while True: 
            try:
                e = int(input("enter e: "))
                break
            except:
                print('Invalid, please enter a number')
                
        while True: 
            try:
                d = int(input("enter d: "))
                break
            except:
                print('Invalid, please enter a number')
        m = 4
        print("Testing keys .....")
        if RSADecryption(RSAEncryption(m, e, n), d, n) == m: 
            break
        else: 
            print("Error!. Public key and private key dont match!")
    return n, e, d

def RSAEncryption(m, e, n):
    print("Encrypting message: "+str(m)+" ......")
    c = pow(m, e) % n
    print("Encrypted message is: "+str(c))
    return c

def RSADecryption(c, d, n):
    print("Decrypting cipher: "+str(c)+" ......")
    m = pow(c, d) % n
    print("Decrypted message is: "+str(m))
    return m

def main():
    while True:
        print("\033[92mWelcome to CSC429 course project.")
        print("Use numbers to select the algorithm:")
        print("1- Ceasar algorithm")
        print("2- Rail fence cipher")
        print("3- RSA")
        print("0- Exit")
        print('\033[0m')
        while True: 
            try:
                x = int(input("Algorithm: "))
                if x > 3 or x < 0: 
                    print("Error! Enter number between 1 and 3.")
                else: 
                    break
            except:
                print('Invalid algorithm, please enter a number')

        if x == 0:
            break
        elif x == 1: 
            while True: 
                key = input("Enter your key: ")
                if not key.isalpha():
                    print("Error! Please enter only alphabetical characters.")
                else: 
                    break
            key = key.upper()
            print("your key is: "+key)
            print("\033[92m1- Encryption")
            print("2- Decryption")
            print('\033[0m')
            while True: 
                try:
                    x = int(input("function: "))
                    if x > 2 or x < 1: 
                        print("Error! Enter number between 1 and 2.")
                    else: 
                        break
                except:
                    print('Invalid algorithm, please enter a number')
            if x == 1:
                try:
                    if os.stat(os.getcwd()+"\Caesar Algorithm\Plain-text.txt").st_size > 0:
                        print("Reading from Plain-text file")
                        file = open(os.getcwd()+"\Caesar Algorithm\Plain-text.txt", "r")
                        message = file.readlines()[0]
                        file.close()
                    else: 
                        print("Error! No message found")
                        print("Please fill the Plain-text.txt file")
                        return 
                    CaesarAlgorithmEncryption(message, key)
                except OSError:
                    print("Error! No message found")
                    print("Please Create a Plain-text.txt file")
            elif x == 2:
                try:
                    if os.stat(os.getcwd()+"\Caesar Algorithm\Cipher-text.txt").st_size > 0:
                        print("Reading from Plain-text file")
                        file = open(os.getcwd()+"\Caesar Algorithm\Cipher-text.txt", "r")
                        message = file.readlines()[0]
                        file.close()
                    else: 
                        print("Error! No message found")
                        print("Please fill the Cipher-text.txt file")
                        return 
                    CaesarAlgorithmDecryption(message, key)
                except OSError:
                    print("Error! No message found")
                    print("Please Create a Cipher-text.txt file")
        elif x == 2:
            print("\033[92m1- Encryption")
            print("2- Decryption")
            print('\033[0m')

            while True: 
                try:
                    x = int(input("function: "))
                    if x > 2 or x < 1: 
                        print("Error! Enter number between 1 and 2.")
                    else: 
                        break
                except:
                    print('Invalid algorithm, please enter a number')
            if x == 1: 
                try:
                    if os.stat(os.getcwd()+"\Rail fence cipher\Plain-text.txt").st_size > 0:
                        print("Reading from Plain-text file")
                        file = open(os.getcwd()+"\Rail fence cipher\Plain-text.txt", "r")
                        message = file.readlines()[0]
                        file.close()
                    else: 
                        print("Error! No message found")
                        print("Please fill the Plain-text.txt file")
                        return 
                    RailFenceCipherEncryption(message)
                except OSError:
                    print("Error! No message found")
                    print("Please Create a Plain-text.txt file")
            elif x == 2:
                try:
                    if os.stat(os.getcwd()+"\Rail fence cipher\Cipher-text.txt").st_size > 0:
                        print("Reading from Plain-text file")
                        file = open(os.getcwd()+"\Rail fence cipher\Cipher-text.txt", "r")
                        message = file.readlines()[0]
                        file.close()
                    else: 
                        print("Error! No message found")
                        print("Please fill the Cipher-text.txt file")
                        return 
                    RailFenceCipherDecryption(message)
                except OSError:
                    print("Error! No message found")
                    print("Please Create a Cipher-text.txt file")
        elif x == 3:
            print("1- Generate Keys for RSA")
            print("2- Enter Keys for RSA")
            n, e, d = 0, 0, 0
            while True: 
                try:
                    x = int(input(": "))
                    if x > 2 or x < 1: 
                        print("Error! Enter number between 1 and 2.")
                    else: 
                        break
                except:
                    print('Invalid, please enter a number')
            if x == 1:
                n, e, d = RSAKeyGeneration()
                print("Successfully generated keys!")
            elif x == 2: 
                n, e, d = RSAKeySelection()
                print("Successfully selected keys!")
            
            while True: 
                print("Enter message or cipher")
                while True: 
                    try:
                        m = int(input("m: "))
                        break
                    except:
                        print('Invalid, please enter a number')

                print("1- Encrypt Message")
                print("2- Decrypt Message")
                print("0- Exit")
                while True: 
                    try:
                        x = int(input(": "))
                        if x > 2 or x < 0: 
                            print("Error! Enter number between 0 and 2.")
                        else: 
                            break
                    except:
                        print('Invalid, please enter a number')
                if x == 1:
                    RSAEncryption(m, e, n)
                elif x == 2:
                    RSADecryption(m, d, n) 
                elif x == 0:
                    break

if __name__ == "__main__":
    main()