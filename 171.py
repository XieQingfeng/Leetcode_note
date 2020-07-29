#给定一个Excel表格中的列名称，返回其相应的列序号。

#例如，
#    A -> 1
#    B -> 2
#    C -> 3
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28 
#    ...
#示例 1:

#输入: "A"
#输出: 1

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/excel-sheet-column-number
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 1:
            return (ord(s) - 65 + 1)
        else:
            sumer = 0
            for n in s:
                sumer += (ord(n) - 65 + 1) * (26 ** (length - 1))
                length = length - 1
            return sumer

a = Solution()
print(a.titleToNumber("AAA"))