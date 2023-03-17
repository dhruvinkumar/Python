que = [40, 50, 60]
amount = [1000, 2000, 3000]

ans = 0
i = 0
while i < len(que):
    inp = int(input("Guess the number "))
    if(inp == que[i]):
        ans += amount[i]
        i += 1
    else:
        break

print("Your winnig amount is ",ans)