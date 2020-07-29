#给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

#请返回 nums 的动态和。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/running-sum-of-1d-array
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#示例 1：
#输入：nums = [1,2,3,4]
#输出：[1,3,6,10]
#解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = []
        for i in range(len(nums)):
            sum = 0
            j = 0
            while j <= i:
                sum += nums[j]
                j = j + 1
            num.append(sum)
        return num

a = Solution()
print(a.runningSum([1,2,3]))