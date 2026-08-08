class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        inputs = sorted(s)
        inputt = sorted(t)

        if inputs == inputt:
            return True
        else:
            return False