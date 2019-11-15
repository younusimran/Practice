message = input("Enter a message to encrypt - Only message in alphabet will be encrypted: ")

cond = True
while cond:
    try:
        shift = input("Enter number to use word shift for encrypting or type exit to quit: ")
        if shift.upper() == "EXIT":
            break
        else:
            shift = int(shift)
            cond = False
    except:
        continue
nm = ""
count = 0
for char in message:
    if char.isalpha() and char.isupper():
        if (ord(char)+shift) > 90: 
            count = 90 - ord(char)
            while count < shift:
                count += 26
                #count += 90 - 65 + 1
                if count < shift:
                    num = shift - count
            count = 0
            nm += chr((65+num-1))
            num = 0
            #nm += chr((ord("A") + shift-(90-ord(char)+1)))
        else:
            nm += chr(ord(char)+shift)
    elif char.isalpha() and char.islower():
        if (ord(char)+shift) > 122:
            count = 122 - ord(char)
            while count < shift:
                count += 26
                #count += 122 - 97 + 1
                if count < shift:
                    num = shift - count
            count = 0
            nm += chr((97+num-1))
            num = 0
            #nm += chr((ord("a") + shift-(122-ord(char)+1)))
        else:
            nm += chr(ord(char)+shift)
    else:
        nm += char


print("The message was: ",message)
print("Character shift for alphabets was: ",shift)
print("Encrypted message: ",nm)
