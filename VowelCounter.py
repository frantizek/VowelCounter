CountVowels = str(input("Escribe una frase o texto: "))

d_vowels = {"a": 0,  "e": 0, "i": 0, "o": 0, "u": 0}

for letter in CountVowels:
    if "a" in letter.lower():
        d_vowels["a"] = d_vowels["a"] + 1
    if "e" in letter.lower():
        d_vowels["e"] = d_vowels["e"] + 1
    if "i" in letter.lower():
        d_vowels["i"] = d_vowels["i"] + 1
    if "o" in letter.lower():
        d_vowels["o"] = d_vowels["o"] + 1
    if "u" in letter.lower():
        d_vowels["u"] = d_vowels["u"] + 1

print("\nEl texto a analizar tiene {} caracteres:".format(len(CountVowels)))

for key, value in d_vowels.items():
    print("La vocal '{}' aparece {} veces.".format(key, value))
