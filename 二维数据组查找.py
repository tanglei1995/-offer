class Solution:
    # array 二维列表
    def Find(self, target, array):
        n = len(array)
        for i in range(n):
            if target in array[i]:
                return True
        return False


s = Solution()
arr = [[1, 3, 5, 7],
       [2, 4, 6, 8],
       [3, 5, 7, 9],
       [4, 6, 8, 10]]
tar = 11
print(s.Find(tar, arr))