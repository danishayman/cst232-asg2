import random
from algorithm.scan import SCAN
from algorithm.cscan import CSCAN
from algorithm.clook import CLOOK


#initialization
disk_size = 200
head = 50
direction = "left"
random_request = [10, 20, 50, 100]

for size in random_request:
    # Generate 'size' random requests
    arr = [random.randint(0, disk_size-1) for _ in range(size-1)]
    print(f"\nRunning SCAN algorithm for {size} requests:")
    SCAN(disk_size, arr, head, direction)
    print(f"\nRunning C-SCAN algorithm for {size} requests:")
    CSCAN(disk_size, arr, head)
    print(f"\nRunning C-LOOK algorithm for {size} requests:")
    CLOOK(arr, head)
    print("\n \n")
