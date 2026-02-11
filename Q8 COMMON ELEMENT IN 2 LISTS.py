def common(l1, l2): 
    for i in l1:
        for j in l2:
            if i==j:
                return True
    return False
x=list(input("Enter elements of List1 :").split(" "))
y=list(input("Enter elements of List2 :").split(" "))
print(common(x,y))
