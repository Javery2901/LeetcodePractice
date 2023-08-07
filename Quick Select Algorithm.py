"""
Quickselect is a selection algorithm to find the kth smallest element in an unordered list
Instead of recursing into both sides, as in quicksort,
Quickselect only recurses into one side – the side with the element it is searching for.
Time complexity: average O(n) (comparing to O(nlogn) with quicksort), worst O(n^2) ()
However, for randomly chosen pivots, this worst case is very unlikely
"""

# The code here is to find the kth biggest element, which is the (len(ls) - k)th smallest element


def quick_select(ls, k):
    return quick_select_helper(0, len(ls) - 1, k - 1)
    # k - 1 means the kth smallest number


def quick_select_helper(l, r, kth_index):
    if l == r:
        return ls[l]
    pivot_index = partition(l, r, l)  # start from ls[0]
    # pivot_index means, after the function partition, the left side of ls will be all smaller
    # and the right side of ls will be all bigger
    # in this way we check if pivot_index is the one we want (kth_index)
    if pivot_index == kth_index:
        return ls[pivot_index]

    if pivot_index < kth_index:
        return quick_select_helper(pivot_index + 1, r, kth_index)
    else:
        return quick_select_helper(l, pivot_index - 1, kth_index)


def partition(l, r, pivot):  # this is very similar with quick sort, but return index
    pivot_elem = ls[pivot]
    ls[r], ls[pivot] = ls[pivot], ls[r]

    index = l
    for i in range(l, r):
        if ls[i] < pivot_elem:
            ls[i], ls[index] = ls[index], ls[i]
            index += 1
    ls[index], ls[r] = ls[r], ls[index]
    return index


ls = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(quick_select(ls, k))
