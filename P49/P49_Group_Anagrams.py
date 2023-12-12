class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        return_dict = dict()
        for word in strs:
            tmp_str = "".join(sorted(word))
            if not tmp_str in return_dict:
                return_dict[tmp_str] = [word]
            else:
                return_dict[tmp_str].append(word)
        return list(return_dict.values())








    def isAnagram(self, s: str, t: str) -> bool:
        str_1 = "".join(sorted(s))
        str_2 = "".join(sorted(t))
        return True if (str_1==str_2) else False
