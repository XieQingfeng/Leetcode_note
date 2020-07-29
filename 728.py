#自除数 是指可以被它包含的每一位数除尽的数。

#例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

#还有，自除数不允许包含 0 。

#给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

#示例 1：

#输入： 
#上边界left = 1, 下边界right = 22
#输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/self-dividing-numbers
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isselfDivid(num):
            l = []
            n = num
            while num != 0:
                l.append(num % 10)
                num = num // 10
            print(l)
            if 0 in l:
                return False
            flag = True
            print(l)
            for i in range(len(l)):
                print(n % l[i])
                if n % l[i] != 0:
                    flag = False
            return flag

        result = []
        for num in range(left,right+1):
            if isselfDivid(num) == True:
                result.append(num)

        return result 

a = Solution()
print(a.selfDividingNumbers(1,22))