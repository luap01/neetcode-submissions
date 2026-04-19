class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0

        r1 = len(nums1) - 1
        l1 = m - 1

        l2 = n - 1

        # 10 20 20 0 0 40


        while l2 >= 0 and l1 >= 0:
            if nums1[l1] > nums2[l2]:
                nums1[r1] = nums1[l1]
                nums1[l1] = 0
                l1 -= 1
                r1 -= 1
            else:
                nums1[r1] = nums2[l2]
                l2 -= 1
                r1 -= 1

        while l2 >= 0:
            nums1[r1] = nums2[l2]
            l2 -= 1
            r1 -= 1

            