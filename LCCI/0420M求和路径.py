#给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。
#设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。
#注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

#My:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        #用栈遍历树，对树的每个结点调用helper
        count=0
        if root is None:
            return 0
        queue=[root]
        while queue:
            r=queue[0]
            queue=queue[1:]
            count+=self.helper(r,sum)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
        return count


    def helper(self,root,sum):
        #从某一个结点往下找
        #需要递归
        if root.left is None and root.right is None:  #到达叶节点
            if root.val==sum:
                return 1
            else:
                return 0
        count=0
        if root.val==sum:
            count+=1
        if root.left:
            count+=self.helper(root.left,sum-root.val)
        if root.right:
            count+=self.helper(root.right,sum-root.val)
        return count

#其他
#法1：在我的上面优化,先计算包含根节点的情况，在递归求解不包含根节点的左右子树，统计相加即可。
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def path(self, root, sum):
        if not root:
            return 0
        res = 0
        if root.val == sum:
            res += 1
        res += self.path(root.left, sum - root.val)
        res += self.path(root.right, sum - root.val)
        return res

#法2：前缀和，递归，回溯
#前缀和。就是到达当前元素的路径上，之前所有元素的和。
#如果两个数的前缀总和是相同的，那么这些节点之间的元素总和为零。
#进一步扩展相同的想法，如果前缀总和currSum，在节点A和节点B处相差target，则位于节点A和节点B之间的元素之和是target
#因为本题中的路径是一棵树，从根往任一节点的路径上(不走回头路)，有且仅有一条路径，因为不存在环。(如果存在环，前缀和就不能用了，需要改造算法)

#抵达当前节点(即B节点)后，将前缀和累加，然后查找在前缀和上，有没有前缀和currSum-target的节点(即A节点)，
#存在即表示从A到B有一条路径之和满足条件的情况。结果加上满足前缀和currSum-target的节点的数量。然后递归进入左右子树。

#左右子树遍历完成之后，回到当前层，需要把当前节点添加的前缀和去除。
#避免回溯之后影响上一层。因为思想是前缀和，不属于前缀的，我们就要去掉它。
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int pathSum(TreeNode root, int sum) {
        // key是前缀和, value是大小为key的前缀和出现的次数
        Map<Integer, Integer> prefixSumCount = new HashMap<>();
        // 前缀和为0的一条路径
        prefixSumCount.put(0, 1);
        // 前缀和的递归回溯思路
        return recursionPathSum(root, prefixSumCount, sum, 0);
    }

    /**
     * 前缀和的递归回溯思路
     * 从当前节点反推到根节点(反推比较好理解，正向其实也只有一条)，有且仅有一条路径，因为这是一棵树
     * 如果此前有和为currSum-target,而当前的和又为currSum,两者的差就肯定为target了
     * 所以前缀和对于当前路径来说是唯一的，当前记录的前缀和，在回溯结束，回到本层时去除，保证其不影响其他分支的结果
     * @param node 树节点
     * @param prefixSumCount 前缀和Map
     * @param target 目标值
     * @param currSum 当前路径和
     * @return 满足题意的解
     */
    private int recursionPathSum(TreeNode node, Map<Integer, Integer> prefixSumCount, int target, int currSum) {
        // 1.递归终止条件
        if (node == null) {
            return 0;
        }
        // 2.本层要做的事情
        int res = 0;
        // 当前路径上的和
        currSum += node.val;

        //---核心代码
        // 看看root到当前节点这条路上是否存在节点前缀和加target为currSum的路径
        // 当前节点->root节点反推，有且仅有一条路径，如果此前有和为currSum-target,而当前的和又为currSum,两者的差就肯定为target了
        // currSum-target相当于找路径的起点，起点的sum+target=currSum，当前点到起点的距离就是target
        res += prefixSumCount.getOrDefault(currSum - target, 0);
        // 更新路径上当前节点前缀和的个数
        prefixSumCount.put(currSum, prefixSumCount.getOrDefault(currSum, 0) + 1);
        //---核心代码

        // 3.进入下一层
        res += recursionPathSum(node.left, prefixSumCount, target, currSum);
        res += recursionPathSum(node.right, prefixSumCount, target, currSum);

        // 4.回到本层，恢复状态，去除当前节点的前缀和数量
        prefixSumCount.put(currSum, prefixSumCount.get(currSum) - 1);
        return res;
    }
}


