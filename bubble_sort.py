a = [5,7,4,3,8,2]


def bubble_sort(arr):
    n = len(arr)
    count = 0
    for run in range(n-1):
        for idx in range(n-1-run):
        #print(f'now compare {arr[idx]} with {arr[idx+1]}')
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                count += 1
    print(f'substitutions: {count}')
    print()
    return arr


print(bubble_sort(a))