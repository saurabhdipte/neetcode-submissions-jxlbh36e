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
                dfs(node.left,max(node.val,value))
            if node.right:
                dfs(node.right,max(node.val,value))
            
        dfs(root,float("-inf"))
        return count

