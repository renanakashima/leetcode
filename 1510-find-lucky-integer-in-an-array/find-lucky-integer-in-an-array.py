class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dictionary = {}
        for num in arr:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        result = -1
        for key in dictionary:
            if key == dictionary[key] and key > result:
                result = key
        return result