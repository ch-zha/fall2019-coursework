import sys
import math
import random

def selectionSort(arr):
	for index in range(0, len(arr)):
		minval = arr[index]
		minindex = index
		for i in range(index, len(arr)):
			if (arr[i] < minval):
				minval = arr[i]
				minindex = i
		placeholder = arr[index]
		arr[index] = arr[minindex]
		arr[minindex] = placeholder
	return arr

def insertionSort(arr, start=0, end=None):
	if end is None:
		end = len(arr)
	for index in range(start, end):
		i = start
		while arr[index] > arr[i] and i < index:
			i += 1
		if i < index:
			placeholder = arr[index]
			for item in range(index, i, -1):
				arr[item] = arr[item - 1]
			arr[i] = placeholder
	return arr

def heapSort(arr):
	if len(arr) < 2:
		return
	leaves = int(len(arr)/2 - 1)
	for node in range(leaves, -1, -1):
		heapify(arr, len(arr), node)
	i = len(arr)
	while i > 0:
		i -= 1
		placeholder = arr[i]
		arr[i] = arr[0]
		arr[0] = placeholder
		heapify(arr, i, 0)

def heapify(arr, end, i):
	left = 2*i + 1
	right = 2*i + 2
	largest = i

	if left < end and arr[left] > arr[largest]:
		largest = left
	if right < end and arr[right] > arr[largest]:
		largest = right
	if largest != i:
		placeholder = arr[largest]
		arr[largest] = arr[i]
		arr[i] = placeholder
		heapify(arr, end, largest)

def mergeSort(arr, start=0, end=None):
	if end is None:
		end = len(arr)
	if end - start <= 1:
		return
	elif end - start < 10:
		insertionSort(arr, start, end)
	else:
		mid = int (math.ceil((end-start)/2)) + start
		mergeSort (arr, start, mid)
		mergeSort (arr, mid, end)
		merge(arr, start, mid, end)

def merge(arr, start, start2, end):
	temp = []
	pos1 = start
	pos2 = start2
	while pos1 < start2 and pos2 < end:
		if arr[pos1] <= arr[pos2]:
			temp.append(arr[pos1])
			pos1 += 1
		else:
			temp.append(arr[pos2])
			pos2 += 1
	while pos1 < start2 or pos2 < end:
		if pos1 < start2:
			temp.append(arr[pos1])
			pos1 += 1
		elif pos2 < end:
			temp.append(arr[pos2])
			pos2 += 1
	pos = 0
	for i in range(start, end):
		arr[i] = temp[pos]
		pos += 1


def quickSort(arr):
	partitions = []
	partitions.append([0, len(arr)])

	while len(partitions) > 0:
		nextset = partitions.pop()
		result = partition(arr, nextset[0], nextset[1])
		if result is not None:
			partitions.append([result[0], result[1]])
			partitions.append([result[2], result[3]])

def partition(arr, low=0, high=None):
	if high is None:
		high = len(arr)
	if high <= low:
		return None
	elif high - low < 10:
		insertionSort(arr, low, high)
		return None

	pivot = high - 1
	divider = low
	for i in range(low, high-1):
		if arr[i] <= arr[pivot]:
			placeholder = arr[i]
			arr[i] = arr[divider]
			arr[divider] = placeholder
			divider += 1
	placeholder = arr[divider]
	arr[divider] = arr[pivot]
	arr[pivot] = placeholder

	return [low, divider, divider+1, high]


def testSort():
	testArray1 = ['z', 'f', 's', 'g', 'e', 'v', 'e', 'k', 'a', 'b', 'd', 'c']
	testArray2 = []
	testArray3 = ['a', 'b', 'c']
	testArray4 = ['g']

	quickSort(testArray1)
	quickSort(testArray2)
	quickSort(testArray3)
	quickSort(testArray4)

	print(testArray1)
	print(testArray2)
	print(testArray3)
	print(testArray4)

testSort()