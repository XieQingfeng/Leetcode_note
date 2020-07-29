#一个网站域名，如"discuss.leetcode.com"，包含了多个子域名。作为顶级域名，常用的有"com"，下一级则有"leetcode.com"，最低的一级为"discuss.leetcode.com"。当我们访问域名"discuss.leetcode.com"时，也同时访问了其父域名"leetcode.com"以及顶级域名 "com"。

#给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。其格式为访问次数+空格+地址，例如："9001 discuss.leetcode.com"。

#接下来会给出一组访问次数和域名组合的列表cpdomains 。要求解析出所有域名的访问次数，输出格式和输入格式相同，不限定先后顺序。

#示例 1:
#输入: 
#["9001 discuss.leetcode.com"]
#输出: 
#["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
#说明: 
#例子中仅包含一个网站域名："discuss.leetcode.com"。按照前文假设，子域名"leetcode.com"和"com"都会被访问，所以它们都被访问了9001次。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/subdomain-visit-count
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        re = {}

        for domain in cpdomains:
            
            string = domain.split(' ')
            num = int(string[0])

            string_2 = string[1].split('.')
            length = len(string_2)
            
            for i in range(length):
                key = ".".join(string_2[i:])
                if key not in re.keys():
                    re[key] = num
                else:
                    re[key] += num
            
        result = []

        for k,v in re.items():
            result_1 = str(v) + " " + k
            result.append(result_1) 

        return result

a = Solution()
print(a.subdomainVisits(["9001 discuss.leetcode.com"]))