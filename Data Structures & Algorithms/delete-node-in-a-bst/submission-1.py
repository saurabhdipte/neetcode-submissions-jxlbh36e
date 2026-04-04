# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        cur=node
        left=node.left
        right=node.right
        while left.right:
            left=left.right
        left.right=right
        return cur.left
        



    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val==key:
            return self.helper(root)
        cur=root
        while root:
            if val<root.val:
                if root.left and root.left.val==key:
                    root.left=self.helper(root.left)
                else:
                    root=root.left
            else:
                if root.right and root.right.val==key:
                    root.right=self.helper(root.right)
                else:
                    root=root.right
        return cur