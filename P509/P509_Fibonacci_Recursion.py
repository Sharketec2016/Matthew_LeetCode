
class Solution:
    def fib(self, n: int) -> int:
       return self.recursion(n, dict())

    def recursion(self, n, ans):
        if n in ans:
            return ans[n]
        elif n==0:
            return 0
        elif n==1:
            return 1
        ans[n] = self.recursion(n-1, ans) + self.recursion(n-2, ans)
        return ans[n]




