def bubble_sort(arr):
    l1 = len(arr)
    for i in range(1, l1):
        for j in range(0, l1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print("Sorted array is-")
    for i in range(0, l1):
        print(arr[i], end=" ")


if __name__ == '__main__':
    arr1 = []
    n = int(input("Enter the size of array:"))
    print("Enter the elements")
    for k in range(0, n):
        arr1.append(int(input()))
    bubble_sort(arr1)
