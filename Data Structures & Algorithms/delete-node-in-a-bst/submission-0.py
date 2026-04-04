# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node):
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        #to find the max in the left subtree
        curr=node
        left=node.left
        right=node.right
        while left.right:
            left=left.right
        left.right=right
        return curr.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val==key:
            return self.helper(root)
        curr=root
        while root:
            if key<root.val:
                if root.left and root.left.val==key:
                    root.left=self.helper(root.left)
                    break
                root=root.left
            else:
                if root.right and root.right.val==key:
                    root.right=self.helper(root.right)
                    break
                root=root.right
        return curr
                    
