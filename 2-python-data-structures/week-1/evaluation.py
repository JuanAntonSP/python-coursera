# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
startPos = text.find("    ")

strNumber = text[startPos:]
flNumber = float(strNumber)
print(flNumber)



# Option 2
delimiterPos = text.find(":")
newText = text[delimiterPos+1:]
newText = newText.strip()
result = float(newText)
print(result)

