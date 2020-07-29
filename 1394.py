#在整数数组中，如果一个整数的出现频次和它的数值大小相等，我们就称这个整数为「幸运数」。

#给你一个整数数组 arr，请你从中找出并返回一个幸运数。

#如果数组中存在多个幸运数，只需返回 最大 的那个。
#如果数组中不含幸运数，则返回 -1 。
#示例 1：

#输入：arr = [2,2,3,4]
#输出：2
#解释：数组中唯一的幸运数是 2 ，因为数值 2 的出现频次也是 2 。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/find-lucky-integer-in-an-array
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hash_m = [0] * (max(arr) + 1)
        for i in arr:
            hash_m[i] += 1
        
        print(hash_m)
        num = -1
        for i in range(1,max(arr)+1):
            if i == hash_m[i]:
                num = i 

        return num

a = Solution()
print(a.findLucky([1,2,2,3,3,3]))