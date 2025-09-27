import random
import time
import sys

# Simulate rolling animation
print("Rolling the dice", end="")
for i in range(5):
    print(".", end="")
    sys.stdout.flush()
    time.sleep(0.4)

# Final result
roll = random.randint(1, 6)
print(f"\nYou rolled a {roll}!")