#给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

#你可以按任意顺序返回答案。

#示例 1：

#输入：["bella","label","roller"]
#输出：["e","l","l"]

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/find-common-characters
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        word = A[0]
        hash_m = [0] * 26
        for w in word:
            hash_m[ord(w) - 97] += 1

        hash_1 = hash_m[:]
        num = len(A)
        for i in range(1,num):
            hash_m_n = [0] * 26
            for c in A[i]:
                hash_m_n[ord(c) - 97] += 1
            for i in range(26):
                hash_1[i] = min(hash_1[i],hash_m_n[i])
        
        result = []
        for i in range(26):
            while hash_1[i] != 0:
                result.append(chr(i + 97))
                hash_1[i] -= 1

        return result

a = Solution()
print(a.commonChars(["cool","lock","cook"]))