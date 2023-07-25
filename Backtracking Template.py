"""
所有回溯法的问题都可以抽象为树形结构
for循环可以理解是横向遍历，backtracking（递归）就是纵向遍历，这样就把这棵树全遍历完了，
一般来说，搜索叶子节点就是找的其中一个结果了。
剪枝精髓是：for循环在寻找起点的时候要有一个范围，如果这个起点到集合终止之间的元素已经不够题目要求的k个元素了，就没有必要搜索了。
子集问题分析：

时间复杂度：O(2^n)，因为每一个元素的状态无外乎取与不取，所以时间复杂度为O(2^n)
空间复杂度：O(n)，递归深度为n，所以系统栈所用空间为O(n)，每一层递归所用的空间都是常数级别，注意代码里的result和path都是全局变量，就算是放在参数里，传的也是引用，并不会新申请内存空间，最终空间复杂度为O(n)
排列问题分析：

时间复杂度：O(n!)，这个可以从排列的树形图中很明显发现，每一层节点为n，第二层每一个分支都延伸了n-1个分支，再往下又是n-2个分支，所以一直到叶子节点一共就是 n * n-1 * n-2 * ..... 1 = n!。
空间复杂度：O(n)，和子集问题同理。
组合问题分析：

时间复杂度：O(2^n)，组合问题其实就是一种子集的问题，所以组合问题最坏的情况，也不会超过子集问题的时间复杂度。
空间复杂度：O(n)，和子集问题同理。
N皇后问题分析：

时间复杂度：O(n!) ，其实如果看树形图的话，直觉上是O(n^n)，但皇后之间不能见面所以在搜索的过程中是有剪枝的，最差也就是O（n!），n!表示n * (n-1) * .... * 1。
空间复杂度：O(n)，和子集问题同理。
解数独问题分析：

时间复杂度：O(9^m) , m是'.'的数目。
空间复杂度：O(n^2)，递归的深度是n^2

如何解决重复问题：尽量在for循环中控制index，如前面的index已经遍历过，则不再重新遍历
当for循环可以控制每次递归时的范围时，如循环逐渐缩小，则可以用index来控制
当for循环无法控制每次递归时的范围时，可以考虑用counter计数器

Permutation ( the number of ways to reorder array) time complexity N!
combination ( the number of ways to select from array)
subset/subsequence 2 ** N since each element could be absent or present.
"""

def backtrack(path: list)
    if condition(path):
        # 存放结果
        return

    for item in given_array:  # 树中节点孩子的数量就是array的大小
        # has problem of high space complexity. Normally we can replace path by index
        path.append(item)
        backtrack(path)  # 递归
        path.pop()
    return