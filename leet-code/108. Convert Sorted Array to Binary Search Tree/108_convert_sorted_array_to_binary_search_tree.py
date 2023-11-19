class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_to_bst(self, nums):
        if not nums:
            return None

        half = len(nums) // 2
        root = TreeNode(nums[half])
        root.left = self.sorted_array_to_bst(nums[:half])
        root.right = self.sorted_array_to_bst(nums[half + 1:])
        return root


solution = Solution()
solution.sorted_array_to_bst([-10, -3, 0, 5, 9])
