# app/merge_sort.py

def insertion_sort(arr, key=lambda x: x):
    for i in range(1, len(arr)):
        key_value = arr[i]
        j = i - 1
        while j >= 0 and key(key_value) < key(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_value

    return result


