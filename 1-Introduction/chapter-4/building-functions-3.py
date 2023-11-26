# return values
def greet(lang='en'):
    if lang == 'es':
        return "hola"
    elif lang == 'en':
        return "hello"
    else:
        return "hello"


# use it
print(greet('es'), 'Juan')
print(greet('en'), 'Sally')
