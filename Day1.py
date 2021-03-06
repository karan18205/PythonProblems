print('Starting Here')

## Program 1

# Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice
# with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
#
# Examples
# stutter("incredible") ➞ "in... in... incredible?"

def stutter(word):
	ans = word[0:2]+'.. '+word[0:2]+'.. '+word
	print(ans)

########################################################################################################################

## Program 2

# Python got drunk and the built-in functions str() and int() are acting odd:
#
# str(4) ➞ 4
#
# str("4") ➞ 4
# You need to create two functions to substitute str() and int(). A function called int_to_str() that converts integers
# into strings and a function called str_to_int() that converts strings into integers.
#
# Examples:
# int_to_str(4) ➞ "4"

def int_to_str(num):
	 print(int(num))

def str_to_int(num):
	 print(str(num))

########################################################################################################################

## Program 3

# Finding Adjacent Nodes
# A graph is a set of nodes and edges that connect those nodes.
#
# Graph Example
#
# There are two types of graphs; directed and undirected. In an undirected graph, the edges between nodes have no
# particular direction (like a two-way street) whereas in a directed graph, each edge has a direction associated with it
# (like a one-way street).
#
# For two nodes in a graph to be considered adjacent to one another, there must be an edge between them. In the example
# given above, nodes 0 and 1 are adjacent, but nodes 0 and 2 are not.
#
# We can encode graphs using an adjaceny matrix. An adjacency matrix for a graph with "n" nodes is an "n * n" matrix
# where the entry at row "i" and column "j" is a 0 if nodes "i" and "j" are not adjacent, and 1 if nodes "i" and "j" are
# adjacent.
#
# For the example above, the adjacency matrix would be as follows:
#
# [
#   [ 0, 1, 0, 0 ],
#   [ 1, 0, 1, 1 ],
#   [ 0, 1, 0, 1 ],
#   [ 0, 1, 1, 0 ]
# ]
# A one indicates that a connection is true and a zero indicates a connection is false.
#
# Here is how the above model might be written out:
#
# On the first row, node 0 does not connect to itself, but it does connect to node 1. It does not connect to node 2 or
# node 3. The row is written as 0, 1, 0, 0.
# On the second row, node 1 connects to node 0, node 2 and node 3, but it does not connect to itself. The row is written
# as 1, 0, 1, 1.
# On the third row, node 2 does not connect to node 0, but it does connect to node 1, does not connect to itself, and it
# does connect to node 3. The row is written as 0, 1, 0, 1
# On the fourth row, node 3 does not connect to node 0, but it does connect to node 1 and node 2. It does not connect to
# itself. The row is written as 0, 1, 1, 0.
# Your task is to determine if two nodes are adjacent in a graph when given the adjacency matrix and the two nodes.
#
# Examples
# Graph Example
#
# Adjacency Matrix:
#
# [
#   [ 0, 1, 0, 0 ],
#   [ 1, 0, 1, 1 ],
#   [ 0, 1, 0, 1 ],
#   [ 0, 1, 1, 0 ]
# ]
# Nodes 0,1 should return True.
# Nodes 0,2 should return False.
# Graph Example 2
#
# [
#   [ 0, 1, 0, 1, 1 ],
#   [ 1, 0, 1, 0, 0 ],
#   [ 0, 1, 0, 1, 0 ],
#   [ 1, 0, 1, 0, 1 ],
#   [ 1, 0, 0, 1, 0 ]
# ]
# Nodes 0,3 should return True.
# Nodes 1,4 should return False.


matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]

def is_adjacent(matrix, node1, node2):
	if matrix[node1][node2]==1:
		print('Adjacent')
	else:
		print('Not Adjacent')

# is_adjacent(matrix, 0, 1)

########################################################################################################################

## Program 4

# Jay and Silent Bob Weight Convertor
# Jay and Silent Bob have been given a fraction of an ounce but they only understand grams. Convert a fraction passed as a
# string to grams with up to two decimal places. An ounce weighs 28 grams.
#
# Examples
# jay_and_bob("half") ➞ "14 grams"
#
# jay_and_bob("quarter") ➞ "7 grams"
#
# jay_and_bob("eighth") ➞ "3.5 grams"

def jay_and_bob(txt):
	if txt=="half":
		print(round(28/2,2))
	elif txt=="quarter":
		print(round(28/4),2)
	elif txt=="eigth":
		print(round(28/8,2))
	elif txt=="sixteenth":
		print(round(28/16,2))

########################################################################################################################

## Program 5

# FizzBuzz Interview Question
# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
#
# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
# The output should always be a string even if it is not a multiple of 3 or 5.
# Examples
# fizz_buzz(3) ➞ "Fizz"
#
# fizz_buzz(5) ➞ "Buzz"
#
# fizz_buzz(15) ➞ "FizzBuzz"
#
# fizz_buzz(4) ➞ "4"

def fizz_buzz(num):
	if(num%3==0 and num%5==0):
		print('FizzBuzz')
	elif(num%3==0 and num%5!=0):
		print('Fizz')
	elif(num%3!=0 and num%5==0):
		print('Buzz')
	elif(num%3!=0 and num%5!=0):
		print(num)

# fizz_buzz(98)

########################################################################################################################

## Program 6

# Length of Number
# Create a function that takes a number num and returns its length.
#
# Examples
# number_length(10) ➞ 2
#
# number_length(5000) ➞ 4
#
# number_length(0) ➞ 1

def number_length(num):
	return print(len(str(num)))

# number_length(777777777777777777777777777777)

########################################################################################################################

## Program 7

# Right Shift by Division
# The right shift operation is similar to floor division by powers of two.
#
# Sample calculation using the right shift operator ( >> ):
#
# 80 >> 3 = floor(80/2^3) = floor(80/8) = 10
# -24 >> 2 = floor(-24/2^2) = floor(-24/4) = -6
# -5 >> 1 = floor(-5/2^1) = floor(-5/2) = -3
# Write a function that mimics (without the use of >>) the right shift operator and returns the result from the two given integers.
#
# Examples
# shift_to_right(80, 3) ➞ 10
#
# shift_to_right(-24, 2) ➞ -6

def floor(n):
    res = int(n)
    return res if res == n or n >= 0 else res-1

def shift_to_right(x, y):
	return print(floor(x/2**y))

# shift_to_right(-24, 2)

########################################################################################################################

## Program 8
# Designing Rugs
# Write a function that accepts the width and height (m, n) and an optional proc s and generates a list with m elements.
# Each element is a string consisting of either:
#
# The default character (hash #) repeating n times (if no proc is given).
# The character passed in through the proc repeating n times.

def make_rug(m, n, s):

	part = ''
	if s:
		part = [s * n]
	else:
		part = ['#' * n]

	for i in range(m):
		print(part[0])

def make_rug(m, n):
	part = ''
	part = ['#' * n]
	final = []
	for i in range(m):
		final.append(part[0])
	print(final)
	return final

def rug(m = None, n = None, s = None):
	part = ''
	if s:
		part = [s * n]
	else:
		part = ['#' * n]

	final = []
	for i in range(m):
		final.append(part[0])
	print(final)
	return final

# rug(5,4,'$')

########################################################################################################################

## Program 9
# A Circle and Two Squares
# Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for
# the bigger one, an incircle.
# Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two
# squares.

def square_areas_difference(r):
	smaller_sq = (2*r*r)
	larger_sq = (2*r*2*r)

	print(larger_sq-smaller_sq)

# square_areas_difference(5)

########################################################################################################################

## Program 10

# Calculate the Profit
# You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are
# given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting
# inventory. Return the total profit made, rounded to the nearest dollar.

def profit(info):
	return print(round(info['inventory']*(info['sell_price']-info['cost_price'])))

profit({'cost_price': 32.67, 'sell_price': 45.00, 'inventory': 1200})







































