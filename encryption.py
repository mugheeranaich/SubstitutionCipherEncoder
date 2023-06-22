print("Three character substitution!!\n")

initial_alph = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"," "]

encryption_alph = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C"," "]

name = input("Enter your message all letters should be uppercase : ")
data = []
for i in name:
    c = initial_alph.index(i)
    b = encryption_alph[c]
    data.append(b)
print("".join(data))
