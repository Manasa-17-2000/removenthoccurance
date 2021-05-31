a = []
n = int(input("enter the number of elements in list :"))
for x in range (0,n):
    element = input("enter the element"+str(x+1)+":")
    a.append(element)
print(a)
c = []
count = 0
b = input("enter the word to remove : ")
n=int(input("enter the occurence to remove :"))
for i in a:
    if(i == b):
        count += 1
        if count!= n:
            c.append(i)
        else:
            c.append(i)
            if(count == 0):
                print("item not found")
            else:
                print("the number of the repetitions is :", count)
                print("updated list is:",c)
                print("the distinct element are :",set(a))