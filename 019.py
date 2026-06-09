S = input()

sutakku = []

ans = "Yes"

for c in S:
    if c == "(":
        sutakku.append(c)
    else:
        if len(sutakku) == 0:
            ans = "No"
            break

        sutakku.pop()

if len(sutakku) != 0:
    ans = "No"
    
print(ans)