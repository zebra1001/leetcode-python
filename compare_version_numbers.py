class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
    	version1 = version1.split('.')
    	version2 = version2.split('.')

    	if len(version1) > len(version2):
    		version2.extend(['0'] * (len(version1) - len(version2)))
    	elif len(version1) < len(version2):
    		version1.extend(['0'] * (len(version2) - len(version1)))

    	for index in xrange(0, min(len(version1), len(version2))):
    		if int(version1[index]) > int(version2[index]):
    			return 1
    		elif int(version1[index]) < int(version2[index]):
    			return -1
    		else:
    			index += 1

    	return 0