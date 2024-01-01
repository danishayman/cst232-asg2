# 📀💾 Disk Scheduling Algorithms 💽💿
This project implements three disk scheduling algorithms: SCAN, C-SCAN, and C-LOOK. The algorithms are evaluated based on average and worst-case seek times across different numbers of random requests.

## Getting Started

Ensure you have the required dependencies installed. You can install them using:
```bash
pip install matplotlib numpy
```

## Usage

1. Clone the repository:
```bash
git clone https://github.com/00Lupin/cst232-asg2.git
cd cst232-asg2
```
2. Run the main script:
```
python main.py
```

You may change the values of 
disk_size, head, direction ("left" / "right") and random requests in the main.py file as needed.


3. View the generated bar charts illustrating average and worst-case seek times in the .ipynb file.

## Project Structure
- algorithm/: Contains the implementation of disk scheduling algorithms.
- main.py: The main script to execute the algorithms and generate results.


## Results
### Average Seek Time
The chart depicts the average seek time for SCAN, C-SCAN, and C-LOOK algorithms across different numbers of random requests.

### Worst Seek Time
The chart illustrates the worst seek time for SCAN, C-SCAN, and C-LOOK algorithms across different numbers of random requests.

## Contributing
Feel free to contribute by opening issues or pull requests.

## Author
Aiman


