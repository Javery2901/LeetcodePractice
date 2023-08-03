'''
stable:An algorithm is said to be stable if it preserves the relative order of equal \
        elements in the input data after sorting.

In-place: An algorithm is said to be in-place if it sorts the input data using only a \
        constant amount of additional memory. In other words, an in-place algorithm does \
        not create a new copy of the input data, but rather modifies the original data \
        in-place to produce the sorted output. 
'''

ls = [1,4,3,9,2,6,7,0,2,4,2,43]
lt = sorted(ls) # [0, 1, 2, 2, 2, 3, 4, 4, 6, 7, 9, 43]
key = 4


'''
binary_search:
import bisect

a = bisect.bisect(lt,key) ->14
b = b=bisect.bisect_right(lt,key) ->14
c = bisect.bisect_left(lt,key) ->10

bisect.bisect, bisect.bisect_left, bisect.bisect_right 均为查找并返回序列号。复杂度O(logn)

bisect.bisect_left: 如果元素已经在序列中，那么该函数返回的是该元素最左侧的位置；\
                    如果元素不在序列中，那么该函数返回的是将该元素插入到序列中时，应该插入的位置
bisect.bisect, bisect.bisect_right: 作用相同
                    如果元素已经在序列中，那么该函数返回的是该元素最右侧的位置 + 1；\
                    如果元素不在序列中，那么该函数返回的是将该元素插入到序列中时，应该插入的位置 \
                    换句话说，i 左侧的元素均小于等于 x，i 右侧的元素均大于 x。
'''
def binary_search_r(lt, key):
    if not lt:
        return False
    middle = (len(lt)-1) // 2
    if key == lt[middle]:
        return True
    if key > lt[middle]:
        return binary_search_r(lt[middle+1:], key)
    if key< lt[middle]:
        return binary_search_r(lt[:middle], key)
##print('binary_search_r(ls, key)', binary_search_r(lt, key))

def binary_search_i(lt, key):
    start = 0
    end = len(lt) - 1
    while start <= end:
        middle = (start + end) // 2
        if key == lt[middle]:
            return True
        elif key > lt[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return False
##print('binary_search_i(ls, key)', binary_search_i(lt, key))


'''
bubble_sort:
    best: O(n) (a sorted list before sorting)
    average: O(n2)
    worst: O(n2) 
    space: 1 (Do not need additional space since it only needs space of original list)
    stable: Yes
    in_place: Yes
'''
def bubble_sort(ls):
    swap_count = 0
    for i in range(len(ls)-1, 0, -1):
        swap = False
        for j in range(1, i+1):
            if ls[j] < ls[j-1]:
                ls[j], ls[j-1] = ls[j-1], ls[j]
                swap_count += 1
                swap = True
        if swap == False:
            return ls, swap_count
    return ls, swap_count
##print('bubble_sort(ls)', bubble_sort(ls))


'''
selection_sort:
    best: O(n2) 
    average: O(n2)
    worst: O(n2) 
    space: 1 (Do not need additional space since it only needs space of original list)
    stable: No
    in_place: Yes
'''
def selection_sort(ls):
    swap_count = 0
    for i in range(len(ls)-1):
        pointer = i
        for j in range(i, len(ls)):
            if ls[j] < ls[pointer]:
                pointer = j
        ls[pointer], ls[i], = ls[i], ls[pointer]
        swap_count += 1
    return ls, swap_count
##print('selection_sort(ls)', selection_sort(ls))


'''
insertion_sort:
    best: O(n) (a sorted list before sorting)
    average: O(n2)
    worst: O(n2) 
    space: 1 (Do not need additional space since it only needs space of original list)
    stable: Yes
    in_place: Yes
'''
def insertion_sort(ls):
    swap_count = 0
    for i in range(1, len(ls)):
        pointer = i
        value = ls[i]
        while pointer > 0 and ls[pointer - 1] > value:
            ls[pointer] = ls[pointer - 1]
            swap_count += 1
            pointer -= 1
        ls[pointer] = value
    return ls, swap_count
####print('insertion_sort(ls)', insertion_sort(ls))


'''
merge_sort:
    best: O(nlogn) (a sorted list before sorting)
    average: O(nlogn)
    worst: O(nlogn) 
    space: O(n) (Do not need additional space since it only needs space of original list)
    stable: Yes
    in_place: No
    
Optimal N-Way Merge Pattern - Greedy Method: why? Consider nlogn
    Always select the smaller size list to merge
    lists: x1, x2, x3, x4, x5
    len:   20, 30, 10, 5,  30
    sort the list based on their len(): x4, x3, x1, x2, x5
        1. merge x4 and x3: cost 15 ->
            lists: x34, x1, x2, x5
            len:   15, 20,  30, 30
           
        2. merge x34 and x1: cost 35 ->
            lists: x2, x5, x134
            len:   30, 30, 35

        3. merge x2 and x5: cost 60 ->
            lists: x134, x25
            len:   35,   60

        4. merge x134 and x25: cost 95 ->
            lists: x12345
'''
def merge_sort_helper(left, right):
    merge = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        elif left[i] > right[j]:
            merge.append(right[j])
            j += 1
    for x in range(i, len(left)):
        merge.append(left[x])
    for y in range(j, len(right)):
        merge.append(right[y])
    return merge
def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    middle = len(ls) //2
    left = merge_sort(ls[:middle])
    right = merge_sort(ls[middle:])
    return merge_sort_helper(left, right)
##print('merge_sort(ls)', merge_sort(ls))


'''
Quick Sort:
    best: nlogn
    average: nlogn
    worst: n2
    space: 1
    stable: No
    in-place: Yes
    There are two ways to improve worst case quick sort:
        1. select middle element as pivot
        2. select random element as pivot (this method is better)
'''
def quick_sort(ls):
    quick_sort_helper(ls, 0, len(ls)-1)
    return ls
def quick_sort_helper(ls, start, end):
    if start >= end:
        return
    splitpoint = partition(ls, start, end)
    quick_sort_helper(ls, start, splitpoint - 1)
    quick_sort_helper(ls, splitpoint + 1, end)
def partition(ls, start, end):
    pivot = ls[start] # in this method, pivot goes from ls[0]
    leftpointer = start +1
    rightpointer = end
    while True:
        while leftpointer <= rightpointer and ls[leftpointer] <= pivot:
            leftpointer += 1
        while rightpointer >= leftpointer and ls[rightpointer] >= pivot:
            rightpointer -= 1
        if rightpointer < leftpointer:
            break
        ls[leftpointer], ls[rightpointer] = ls[rightpointer], ls[leftpointer]
    ls[start], ls[rightpointer] = ls[rightpointer], ls[start]
    return rightpointer
##print('quick_sort(ls)', quick_sort(ls))

'''
Quick Sort2:
    best: nlogn
    average: nlogn
    worst: n2
    space: 1
    stable: No
    in-place: Yes
    There are two ways to improve worst case quick sort:
        1. select middle element as pivot
        2. select random element as pivot (this method is better)
'''
def quick_sort2(ls):
    def aux(start, end):
        if start >= end:
            return
        p_id = partition2(ls, start, end)
        aux(start, p_id)
        aux(p_id + 1, end)
    return aux(0, len(ls))
def partition2(ls, start, end):
    pivot = ls[start]
    p_idx = start + 1
    for i in range(start + 1, end):
        if ls[i] < pivot:
            ls[i], ls[p_idx] = ls[p_idx], ls[i]
            p_idx += 1
    ls[start], ls[p_idx-1] = ls[p_idx-1], ls[start]
    return p_idx-1
##print('quick_sort2(ls)', quick_sort2(ls), ls)
'''
Quick Sort3: 
    best: nlogn
    average: nlogn
    worst: n2 (if lst is already sorted either ascending or descending.)
    space: 1
    stable: No
    in-place: Yes
 
    Optimal 1:
    In the partition(), select the pivot value at the mid of the lst
    Iterate the lst using two pointers
'''
def quick_sort_mid(ls):
    quick_sort_mid_helper(ls, 0, len(ls)-1)
    return ls
def quick_sort_mid_helper(ls, start, end):
    if start >= end:
        return
    splitpointer = partition3(ls, start, end)
    quick_sort_mid_helper(ls, start, splitpointer-1)
    quick_sort_mid_helper(ls, splitpointer + 1, end)
def partition3(ls, start, end):
    mid = (start + end) // 2
    pivot = ls[mid]
    ls[mid],ls[start] = ls[start], ls[mid]
    leftpointer = start +1
    rightpointer = end
    while True:
        while leftpointer <= rightpointer and ls[leftpointer] <= pivot:
            leftpointer += 1
        while rightpointer >= leftpointer and ls[rightpointer] >= pivot:
            rightpointer -= 1
        if rightpointer < leftpointer:
            break
        ls[leftpointer], ls[rightpointer] = ls[rightpointer], ls[leftpointer]
    ls[start], ls[rightpointer] = ls[rightpointer], ls[start]
    return rightpointer
##print('quick_sort_mid(ls)', quick_sort_mid(ls))
'''
Quick Sort3: 
    best: nlogn
    average: nlogn
    worst: nlogn (expected O(nlogn) worst case for All cases)
    space: 1
    stable: No
    in-place: Yes
 
    Optimal 1:
    In the partition(), select the pivot value at the mid of the lst
    Iterate the lst using two pointers
'''
# from Lecture
import random
def quick_sort_random(ls, start, end):
    if start < end:
        splitpointer = start + random.randrange(end-start+1) # set the index of first pivot randomly
        pivot = ls[splitpointer] # our pivot
        ls[start], ls[splitpointer] = ls[splitpointer],ls[start] # put the pivot value at the first in the list
        pointer = start #S1 and S2 are initially empty
        for i in range(start+1, end+1): #explot the whole region
            if ls[i] < pivot or (ls[i] == pivot and random.randrange(2)==0): 
                pointer +=1
                ls[i],ls[pointer]=ls[pointer],ls[i]
                # if any value starting from index start+1 is smaller than pivot value, we put it at the left side
        # if all elemetns that us smaller than pivot value have been put at the left side:
        # we can now put the real pivot value to the position,
        # now all the elements whose value is smaller than pivot have been put at the left side of the pivot      
        ls[start], ls[pointer] = ls[pointer],ls[start]
        quick_sort_random(ls,start,pointer-1) # revursively sort left sublist
        quick_sort_random(ls,pointer+1,end) # revursively sort right sublist
    return ls
print('quick_sort_random(ls,start)', quick_sort_random(ls,0,len(ls)-1))

    





