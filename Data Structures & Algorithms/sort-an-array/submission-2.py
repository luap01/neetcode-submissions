class Solution:

    # 10 9 1 1
    # l=0, r=1, m=0 (10, 9)
    # 
    # 10 9
    #
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        lh = [0] * n1
        rh = [0] * n2

        for i in range(n1):
            lh[i] = arr[l + i]
        for j in range(n2):
            rh[j] = arr[m + 1 + j]
        
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if lh[i] <= rh[j]:
                arr[k] = lh[i]
                i += 1
            else:
                arr[k] = rh[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = lh[i]
            i += 1
            k += 1
        
        while j < n2:
            arr[k] = rh[j]
            j += 1
            k += 1
    
    def merge_sort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2

            self.merge_sort(arr, l, m)
            self.merge_sort(arr, m + 1, r)
            self.merge(arr, l, m, r)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums