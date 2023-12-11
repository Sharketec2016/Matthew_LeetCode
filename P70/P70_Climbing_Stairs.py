class Solution:
    def climbStairs(self, n: int) -> int:

        return self.recursion(n=n, ans = dict())

    def recursion(self, n, ans):
        if n == 0:
            return 1
        elif n == -1:
            return 0
        if n not in ans:
            ans[n] = self.recursion(n-1, ans) + self.recursion(n-2, ans)
        return ans[n]