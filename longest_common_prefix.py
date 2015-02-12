class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            n = len(s)
            for i in xrange(len(prefix)):
                if i >= n or prefix[i] != s[i]:
                    prefix = prefix[:i]
                    break
        return prefix