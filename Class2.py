
number = input("enter a sentancne: ").lower()

numbers = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "y":0, "z":0}


for i in number:
    if i in numbers:
        numbers[i] += 1
print(numbers)
panogram = True
for j in numbers.values():
    if j == 0:
        panogram = False
if panogram:
    print("Enterd letter is a panogram")
else:
    print("enterd letter is not a panogram")



