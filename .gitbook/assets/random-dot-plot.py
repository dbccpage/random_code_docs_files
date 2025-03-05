import matplotlib.pyplot as plt
import numpy as np

# Generate 50 random integers
np.random.seed(42)  # for reproducibility
random_integers = np.random.randint(1, 100, 50)

# Create the dot plot
plt.figure(figsize=(10, 6))
plt.scatter(range(len(random_integers)), random_integers, 
            color='blue', alpha=0.7, s=100)

plt.title('Random Integers Dot Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()

# Print the list of random integers for reference
print(random_integers.tolist())
