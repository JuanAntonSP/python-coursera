# Getting the file name using the prompt

while True:
    fName = input("Enter the file name:")
    if fName != "":
        try:
            file = open(fName)
        except:
            print("File cannot be opened", fName)
            break
            quit()

        count = 0
        for line in file:
            if line.startswith("Author:"):
                count = count + 1
        print("We found ", count, " times the word 'Author: ' in", fName)
        break
    else:
        print("ingresa un nombre")
