import random
def partition(arr, low, high):
  
    pivot = arr[high]  # опорный элемент — последний
    i = low - 1        # индекс меньшего элемента

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # ставим pivot на правильную позицию
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    """
    Быстрая сортировка с рандомизацией.
    """
    if low < high:
        # 1. Выбираем случайный индекс
        random_index = random.randint(low, high)
        # 2. Меняем его с последним элементом
        arr[random_index], arr[high] = arr[high], arr[random_index]
        # 3. Делим массив
        pivot_index = partition(arr, low, high)
        # 4. Сортируем левую часть
        quick_sort(arr, low, pivot_index - 1)
        # 5. Сортируем правую часть
        quick_sort(arr, pivot_index + 1, high)

nums = [10, 7, 8, 9, 1, 5]
quick_sort(nums, 0, len(nums) - 1)
print(nums)