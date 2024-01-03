# SCAN Disk Scheduling algorithm

def  SCAN(disk_size, arr, head, direction):
 
    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []
 
    # Appending end values which has to be visited before reversing the direction
    if (direction == "left"):
        left.append(0)
    elif (direction == "right"):
        right.append(disk_size - 1)
 
    for i in range(len(arr)):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])
 
    # Sorting left and right vectors
    left.sort()
    right.sort()
 
    # Run the while loop two times one by one scanning righ and left of the head
    run = 2
    while (run != 0):
        if (direction == "left"):
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]
 
                # Appending current track to 
                # seek sequence
                seek_sequence.append(cur_track)
 
                # Calculate absolute distance
                distance = abs(cur_track - head)
 
                # Increase the total count
                seek_count += distance
 
                # Accessed track is now the new head
                head = cur_track
             
            direction = "right"
     
        elif (direction == "right"):
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
             
            direction = "left"
         
        run -= 1
 
    print("Total number of seek operations =", seek_count)


    # Calculate average seek time
    scan_avg = seek_count / len(seek_sequence)
    print("Average seek time =", scan_avg)
    
    

     # Calculate worst-case seek time
    scan_worst = max([abs(b - a) for a, b in zip(seek_sequence[:-1], seek_sequence[1:])])
    print("Worst-case seek time =", scan_worst)

    
    print("Seek Sequence is: ", end=" ")
    for i in range(len(seek_sequence) - 1):
        print(seek_sequence[i], end=", ")
    print(seek_sequence[-1])
        


    return scan_avg, scan_worst, seek_sequence
    