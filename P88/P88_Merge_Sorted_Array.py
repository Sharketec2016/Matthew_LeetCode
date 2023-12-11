class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_ptr = m-1
        n_ptr = n-1
        total_ptr = m+n-1
        while n_ptr>=0:
            if m_ptr >=0 and nums1[m_ptr] > nums2[n_ptr]:
                nums1[total_ptr] = nums1[m_ptr]
                m_ptr-=1
            else:
                nums1[total_ptr] = nums2[n_ptr]
                n_ptr-=1
            total_ptr-=1



