from tkinter import *

root = Tk()
root.geometry("600x500")
root.title("Cuenta Vocales")


def VowelCounter():
    Output.delete('1.0', END)
    CountVowels = str(inputtxt.get("1.0", "end-1c"))
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

    TerribleLongAnswer = ""

    TerribleLongAnswer = TerribleLongAnswer + "El texto a analizar tiene {} caracteres:\n".format(len(CountVowels))

    for key, value in d_vowels.items():
        TerribleLongAnswer = TerribleLongAnswer + "\nLa vocal '{}' aparece {} veces.".format(key, value)

    Output.insert(END, TerribleLongAnswer)


l = Label(text="\nEscribe una frase o texto: \n")
inputtxt = Text(root, height=10,
                width=60,
                bg="light yellow")

Output = Text(root, height=10,
              width=50,
              bg="white")

Display = Button(root, height=2,
                 width=20,
                 text="Cuenta las vocales",
                 command=lambda: VowelCounter())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
