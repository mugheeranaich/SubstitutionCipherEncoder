print("Three character substitution!!\n")

initial_alph = [ "A","a", "B","b", "C","c", "D","d", "E","e", "F","f", "G","g", "H","h", "I","i", "J","j", "K","k", "L","l", "M","m", "N","n" ,"O","o", "P", "p", "Q","q", "R","r", "S","s", "T","t", "U","u", "V","v", "W","w", "X","x", "Y","y", "Z","z"," "]

encryption_alph = ["D","d", "E","e", "F","f", "G","g", "H","h", "I","i", "J","j", "K","k", "L","l", "M","m", "N","n" ,"O","o", "P", "p", "Q","q", "R","r", "S","s", "T","t", "U","u", "V","v", "W","w", "X","x", "Y","y", "Z","z","A","a", "B","b", "C","c"," "]

name = input("Enter your message: ")
# print(initial_alph.index[])
# print(index.[encryption_alph])

data = []
for i in name:
    c = initial_alph.index(i)

    b = encryption_alph[c]
    data.append(b)
print("".join(data))
