#给你一个字符串 s ，请你根据下面的算法重新构造字符串：

#从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
#从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
#重复步骤 2 ，直到你没法从 s 中选择字符。
#从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
#从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
#重复步骤 5 ，直到你没法从 s 中选择字符。
#重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
#在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

#请你返回将 s 中字符重新排序后的 结果字符串 。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/increasing-decreasing-string
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def sortString(self, s: str) -> str:
        h = [0] * 26
        for ch in s:
            h[ord(ch) - 97] += 1

        def appendChar(ret, p):
            if h[p] > 0:
                h[p] -= 1
                ret.append(chr(p + 97))
        
        def haveChar():
            return any(h[i] > 0 for i in range(26))
        
        ret = list()
        while True:
            if not haveChar():
                break
            for i in range(26):
                appendChar(ret, i)
            for i in range(26):
                appendChar(ret, 25 - i)
        return "".join(ret)

a = Solution()
print(a.sortString("aaaabbbbcccc"))