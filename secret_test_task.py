#Test task in Intetics Inc.
#The greatest number of palindromes, which is the product of two simple five-digit numbers

from math import sqrt, ceil
#import time
#start = time.time()

#min_value = 10000
#max_value = 99999
#prime_list = []

def check_prime(num):
	for i in xrange(2, int(ceil(sqrt(num)))+1):
		if num % i == 0:
			return False
	return True

def check_palindrome(num):
	num = str(num)
	#print num
	rev_num = ''.join(reversed(num))
	#print rev_num
	return num == rev_num

def find_all_primes(min=10000, max=99999):
	lst = []

	for num in xrange(min, max+1):
		if check_prime(num):
			lst.append(num)
	return lst

def find_max_palindrome(lst):
	first, second, result = 0, 0, 0
	for i in lst:
		for j in lst[lst.index(i)-1:]:
			if check_palindrome(i*j) and result < i*j:
				first, second, result = i, j, i*j
	return first, second, result

''' test
def find_all_palindrome(lst):
	palindrome_lst = []
	for i in lst:
		for j in lst:
			if check_palindrome(i*j):
				palindrome_lst.append(i*j)
	return palindrome_lst
'''

prime_list = find_all_primes() #(min_value, max_value)

''' tests
print prime_list
print "len: " + str(len(prime_list))
print check_palindrome(12345)
print check_palindrome(12321)
print check_palindrome(1221)
print check_palindrome(1222)

all_palindrome = find_all_palindrome(prime_list)
print all_palindrome
print max(all_palindrome)
'''

first, second, result = find_max_palindrome(prime_list)
print "Max palindrome is: %s * %s = %s" % (first, second, result)

#print("--- %s seconds ---" % (time.time() - start))