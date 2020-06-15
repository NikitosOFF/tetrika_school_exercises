def search_pairs(array, k):
    result = []

    array = list(set(array))
    if k % 2 == 0 and k // 2 in array:
        array.append(k // 2)

    for i, num in enumerate(array):
        for j, _ in enumerate(array):
            if j > i:
                summa = num + array[j]
                if summa == k:
                    result.append((num, array[j]))
    return result


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 2], 5))
