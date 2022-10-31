def bubble_sort(arr):
    is_sorted = False
    while is_sorted == False:
        is_sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False

    return arr


test_case = [5,8,1,0]
print(bubble_sort(test_case))