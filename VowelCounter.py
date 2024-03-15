import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


root = customtkinter.CTk()
root.geometry("600x700")
root.title("Cuenta Vocales")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


l2 = customtkinter.CTkLabel(master=frame, text="\nEscribe una frase o texto: \n",
                            font=customtkinter.CTkFont(size=16, weight="normal"))
l2.pack(padx=20, pady=10)

inputtxt = customtkinter.CTkTextbox(master=frame, width=400, corner_radius=0, bg_color="white")
inputtxt.pack(padx=20, pady=10)

outputtxt = customtkinter.CTkTextbox(master=frame, width=400, corner_radius=0, bg_color="gray")
outputtxt.pack(padx=20, pady=10)


def VowelCounter():
    outputtxt.delete('0.0', "end")
    CountVowels = str(inputtxt.get("0.0", "end"))
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

    outputtxt.insert("0.0", TerribleLongAnswer)


display = customtkinter.CTkButton(master=frame, text="Cuenta las vocales.", height=2, width=20, command=lambda: VowelCounter())
display.pack(padx=20, pady=10)

root.mainloop()
