

def QuickSort(line):
    num = len(line)
    low = 1 # 0 as pivot
    high = num -1
    pivot = low-1
    if low > high: return line
    while(low > high):
        while()
        if line[low] < line[pivot]: low += 1
        if line[pivot] < line[high]: high -= 1




    return QuickSort(line[0:])+QuickSort(line[:-1])

def quickSort(array):
    if len(array) < 2:# 基线条件（停止递归的条件）
        return array
    else:  # 递归条件
        baseValue = array[0]  # 选择基准值# 由所有小于基准值的元素组成的子数组
        less = [m for m in array[1:] if m < baseValue]# 包括基准在内的同时和基准相等的元素，在上一个版本的百科当中，并没有考虑相等元素
        equal = [w for w in array if w == baseValue]# 由所有大于基准值的元素组成的子数组
        greater = [n for n in array[1:] if n > baseValue]
        return quickSort(less) + equal + quickSort(greater)


if __name__ == '__main__':
    numbers = 10
    result = [1,2,5,8,9,0,4,6,7,3]
    QuickSort(result)
