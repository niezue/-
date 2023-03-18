import random


def partition(li, left, right):  # 选取一个数置于整个数列的中间，左右分别是小于以及大于它的数，再对左右进行同等进行
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def serect(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        serect(li, left, mid - 1)
        serect(li, mid + 1, right)


def t(li):
    serect(li, 0, len(a) - 1)


a = list(i for i in range(50000))
random.shuffle(a)
t(a)
print(a)
