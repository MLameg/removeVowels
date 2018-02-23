import string
x = input("Please enter a sentence: ").lower()

removeA = x.replace("a", "")
removeE = removeA.replace("e", "")
removeI = removeE.replace("i", "")
removeO = removeI.replace("o", "")
removeU = removeO.replace("u", "")

print("All vowels have been removed: " + removeU)


print(removeU.translate(bytes.maketrans(b"vb",b"bv")))

