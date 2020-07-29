#给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

#示例 1：

#输入: "babad"
#输出: "bab"
#注意: "aba" 也是一个有效答案。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/longest-palindromic-substring
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s

        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        max_len = 1
        start = 0

        for j in range(n):
            for i in range(0,i):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]


a = Solution()
print(a.longestPalindrome("babad"))