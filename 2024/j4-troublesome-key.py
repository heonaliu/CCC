#preconditions: silly and quiet key NEVER pressed consecutively
#silly key pressed at least once
#never pressses the letter that the silly key displays
path = "2024/j4-troublesome-key-input.txt"

with open(path, 'r') as file:
    lines = file.readlines()

lines = [i.strip() for i in lines]
print(lines)
pressed = lines[0]
shown = lines[1]

i = 0
j=0

silly = None
wrong_letter = None
quiet = None

while i<len(pressed) and j<len(shown):
    p = pressed[i]
    s = shown[j]

    if p==s:
        i+=1
        j+=1

    else:

        if silly is None or p == silly:
            silly = p
            wrong_letter = s
            i+=1
            j+=1
        else:
            quiet = p
            i+=1 #only increment pressed if there's a silient letter

while i < len(pressed):
    quiet=pressed[i]
    i+=1 #every leftover key MUST be silent

print(silly, wrong_letter)
print(quiet if quiet is not None else "-")
