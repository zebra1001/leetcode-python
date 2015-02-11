class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer

    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        occurrence = -1
        needle_index = 0
        index = 0
        while index < len(haystack):
            if needle_index >= len(needle):
                return occurrence
            if haystack[index] == needle[needle_index]:
                needle_index += 1
                if occurrence == -1:
                    occurrence = index
                index += 1
            else:
                needle_index = 0
                if occurrence != -1:
                    index = occurrence + 1
                else:
                    index += 1
                occurrence = -1
        if needle_index != len(needle):
            return -1
        return occurrence

    def strStr2(self, haystack, needle):
        return haystack.find(needle)


s = Solution()
print s.strStr('a', 'a')
