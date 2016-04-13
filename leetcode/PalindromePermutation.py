def isPalindrome(str):
	"""
	"""
	n = len(str)

	for i in xrange(n / 2):
		if str[i] != str[n - 1 -i]:
			return False
	return True


a = 'aba'
print isPalindrome(a)