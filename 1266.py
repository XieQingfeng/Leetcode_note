
#面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。请你计算访问所有这些点需要的最小时间（以秒为单位）。

#你可以按照下面的规则在平面上移动：

#每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
#必须按照数组中出现的顺序来访问这些点。

#输入：points = [[1,1],[3,4],[-1,0]]
#输出：7
#解释：一条最佳的访问路径是： [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
#从 [1,1] 到 [3,4] 需要 3 秒 
#从 [3,4] 到 [-1,0] 需要 4 秒
#一共需要 7 秒

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/minimum-time-visiting-all-points
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x0, x1 = points[0]
        ans = 0
        for i in range(1, len(points)):
            y0, y1 = points[i]
            ans += max(abs(x0 - y0), abs(x1 - y1))
            x0, x1 = points[i]
        return ans

a = Solution()
print(a.minTimeToVisitAllPoints([[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]))