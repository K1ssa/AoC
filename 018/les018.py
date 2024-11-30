def shift(zin, j):
    result = ""

    for i in range(len(zin)):
        char = zin[i]

        if (char.isupper()):
            result +=chr((ord(char) + j - 65) % 26 + 65)
        elif char == " ":
            result += char
        else:
            result += chr((ord(char) + j - 97) % 26 + 97)

    return result

zin = "Een loempia is best lekker"
j = input( "Geef een shift getal: ")
j = int(j)

print("Te coderen tekst: " + zin)
print("Shift nummer: " , j)
print("Gecodeerde tekst: " + shift(zin, j))


