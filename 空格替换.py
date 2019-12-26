class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        count=len(s)
        for i in range(0,count):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)

def main():
    Str = input("请输入：\n")
    s = Solution()
    print(s.replaceSpace(Str))
if __name__ == '__main__':
    main()
