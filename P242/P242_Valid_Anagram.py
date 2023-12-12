class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     s_chars = set(list(s))
    #     t_chars = set(list(t))
    #     if s_chars != t_chars:
    #         return False
    #
    #     s_dict = {char : s.count(char) for char in s_chars}
    #     t_dict = {char : t.count(char) for char in t_chars}
    #
    #
    #     return True if s_dict == t_dict else False


    def isAnagram(self, s: str, t: str) -> bool:
        str_1 = "".join(sorted(s))
        str_2 = "".join(sorted(t))
        return True if (str_1==str_2) else False

