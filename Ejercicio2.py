texto_1 = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
texto_2 = "Un día que el viento soplaba con fuerza..."
"- Mira como se mueve aquella banderola -dijo un monje."
"- Lo que se mueve es el viento -respondió otro monje."
"- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro."

corregido_1 = texto_1.capitalize().replace("#"," -").replace(" -",".\n-")
print(corregido_1,end=".")
