#pip install matplotlib seaborn

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Basic Charts

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]
data = np.random.randn(1000)
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)

# Line Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Sin(x)')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='g')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(x_scatter, y_scatter, alpha=0.6)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Pie Chart
plt.figure(figsize=(10, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')
plt.show()

# Advanced Charts

# Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, orient='h', palette='Set2')
plt.title('Box Plot')
plt.xlabel('Values')
plt.show()

# Violin Plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, palette='muted')
plt.title('Violin Plot')
plt.xlabel('Values')
plt.show()

# Heatmap
matrix_data = np.random.rand(10, 12)
plt.figure(figsize=(10, 6))
sns.heatmap(matrix_data, annot=True, fmt=".1f")
plt.title('Heatmap')
plt.show()

# 3D Plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
x_3d = np.random.rand(100)
y_3d = np.random.rand(100)
z_3d = np.random.rand(100)
ax.scatter(x_3d, y_3d, z_3d, c='r', marker='o')
ax.set_title('3D Scatter Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.show()

# Polar Plot
theta = np.linspace(0, 2*np.pi, 100)
r = 1 + np.sin(3*theta)
plt.figure(figsize=(10, 6))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_title('Polar Plot')
plt.show()
