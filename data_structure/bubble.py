import heapq

def bubble_sort(arr):
    n = len(arr)
    cnt = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n-i-1):
            cnt += 1

            if arr[j] > arr[j+1]:
                swaps += 1

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return cnt, swaps


size = 1000
unsorted_list = list(range(size, 0, -1))

swaps = bubble_sort(unsorted_list.copy())
no_swaps = bubble_sort(sorted(unsorted_list.copy()))

print(f"리스트 크기 : {size}")
print(f"자리 바꿈o: {swaps}")
print(f"자리 바꿈x: {no_swaps}")