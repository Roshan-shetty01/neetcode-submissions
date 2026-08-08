class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using defaultdict(list) prevents KeyErrors when adding new keys
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to use as a key
            # sorted("eat") returns ['a', 'e', 't'], so we join it back to "aet"
            sorted_key = "".join(sorted(s))
            
            # Append the original string to the corresponding sorted key
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())