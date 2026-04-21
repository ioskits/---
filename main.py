def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    print("=== СОРТИРОВКА ПУЗЫРЬКОМ ===")
    user_input = input("введи числа через пробел: ")
    
    try:
        numbers = [int(x) for x in user_input.split()]
    except:
        print("ты дурак? числа введи")
        return
    
    print(f"было: {numbers}")
    sorted_numbers = bubble_sort(numbers.copy())
    print(f"стало: {sorted_numbers}")
    
    if numbers == sorted_numbers:
        print("уже было отсортировано. зачем ты меня вызвал?")

if __name__ == "__main__":
    main()
