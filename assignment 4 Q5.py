def isPalindrome(num):

	for i in range(0, int(len(num)/2)): 
		if num[i] != num[len(num)-i-1]:
			return False
	return True
num = input("Enter the number: ")
ans = isPalindrome(num)
if (ans):
	print("Palindrome Number")
else:
	print("Not a Palindrome Number")
