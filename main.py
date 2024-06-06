def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))

    unique_in_list1 = list(set(list1) - set(list2))

    unique_in_list2 = list(set(list2) - set(list1))

    return common_elements, unique_in_list1, unique_in_list2

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common, unique1, unique2 = compare_lists(list1, list2)

print("Общие элементы:", common)
print("Уникальные элементы из первого списка:", unique1)
print("Уникальные элементы из второго списка:", unique2)
