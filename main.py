from custom_quick_sort import custom_quick_sort


def main():
    input_data = input("Enter list of numbers separated by space: ")
    input_list = list(map(lambda x: int(x), input_data.split(" ")))
    print("Entered data is :")
    print(input_list)
    result = custom_quick_sort(input_list)
    print("Sorted result is: ")
    print(result)


if __name__ == "__main__":
    main()
