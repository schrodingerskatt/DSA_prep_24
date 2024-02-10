celebrity = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
stack = []

n = len(celebrity)
for i in range(n):
    stack.append(i)

while len(stack) >= 2:
    i = stack.pop()
    j = stack.pop()
    if celebrity[i][j] == 1: # if 'i' knows 'j', then 'j' cannot be celebrity
        stack.append(j)
    else:
        stack.append(i)
potential_celebrity = stack.pop()
flag = False
for i in range(n):
    if i != potential_celebrity:
        if celebrity[potential_celebrity][i]==1 or celebrity[i][potential_celebrity] == 0:
            flag = True
            break
if flag == False:
    print(potential_celebrity, "is a celebrity.")
else:
    print("There is no potential celebrity")