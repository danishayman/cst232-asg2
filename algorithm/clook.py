#C-LOOK Disk Scheduling algorithm
def CLOOK(arr, head):
	
	seek_count = 0
	distance = 0
	cur_track = 0

	left = []
	right = []

	seek_sequence = []

	# Appending head to seek sequence
	seek_sequence.append(head)

	# Tracks on the left of the head will be serviced when once the head comes back to the beginning (left end)
	for i in range(len(arr)):
		if (arr[i] < head):
			left.append(arr[i])
		if (arr[i] > head):
			right.append(arr[i])

	# Sorting left and right vectors
	left.sort()
	right.sort()

	# First service the requests on the right side of the head
	for i in range(len(right)):
		cur_track = right[i]
		
		# Appending current track  seek sequence
		seek_sequence.append(cur_track)

		# Calculate absolute distance
		distance = abs(cur_track - head)

		# Increase the total count
		seek_count += distance

		# Accessed track is now new head
		head = cur_track

	# Once reached the right end jump to the last track that is needed to be serviced in left direction
	seek_count += abs(head - left[0])
	head = left[0]

	# Now service the requests again which are left
	for i in range(len(left)):
		cur_track = left[i]

		# Appending current track to seek sequence
		seek_sequence.append(cur_track)

		# Calculate absolute distance
		distance = abs(cur_track - head)

		# Increase the total count
		seek_count += distance

		# Accessed track is now the new head
		head = cur_track

	print("Seek Sequence is: ", end=" ")
	for i in range(len(seek_sequence) - 1):
		print(seek_sequence[i], end=", ")
	print(seek_sequence[-1])
 
	print("Total number of seek operations =", len(seek_sequence)-1)

	print("Seek time =" , seek_count)

	# Calculate average seek time
	clook_avg = seek_count / (len(seek_sequence)-1)
	print("Average seek time =", clook_avg)
	

	# Calculate Worst-case seek time
	clook_worst= max([abs(b - a) for a, b in zip(seek_sequence[:-1], seek_sequence[1:])])
	print("Worst-case seek time =", clook_worst)

	return clook_avg, clook_worst, seek_sequence
