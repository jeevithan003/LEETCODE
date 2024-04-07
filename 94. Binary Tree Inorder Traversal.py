# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        res += self.inorderTraversal(root.left)
        res += [root.val]
        res += self.inorderTraversal(root.right)
        return res
