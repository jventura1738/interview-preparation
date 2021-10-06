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


def encode(input_str: str) -> str:
	"""Perform run length encoding for compression.

	Complexity( n=len(input_str) ):
		Time: O(n)
		Space: O(1)
	"""
	# Base cases:
	if input_str == None or len(input_str) == 0:
		return ' '
	if len(input_str) == 1:
		return f'1{input_str[0]}'
	
	# Prepare for iterating:
	s = input_str.strip()
	res = ''
	p = s[0]
	cnt = 1

	# Run through each char in string:
	for c in s[1:]:
		if c == p:
			cnt += 1
		else:
			res += f'{cnt}{p}'
			cnt = 1
		p = c

	res += f'{cnt}{s[-1]}'
	return res


if __name__ == '__main__':
	assert(len(sys.argv) == 2), 'python3 rl_encoding.py rlencode_str'
	if sys.argv[1] == 'help':
		print(help)
	else:
		print(encode(str(sys.argv[1])))
