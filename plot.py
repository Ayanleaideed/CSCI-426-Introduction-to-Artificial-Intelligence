# Visualization code for satisfaction ratings
import matplotlib.pyplot as plt
import numpy as np

categories = ['Usability', 'Task Satisfaction', 'Trust', 'Time Savings', 'Convenience']
ratings = [4.50, 4.30, 4.20, 4.40, 4.40]
std_dev = [0.61, 0.66, 0.62, 1.05, 0.75]

plt.figure(figsize=(10, 6))
plt.bar(categories, ratings, yerr=std_dev, capsize=10, color='#5e17eb')
plt.ylim(0, 5)
plt.ylabel('Average Rating (1-5 Scale)')
plt.title('System Performance Metrics')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
