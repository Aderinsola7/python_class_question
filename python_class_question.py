from bs4 import BeautifulSoup

# Read the HTML file
with open('python_class_question.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# Extract color data from the table
color_data = []
for row in soup.find('table').find('tbody').find_all('tr'):
    day, colors = row.find_all('td')
    color_data.extend(colors.text.split(', '))

# Convert color data to lowercase for consistency
color_data = [color.lower() for color in color_data]
import pandas as pd

# Sample data with color names
data = {
    'Color': ['green', 'yellow', 'green', 'brown', 'blue', 'pink', ...]  # Include all color values
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define a mapping of color names to numeric values
color_mapping = {
    'green': 1,
    'yellow': 2,
    'brown': 3,
    'blue': 4,
    'pink': 5,
    # Add more color mappings as needed
}

# Replace color names with numeric values
df['Color'] = df['Color'].map(color_mapping)


# 1. Which color of shirt is the mean color?
mean_color = df['Color'].mode().iloc[0]
print(f'1. Mean Color: {mean_color}')

# 2. Which color is mostly worn throughout the week?
most_worn_color = df['Color'].value_counts().idxmax()
print(f'2. Most Worn Color: {most_worn_color}')

# 3. Which color is the median?
median_color = df['Color'].median()
print(f'3. Median Color: {median_color}')

# 4. BONUS: Get the variance of the colors
color_variance = df['Color'].var()
print(f'4. Color Variance: {color_variance}')

# 5. BONUS: Probability of choosing red at random
probability_red = (df['Color'] == 'red').sum() / len(df)
print(f'5. Probability of Choosing Red: {probability_red}')

# 8. Generate a random 4-digit binary number of 0s and 1s and convert it to base 10
import random

def random_binary_to_decimal():
    random_binary = ''.join(random.choice('01') for _ in range(4))
    decimal_number = int(random_binary, 2)
    return random_binary, decimal_number

random_binary, decimal_number = random_binary_to_decimal()
print(f'8. Random Binary: {random_binary}')
print(f'   Converted to Decimal: {decimal_number}')

# 9. Write a program to sum the first 50 Fibonacci sequence
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

first_50_fibonacci = fibonacci(50)
sum_of_fibonacci = sum(first_50_fibonacci)
print(f'9. Sum of the First 50 Fibonacci Numbers: {sum_of_fibonacci}')