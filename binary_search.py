# code your iterative algorithm here

list = [5, 8, 12, 14, 19, 22, 27, 30 , 31]

def binary_search(data, el):
    first = 0
    last = len(data)-1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if data[mid] == el:
            found = True
        else:
            if el < data[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

print(binary_search(list, 12))