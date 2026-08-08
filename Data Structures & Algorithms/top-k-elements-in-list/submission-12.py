class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums)

        repeted_element = my_dict.most_common(k)
        output=[]
        for item in repeted_element:
            output.append(item[0])
        return output