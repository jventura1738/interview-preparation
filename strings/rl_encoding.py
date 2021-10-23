# Justin Ventura Amazon Prep

help = """
Given a string, perform run length encoding for compression.

Ex1: aaaabbbcdd
  -> 4a3b1c2d

Ex2: 
  -> ''

Ex3: abc
  -> 1a1b1c
"""

import sys


def encode(string: str) -> str:
	"""Perform run length encoding for compression.

	Complexity( n=len(string) ):
		Time: O(n)
		Space: O(n)
	"""
	# Base cases:
	if string == None or len(string) == 0:
		return ''
	
	encoding = list()
	counter = 1
	for i in range(len(string)-1):
		if string[i] != string[i+1] or counter == 9:
			encoding.append(f'{counter}{string[i]}')
			counter = 1
		else:
			counter += 1
	encoding.append(f'{counter}{string[-1]}')
    
	return ''.join(encoding)


if __name__ == '__main__':
	assert(len(sys.argv) == 2), 'python3 rl_encoding.py rlencode_str'
	if sys.argv[1] == 'help':
		print(help)
	else:
		print(encode(str(sys.argv[1])))
