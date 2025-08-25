# use this for seeing if the odds for each number balance out over time

import random   
import matplotlib.pyplot as plt
from collections import Counter

def balls_draw():
    draws = []
    for i in range(9345):             #9345 is how many draws there have been so far, or at least in the text file
        draw_ball = random.randint(1, 50)
        draws.append(draw_ball)
    return draws

def run_simulation():
    draws = balls_draw()
    counter = Counter(draws)

    print("Ball occurrences:")
    for ball, count in sorted(counter.items()):
        print(f"{ball}: {count}")

    # Optional: plot the results
    plt.bar(counter.keys(), counter.values())
    plt.xlabel('Ball Number')
    plt.ylabel('Occurrences')
    plt.title('Ball Draw Occurrences')
    plt.show()
