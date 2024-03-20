import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class MyVocalsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.l2 = customtkinter.CTkLabel(self, text="\nEscribe una frase o texto: \n",
                                    font=customtkinter.CTkFont(size=16, weight="normal"))
        self.l2.grid(row=0, column=0, padx=10, pady=5)

        self.inputtxt = customtkinter.CTkTextbox(self, width=400, corner_radius=0, bg_color="white")
        self.inputtxt.grid(row=1, column=0, padx=10, pady=5)

        def VowelCounter():
            self.outputtxt.delete('0.0', "end")
            CountVowels = str(self.inputtxt.get("0.0", "end"))
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

            self.outputtxt.insert("0.0", TerribleLongAnswer)

        self.display = customtkinter.CTkButton(self, text="Cuenta las vocales.", width=28, command=lambda: VowelCounter())
        self.display.grid(row=2, column=0, padx=10, pady=5)

        self.outputtxt = customtkinter.CTkTextbox(self, width=400, corner_radius=0, bg_color="gray")
        self.outputtxt.grid(row=3, column=0, padx=10, pady=5)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{600}x{700}")
        self.title("Cuenta Vocales")
        self.grid_rowconfigure(2, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1)
        self.my_frame = MyVocalsFrame(master=self)
        self.my_frame.grid(row=2, column=1, padx=10, pady=10)


app = App()
app.mainloop()
