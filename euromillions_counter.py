#use for counting how many times each number has been drawn in the real euromillions


from collections import Counter
import re
import matplotlib.pyplot as plt
def main():

    
    with open("euro_millions_past_results.txt", "r") as file:
        lines = file.readlines()

    numbers = []

    for line in lines:
        match = re.match(r'^\s*([\d\s]+)', line)
        if match:
            nums = match.group(1).split()
            numbers.extend(nums)


    counter = Counter(numbers)
    least_common = sorted(counter.items(), key=lambda x: int(x[0]))  # sort by number 

   
    nums = [int(num) for num, count in least_common]
    counts = [count for num, count in least_common]

    
    print("Number occurrences:")
    for num, count in least_common:
        print(f"Number: {num}, Count: {count}")

    
    plt.plot(nums, counts, marker='o')
    plt.title("EuroMillions Number Frequencies")
    plt.xlabel("Number")
    plt.ylabel("Occurrences")
    plt.grid(True)
    plt.show()
