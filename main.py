data = []


def binary_search(lst, number):
    start = lst[0]
    stop = [-1]
    mid = len(lst) // 2
    while True:
        if mid < number:
            data.append(mid)
            start = mid
            mid = (start + stop) // 2
        elif mid > number:
            data.append(mid)
            stop = mid
            mid = (start + mid) // 2
        elif mid == number:
            data.append(mid)
            return "завершено"


print(f"{binary_search(range(1, 101), 45)}\n"
      f"попытки - {data}")

sort_list = []


def buble_sort(lst):
    while len(lst) != 0:
        m = lst.index(min(lst))
        sort_list.append(lst.pop(m))
    return f"отсортированный список - {sort_list}"


print(buble_sort([12, 1, 39, 25, 30, 80, 10]))
