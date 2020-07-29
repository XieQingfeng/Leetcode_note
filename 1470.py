#给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

#请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

#示例 1：

#输入：nums = [2,5,1,3,4,7], n = 3
#输出：[2,3,5,4,1,7] 
#解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/shuffle-the-array
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result = []
        
        index_x = 0
        index_y = n

        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(nums[index_x])
                index_x = index_x + 1
            else:
                result.append(nums[index_y])
                index_y = index_y + 1

        return result

a = Solution()
print(a.shuffle([2,5,1,3,4,7],3))