# Given an integer, write a function to determine if it is a power of three.

# Follow up:
# Could you do it without using any loop / recursion?

def isPowerOfThree(n):
	if n == 0: return False
	if n == 1: return True
	return n % 3 == 0 and isPowerOfThree(n / 3)


def isPowerOfThree2(n):
	return False if n <= 0 else n == round(3 ** round(math.log(n, 3)))

print isPowerOfThree(8)