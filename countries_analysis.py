import pandas as pd
import matplotlib.pyplot as plt

# Loads the population data
population_data = pd.read_csv('country_population.csv')

# Sorts data by population in descending order
population_data = population_data.sort_values(by='Population', ascending=False)

# Displays message for users and users have to press "Enter" to continue
print("This is the top 10 most populated countries.")
input("Press the Enter key to continue.")

# Displays the top 10 most populated countries 
top_10 = population_data.head(10)
print("Top 10 most populated countries:")
print(top_10)

# Creates a bar plot for top 10 country populations
plt.figure(figsize=(10, 6))
plt.bar(top_10['Country'], top_10['Population'], color='skyblue')
plt.title('Top 10 Most Populated Countries')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45, ha='right')

# Set y-axis range from 0 to 250 million to 1.5 billion
plt.yticks(range(0, 1_500_000_001, 250_000_000))

plt.tight_layout()

# Saves the plot as an image
plt.savefig('top_10_country_population_chart.png')

# Shows the chart
plt.show()
