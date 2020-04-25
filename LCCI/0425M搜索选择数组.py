#搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。
#请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。
 
#二分法?先排序再查找？
#My:python 偷懒法
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if target in set(arr):
            return arr.index(target)
        else:
            return -1

#其他：
#真的用二分法也
#对于能判断升序区间的情况，根据目标值的大小移动边界。
#对于不能判断升序区间的情况，需要逐步清除重复值。
#没有重复值的最优情况时间复杂度是O(log N)，全部或几乎全部是重复值的最差情况时间复杂度是O(N)。
'''
                                   nums[left] <= target  
                              ┌─  && target <= nums[mid]   ──>  right = mid                
                              │   （目标在左边的升序区间中）         （右边界移动到mid）
  ┌─  nums[left] < nums[mid] ─┼
  │     （左边区间升序）         │
  │                           └─    否则目标在右半边          ──>  left = mid + 1
  │                                                             （左边界移动到mid+1）
  │               
  │                                 nums[left] <= target  
  │                           ┌─  || target <= nums[mid]   ──>  right = mid              
  │                           │    （目标在左半边）                （右边界移动到mid）
 ─┼─  nums[left] > nums[mid] ─┼     
  │     （左边不是升序）         │
  │                           └─    否则目标在右半边          ──>  left = mid + 1 
  │                                                              （左边界移动到mid+1）
  │               
  │                             
  │                           ┌─   nums[left] != target    ──>  left++                
  │                           │     （左值不等于目标               （需要逐一清理重复值）        
  └─ nums[left] == nums[mid] ─┼         说明还没找到）
      （可能是已经找到了目标      │
        也可能是遇到了重复值）    └─   nums[left] == target    ──>  right = left
                                    （左值等于目标                 （将右边界移动到left，循环结束）
                                      已经找到最左边的目标值）
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:                                         # 循环结束条件left==right
            mid = (left + right) >> 1
            if nums[left] < nums[mid]:                              # 如果左值小于中值，说明左边区间升序 
                if nums[left] <= target and target <= nums[mid]:    # 如果目标在左边的升序区间中，右边界移动到mid
                    right = mid
                else:                                               # 否则目标在右半边，左边界移动到mid+1
                    left = mid + 1
            elif nums[left] > nums[mid]:                            # 如果左值大于中值，说明左边不是升序，右半边升序
                if nums[left] <= target or target <= nums[mid]:     # 如果目标在左边，右边界移动到mid
                    right = mid
                else:                                               # 否则目标在右半边的升序区间中，左边界移动到mid+1
                    left = mid + 1
            elif nums[left] == nums[mid]:                           # 如果左值等于中值，可能是已经找到了目标，也可能是遇到了重复值
                if nums[left] != target:                            # 如果左值不等于目标，说明还没找到，需要逐一清理重复值
                    left += 1                                        
                else:                                               # 如果左值等于目标，说明已经找到最左边的目标值
                    right = left                                    # 将右边界移动到left，循环结束
        return left if nums[left] == target else -1                 # 返回left，或者-1

