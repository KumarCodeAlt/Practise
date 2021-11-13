def custom_quick_sort(input_list):
    length = len(input_list)
    print(length)
    if len(input_list) < 2:
        return input_list
    else:
        lhs_ = []
        rhs_ = []
        pivot = int(length/2)

        for i in range(len(input_list)):
            if i != pivot:
                if input_list[i] <= input_list[pivot]:
                    lhs_.append(input_list[i])
                else:
                    rhs_.append(input_list[i])

        lhs = custom_quick_sort(lhs_)
        rhs = custom_quick_sort(rhs_)
        middle = input_list[pivot]

        return [*lhs, middle, *rhs]
