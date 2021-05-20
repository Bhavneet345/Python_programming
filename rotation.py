def rotation(arr,n):
    l=[]
    for i in range(1,n+1):
        j=0
        ch=arr.pop(j)
        l.append(ch)
    for elements in l:
        arr.append(elements)
    print(f"New array: {arr}")
arr=[]
n=int(input("Enter how many elements you want in your array-"))
for i in range(1,n+1):
    arr.append(int(input()))
num=int(input("Enter the number of elements you want to change-"))
rotation(arr,num)


