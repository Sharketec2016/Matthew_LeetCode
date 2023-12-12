class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        tmp_dict = dict()

        for num in nums:
            if not num in tmp_dict:
                tmp_dict[num] = 1
            else:
                tmp_dict[num]+=1

        return_ls = []
        values = sorted(list(tmp_dict.values()))[-1::-1]
        for freq in values:
            for key, v in tmp_dict.items():
                if v == freq:
                    return_ls.append(key)
                    del tmp_dict[key]
                    break

        return return_ls[:k]
