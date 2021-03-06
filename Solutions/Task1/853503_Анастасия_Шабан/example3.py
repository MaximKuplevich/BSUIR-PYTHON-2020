import random


def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        quick_sort(array, begin, pivot - 1)
        quick_sort(array, pivot + 1, end)

    return quick_sort(array, begin, end)


def quick_sort_func(file_name):
    with open(file_name, "r") as file:
        L = list(map(int, file.read().split(" ")))
    quick_sort(L)
    print("Быстрая сортировка")
    print(L)
