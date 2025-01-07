def countCharacterType(file):
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0
    space=0
    v="aeiou"
    c="bcdfghjklmnpqrstvwxyz"
    for line in file:
             for i in line.lower():
                    if i.isalpha():
                            if i in v: 
                                vowels += 1
                            elif i in c:
                                consonant += 1
                    elif i.isdigit():
                          digit += 1
                    elif i.isspace():
                          space+=1
                    else:
                          specialChar += 1
    print("Vowels:", vowels)
    print("Consonant:", consonant) 
    print("Digit:", digit) 
    print("Special Character:", specialChar)
    print("Number of Space:",space)

file=open("python.txt","r+")
countCharacterType(file)
