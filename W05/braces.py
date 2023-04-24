file = input("File: ")
content1 = open(file, "r")

braces = []

balanced = True

for brace in content1:
    brace = brace.strip()
    if (brace == "(") or (brace == "[") or (brace == "{"):
        braces.append(brace)
    else:
        if (len(braces) == 0):
            balanced == False
            break

        pre_brace = braces.pop()
        if (((brace == ")") and (pre_brace != "(")) or
            ((brace == "}") and (pre_brace != "{")) or
            ((brace == "]") and (pre_brace != "["))):
            balanced = False
            break
content1.close

if (len(braces) != 0) or (not balanced):
    print("Not balanced")
else:
    print("Balanced")


