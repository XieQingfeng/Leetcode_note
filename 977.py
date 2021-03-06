#给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

#示例 1：

#输入：[-4,-1,0,3,10]
#输出：[0,1,9,16,100]

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = [i*i for i in A]
        B.sort()
        return B

a = Solution()
print(a.sortedSquares([-4,-1,0,3,10]))