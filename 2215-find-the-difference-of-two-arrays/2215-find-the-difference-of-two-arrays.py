class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash_one = {}
        hash_two = {}
        li1= []
        li2= []
        for i in nums1:
            hash_one[i]= hash_one.get(i,0)+1
        for i in nums2:
            hash_two[i]= hash_two.get(i,0)+1
        for i in nums1:
            if i not in hash_two and i not in li1:
                li1.append(i)
        for i in nums2:
            if i not in hash_one and i not in li2:
                li2.append(i)
        return [li1,li2]