#给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。
#我的方法：
#执行用时 :52 ms, 在所有 Python3 提交中击败了88.01%的用户   内存消耗 :15.7 MB, 在所有 Python3 提交中击败了100.00%的用户
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        #最中间的肯定是头,截成两组后继续找各组中间的，如此往复递归直至组长度为1
        return self.get_head(nums)

    def get_head(self,nums:List[int]):  
        if len(nums)>1:
            head_idx=int(len(nums)/2)
            head=TreeNode(nums[head_idx])
            left=nums[:head_idx]
            right=nums[head_idx+1:]
            left_Node=self.get_head(left)
            right_Node=self.get_head(right)
            head.left=left_Node
            head.right=right_Node
            return head
        elif len(nums)==1:
            return TreeNode(nums[0])
        else:
            return None

#其他题解：别人写得更简洁
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not len(nums):
            return 
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[: mid])
        root.right = self.sortedArrayToBST(nums[mid + 1: ])
        
        return root 
