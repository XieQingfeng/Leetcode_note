# 893.特殊等价字符串组
# 你将得到一个字符串数组 A。

#每次移动都可以交换 S 的任意两个偶数下标的字符或任意两个奇数下标的字符。

#如果经过任意次数的移动，S == T，那么两个字符串 S 和 T 是 特殊等价 的。

#例如，S = "zzxy" 和 T = "xyzz" 是一对特殊等价字符串，因为可以先交换 S[0] 和 S[2]，然后交换 S[1] 和 S[3]，使得 "zzxy" -> "xzzy" -> "xyzz" 。

#现在规定，A 的 一组特殊等价字符串 就是 A 的一个同时满足下述条件的非空子集：

#该组中的每一对字符串都是 特殊等价 的
#该组字符串已经涵盖了该类别中的所有特殊等价字符串，容量达到理论上的最大值（也就是说，如果一个字符串不在该组中，那么这个字符串就 不会 与该组内任何字符串特殊等价）
#返回 A 中特殊等价字符串组的数量。

#示例 1：

#输入：["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
#输出：3
#解释：
#其中一组为 ["abcd", "cdab", "cbad"]，因为它们是成对的特殊等价字符串，且没有其他字符串与这些字符串特殊等价。
#另外两组分别是 ["xyzz", "zzxy"] 和 ["zzyx"]。特别需要注意的是，"zzxy" 不与 "zzyx" 特殊等价。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/groups-of-special-equivalent-strings
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if A == []:
            return 0

        sumer = 0
        for i in range(len(A)):
            if A[i] == '':
                continue

            sumer += 1
            odd_1 = []
            even_1 = []
            string = A[i]
            for m in range(len(string)):
                if m % 2 == 0:
                    even_1.append(string[m])
                else:
                    odd_1.append(string[m])
            
            for j in range(i+1,len(A)):
                if A[j] == '':
                    continue
                odd_2 = []
                even_2 = []
                string_2 = A[j]
                for k in range(len(string_2)):
                    if k % 2 == 0:
                        even_2.append(string_2[k])
                    else:
                        odd_2.append(string_2[k])

                odd_1.sort()
                odd_2.sort()
                even_1.sort()
                even_2.sort()
                if odd_1 == odd_2 and even_1 == even_2:
                    A[j] = ''
            
        return sumer                

a = Solution()
print(a.numSpecialEquivGroups(["ababaa","aaabaa"]))