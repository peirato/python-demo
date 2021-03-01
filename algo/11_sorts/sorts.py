"""
    Bubble sort, insertion sort and selection sort
    冒泡排序、插入排序、选择排序

    Author: Wenru
"""
from typing import List


# 冒泡排序
def bubble_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        made_swap = False
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                made_swap = True
        if not made_swap:
            break


# def insertion_sort(a: List[int]):
#     length = len(a)
#     if length <= 1:
#         return
#
#     # 已排序区间和未排序区间的分割下标，也是下次要插入的元素下标
#     index = 1
#
#     for i in range(length - 1):
#         # 要排序的元素
#         current = a[index]
#         # 计算插入位置 遍历已排序区间
#         insert_index = index
#         for j in range(0, index):
#             # 计算要插入的位置
#             if current < a[j]:
#                 insert_index = j
#                 break
#         a.pop(index)
#         a.insert(insert_index, current)
#         index = index + 1

# 插入排序
def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(1, length):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


# 选择排序
def selection_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(0, length):
        # 找到最小的
        min_idx = i
        for j in range(i, length):
            if a[j] < a[min_idx]:
                min_idx = j

        # 交换
        a[i], a[min_idx] = a[min_idx], a[i]
        while min_idx > i:
            a[min_idx - 1], a[min_idx] = a[min_idx], a[min_idx - 1]
            min_idx -= 1


def test_bubble_sort():
    test_array = [1, 1, 1, 1]
    bubble_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_insertion_sort():
    test_array = [1, 1, 1, 1]
    insertion_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    insertion_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    insertion_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_selection_sort():
    test_array = [1, 1, 1, 1]
    selection_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insertion_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    selection_sort(array)
    print(array)

    test_bubble_sort()
    test_insertion_sort()
    test_selection_sort()
