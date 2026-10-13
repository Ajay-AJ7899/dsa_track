class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = self.findInorderSuccessor(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root

    def findInorderSuccessor(self, node: TreeNode) -> TreeNode:
        while node.left is not None:
            node = node.left
        return node