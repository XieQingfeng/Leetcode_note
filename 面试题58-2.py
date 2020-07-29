#字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

#示例 1:

#输入: s = "abcdefg", k = 2
#输出: "cdefgab"

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        result = []
        for i in range(n,len(s)):
            result.append(s[i])
        for i in range(n):
            result.append(s[i])
        return ''.join(result)

a = Solution()
print(a.reverseLeftWords('abcdefg',2))