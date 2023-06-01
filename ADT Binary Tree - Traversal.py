import collections

"""
in this ADT, every node of the tree is initialized in Node class, which follows the rules of Leetcode
Add_element function will help to build a complete binary tree, but it's slow O(n)
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add_element(self, new_node_value):
        # this is a function to build complete binary tree
        # but this is slow
        node = Node(new_node_value)
        if not self.root:
            self.root = node
            return
        q = collections.deque([self.root])  # FIFO
        while True:
            pop_node = q.popleft()
            if pop_node.left:
                q.append(pop_node.left)
            else:
                pop_node.left = node
                return
            if pop_node.right:
                q.append(pop_node.right)
            else:
                pop_node.right = node
                return

    def bfs(self, node=None):
        #  if default node, bfs function will start from tree's root
        #  else: bfs will start from any node that we give
        if not node:
            node = self.root
            if not node:
                return
        q = collections.deque([node])
        while q:
            pop_node = q.popleft()
            print(pop_node.val, end=' ')
            if pop_node.left:
                q.append(pop_node.left)
            if pop_node.right:
                q.append(pop_node.right)

    def dfs_preorder_re(self, node):
        if not node:
            return
        print(node.val, end=' ')
        self.dfs_preorder_re(node.left)
        self.dfs_preorder_re(node.right)

    def dfs_inorder_re(self, node):
        if not node:
            return
        self.dfs_inorder_re(node.left)
        print(node.val, end=' ')
        self.dfs_inorder_re(node.right)

    def dfs_postorder_re(self, node):
        if not node:
            return
        self.dfs_postorder_re(node.left)
        self.dfs_postorder_re(node.right)
        print(node.val, end=' ')

    def dfs_preorder_it(self, node=None):
        if not node:
            node = self.root
            if not node:
                return
        stack = [node]
        # quite similar with bfs but what's important is that right goes into stack first
        while stack:
            pop_node = stack.pop()
            print(pop_node.val, end=' ')
            if pop_node.right:
                stack.append(pop_node.right)  # right child first because of stack
            if pop_node.left:
                stack.append(pop_node.left)

    def dfs_inorder_it(self, node=None):
        if not node:
            node = self.root
            if not node:
                return
        stack = []  # 唯一一种开始不将node放入stack的function
        cur = node  # pointer
        while cur or stack:  # cur 在此处只为第一轮能进入循环
            while cur:
                stack.append(cur)
                cur = cur.left  # 必须找到最左边的节点
            pop_node = stack.pop()
            print(pop_node.val, end=' ')
            cur = pop_node.right  # 再检查其有没有右节点，有的话循环加入

    def dfs_postorder_it(self, node=None):
        # 常用的有两种方法：
        # 第一种，postorder是preorder的反向，所以可以将postorder的结果放在list中，按照preorder操作，最后reverse list
        # 第二种，每次将node推进stack两次，第一个推进的用作遍历其子树，第二个推进的树用来打印
        if not node:
            node = self.root
            if not node:
                return
        stack = [node]  # 2
        while stack:
            pop_node = stack.pop()
            if stack and pop_node == stack[-1]:
                if pop_node.right:
                    stack.append(pop_node.right)
                    stack.append(pop_node.right)
                if pop_node.left:
                    stack.append(pop_node.left)
                    stack.append(pop_node.left)
            else:
                print(pop_node.val, end=' ')

    def morris_inorder_it(self, node=None):
        # 一种不使用栈的方法来遍历二叉树，空间复杂度为O(1)
        if not node:
            node = self.root
            if not node:
                return
        cur = node
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right, cur = cur, cur.left
                    continue
                prev.right = None
            print(cur.val, end=' ')
            cur = cur.right
    # Morris遍历会修改树的结构，因此如果在遍历过程中需要保持树的原始结构，建议使用其他遍历方法。


"""
          1
       2    3
     4  5  6  7
"""
tree = Tree()
tree.add_element(1)
tree.add_element(2)
tree.add_element(3)
tree.add_element(4)
tree.add_element(5)
tree.add_element(6)
tree.add_element(7)
# tree.bfs()
# tree.dfs_preorder_re(tree.root)
# tree.dfs_inorder_re(tree.root)
# tree.dfs_postorder_re(tree.root)
# tree.dfs_preorder_it(tree.root)
# tree.dfs_inorder_it(tree.root)
# tree.dfs_preorder_it(tree.root)
tree.morris_inorder_it(tree.root)


# n = Node(1)
# n.left = Node(2)
# n.right = Node(3)
# n.left.left = Node(4)
# n.left.right = Node(5)
# n.right.left = Node(6)
# n.right.right = Node(7)
# t = Tree()
# t.bfs(n)
# t.dfs_preorder_re(n)
