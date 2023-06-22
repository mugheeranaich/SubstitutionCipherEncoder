import sys
string ="Three character substitution!!"
print (string.center(50))

print("1:Encyption\n2:Decryption")
choice = int(input("Enter your choice[1or2]: "))


initial_alph = [ "A","a", "B","b", "C","c", "D","d", "E","e", "F","f", "G","g", "H","h", "I","i", "J","j", "K","k", "L","l", "M","m", "N","n" ,"O","o", "P", "p", "Q","q", "R","r", "S","s", "T","t", "U","u", "V","v", "W","w", "X","x", "Y","y", "Z","z"," ","0","1","2","3","4","5","6","7","8","9"]

encryption_alph = ["D","d", "E","e", "F","f", "G","g", "H","h", "I","i", "J","j", "K","k", "L","l", "M","m", "N","n" ,"O","o", "P", "p", "Q","q", "R","r", "S","s", "T","t", "U","u", "V","v", "W","w", "X","x", "Y","y", "Z","z","A","a", "B","b", "C","c"," ","3","4","5","6","7","8","9","0","1","2"]


if choice == 1:
    name = input("Enter your message: ")
    data = []
    for i in name:
        c = initial_alph.index(i)
        b = encryption_alph[c]
        data.append(b)
    print("".join(data))
elif choice == 2:
    name = input("Enter your message: ")
    data = []
    for i in name:
        c = encryption_alph.index(i)
        b = initial_alph[c]
        data.append(b)
    print("".join(data))

else:
    sys.exit("Invalid input")
