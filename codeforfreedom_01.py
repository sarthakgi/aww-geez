num=int(input("Enter length: "))
order=[]
list1=[]
print("Enter required order in which the strings are to be printed separated by ENTER")
for i in range(num):
    order.append(int(input()))
print("Enter strings to be printed separated by ENTER")
for i in range(num):
    list1.append(input())

def arrange_it(num,list1,order):
    for i in range(num):
        if order[i]==min(order):
            if order[i]==i+1:
                print(list1[i])
            else:
                if len(list1[i])==order[i]:
                    print(list1[i].upper())
                else:
                    print(list1[i].lower())
            return i
            break
                
for i in range(num):
    p=arrange_it(num,list1,order)
    order[p]=num+1