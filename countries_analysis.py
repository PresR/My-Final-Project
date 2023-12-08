# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the population data
population_data = pd.read_csv('country_population.csv')

# Display the data (optional)
print(population_data)

# Sort data by population in descending order
population_data = population_data.sort_values(by='Population', ascending=False)

# Create a bar plot for country population
plt.figure(figsize=(10, 6))
plt.bar(population_data['Country'], population_data['Population'], color='skyblue')
plt.title('Population of Countries')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot as an image
plt.savefig('country_population_chart.png')

# Show the plot
plt.show()
