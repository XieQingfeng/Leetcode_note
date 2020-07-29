#给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。

#完成所有替换操作后，请你返回这个数组。

#示例：

#输入：arr = [17,18,5,4,6,1]
#输出：[18,6,6,6,1,-1]

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(arr)-1):
            result.append(max(arr[i+1:]))
        result.append(-1)
        return result


a = Solution()
print(a.replaceElements([17,18,5,4,6,1]))