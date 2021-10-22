from org.transcrypt.stubs.browser import *
import random

array = []
def bubble_sort(array):
    count = 0
    ###
    ## YOUR CODE HERE
    n = len(array)
    swapped = True
    while swapped == True:
        swapped = False
        new_n = 0
        for inner in range(1,n):
            first = array[inner - 1]
            second = array[inner]
            count += 1
            if first > second:
                temp = second
                array[inner] = array[inner - 1]
                array[inner - 1] = temp
                swapped = True
                new_n = inner
        n = new_n
    ###
    return count


def gen_random_int(number, seed):
    result = []
    ###
    ### YOUR CODE HERE
    random.seed(seed)
    for i in range(number):
        result.append(i)
    random.shuffle(result)
    ###
    return result

def generate():
	global array

	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	array = gen_random_int(number, seed)

	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	s= ""
	for i in range(len(array)):
		if i == (len(array) - 1):
			s += str(array[i])
		else:
			s = s + str(array[i]) + ", "

	array_str = s

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''

	original_str = document.getElementById("generate").innerHTML
	array_sorted = original_str.split(", ")

	bubble_sort(array_sorted)
	s = ""
	for i in range(len(array_sorted)):
		if i == (len(array_sorted) - 1):
			s += str(array_sorted[i])
		else:
			s = s + str(array_sorted[i]) + ", "

	array_str = s
	
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	value_arr = value.split(",")
	console.log(value_arr)
	for i in value_arr:
	    if i == "" or i == " ":
	        value_arr.remove(i)
	for i in range(len(value_arr)):
	        value_arr[i].strip()
	        value_arr[i] = int(value_arr[i])
	console.log(value_arr)
	bubble_sort(value_arr)
	s = ""
	for i in range(len(value_arr)):
		if i == (len(value_arr) - 1):
			s += str(value_arr[i])
		else:
			s = s + str(value_arr[i]) + ", "

	array_str = s

	document.getElementById("sorted").innerHTML = array_str


