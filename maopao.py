"""冒泡排序"""


def bubble_sort(nums: list[float]) -> list[float]:
    arr = list(nums)
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
