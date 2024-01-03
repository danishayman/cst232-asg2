# C-SCAN Disk Scheduling algorithm

def CSCAN(disk_size, arr, head):

	seek_count = 0
	distance = 0
	cur_track = 0
	left = []
	right = []
	seek_sequence = []

	# Append head to seek sequence
	seek_sequence.append(head)


	# Appending end values which has to be visited before reversing the direction
	left.append(0)
	right.append(disk_size - 1)


	# Tracks on the left of the head will be serviced when once the head comes back to the beginning (left end).
	for i in range(len(arr)):
		if (arr[i] < head):
			left.append(arr[i])
		if (arr[i] > head):
			right.append(arr[i])

	# Sorting left and right vectors
	left.sort()
	right.sort()

	# First service the requests on the right side of the head.
	for i in range(len(right)):
		cur_track = right[i]

		# Appending current track to seek sequence
		seek_sequence.append(cur_track)

		# Calculate absolute distance
		distance = abs(cur_track - head)

		# Increase the total count
		seek_count += distance

		# Accessed track is now new head
		head = cur_track

	# Once reached the right end jump to the beginning.
	head = 0

	# adding seek count for head returning from 199 to 0
	seek_count += (disk_size - 1)

	# Now service the requests again which are left.
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

	print("Total number of seek operations =", seek_count)
	
    # Calculate average seek time
	cscan_avg = seek_count / len(seek_sequence)
	print("Average seek time =", cscan_avg)
	

    # Calculate Worst-case seek time
	cscan_worst = max([abs(b - a) for a, b in zip(seek_sequence[:-1], seek_sequence[1:])])
	print("Worst-case seek time =", cscan_worst)


	print("Seek Sequence is: ", end=" ")
	for i in range(len(seek_sequence) - 1):
		print(seek_sequence[i], end=", ")
	print(seek_sequence[-1])


	return cscan_avg, cscan_worst, seek_sequence

