import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Dataset salary 2024.csv'
data = pd.read_csv(file_path)

# Data Cleaning
# Remove duplicate rows
data_cleaned = data.drop_duplicates()

# Remove outliers with salary_in_usd greater than 1,000,000 as they seem unrealistic
data_cleaned = data_cleaned[data_cleaned['salary_in_usd'] <= 1_000_000]

# Analysis
# Trend 1: Salary distribution by job title
salary_by_job_title = data_cleaned.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)

# Trend 2: Salary distribution by experience level
salary_by_experience = data_cleaned.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)

# Trend 3: Distribution of remote work
remote_work_distribution = data_cleaned['remote_ratio'].value_counts().sort_index()

# Visualizations
plt.figure(figsize=(14, 10))

# Plot 1: Top 5 Highest Paying Job Titles
plt.subplot(3, 1, 1)
salary_by_job_title.head(5).plot(kind='bar', color='skyblue')
plt.title('Top 5 Highest Paying Job Titles')
plt.xlabel('Job Title')
plt.ylabel('Average Salary in USD')
plt.xticks(rotation=45, ha='right')

# Plot 2: Average Salary by Experience Level
plt.subplot(3, 1, 2)
salary_by_experience.plot(kind='bar', color='orange')
plt.title('Average Salary by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Average Salary in USD')

# Plot 3: Distribution of Remote Work
plt.subplot(3, 1, 3)
remote_work_distribution.plot(kind='bar', color='green')
plt.title('Distribution of Remote Work')
plt.xlabel('Remote Ratio')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

    
    
