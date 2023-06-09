def sift(li, low, high):
    i = low
    j = 2 * i - 1
    tmp = li[low]
    while j <= high:  # 堆栈排序 左边2*i+1 右边2*i+2
        if j + 1 <= high and li[j + 1] > li[j]:
            j = j + 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i - 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def hemp(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
    for i in range((n - 2) // 2, -1, -1):
        li[0], li[n - 1] = li[n - 1], li[0]
        sift(li, 0, i - 1)
