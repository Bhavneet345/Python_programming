number = int(input("How many numbers you want to enter to check palindrome:"))
list1 = []
for i in range(number):
    list1.append(input())
for i in range(0, len(list1)):
    num = int(list1[i])
    while True:
        num = num + 1
        new = str(num)
        reverse = new[::-1]
        if new == reverse:
            print(f"next palindrome of {list1[i]}:{new}")
            break
    continue


