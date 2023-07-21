n=input()
for i in range(len(n)):
    for j in range(len(n)):
        combination=n[i:j+1]
        print(combination,end=" ")
combination=combination+n[0]
print(combination)
