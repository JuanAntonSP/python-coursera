greet = "hello Bob"
zap = greet.lower()
print(zap)
print(greet)
print("Hello Juan".lower())

stuff = "Hello World"
type(stuff)
dir(stuff)

# dir: función incorporada para encontrar todos los métodos y atributos disponibles par aun objeto.
print(dir(stuff))

# example
str = "Juan Antonio Cahuana"
str.capitalize()
print(str.upper()) # JUAN ANTONIO
print(str.strip())
print(str.replace(" ", "")) #JuanAntonioCahuana


# searching a string
position = str.find("sss")
found = position != -1
print("pos", position, found)


