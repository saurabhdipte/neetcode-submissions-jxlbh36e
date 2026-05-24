# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(node,value):
            nonlocal count
           
            if node.val>=value:
                count+=1
            value=max(value,node.val)
            if node.left:
                dfs(node.left,value)
            if node.right:
                dfs(node.right,value)
            
        dfs(root,float("-inf"))
        return count

