sh = input("Enter hours:")
sr = input("Enter rate:")

fh = float(sh)
fr = float(sr)


if fh > 40:
    regular = 40 * fr
    extra = fr*1.5 * (fh-40)

    xp = regular + extra

else:
    xp = fh * fr

print("Pay:", xp)