
# Salary Trends Visualizer

## Project Purpose

**Salary Trends Visualizer** is a data analysis and visualization project designed to explore and uncover trends in salary data. By analyzing a dataset of salaries, this project aims to provide insights into salary distributions across different job titles, experience levels, and remote work arrangements. The visualizations generated can help individuals and organizations make informed decisions regarding career choices, hiring practices, and salary negotiations.

## Dataset

The dataset used in this project contains information on various job titles, experience levels, employment types, salaries, and remote work ratios for the year 2024. Key columns in the dataset include:
- `work_year`: The year of the data.
- `experience_level`: The level of experience (e.g., Entry, Mid, Senior, Executive).
- `employment_type`: The type of employment (e.g., Full-time).
- `job_title`: The title of the job.
- `salary`: The salary in the local currency.
- `salary_currency`: The currency of the salary.
- `salary_in_usd`: The salary converted to USD.
- `employee_residence`: The residence of the employee.
- `remote_ratio`: The percentage of remote work (0, 50, 100).
- `company_location`: The location of the company.
- `company_size`: The size of the company (e.g., Small, Medium, Large).

## Key Insights

### Top 5 Highest Paying Job Titles
The analysis revealed the top five highest paying job titles:
1. **Analytics Engineering Manager**: \$399,880
2. **Data Science Tech Lead**: \$375,000
3. **Head of Machine Learning**: \$299,758
4. **Managing Director Data Science**: \$280,000
5. **AWS Data Architect**: \$258,000

### Average Salary by Experience Level
The average salary based on different experience levels showed a clear correlation between higher experience levels and higher salaries:
- **Executive (EX)**: \$195,218
- **Senior (SE)**: \$163,331
- **Mid (MI)**: \$124,116
- **Entry (EN)**: \$91,351

### Distribution of Remote Work
The distribution of employees based on their remote work ratio indicated that most employees are either fully remote or not remote at all:
- **0% Remote**: 6,394 employees
- **50% Remote**: 247 employees
- **100% Remote**: 3,472 employees

## Visualizations

The project includes the following visualizations to illustrate the trends:



1. **Top 5 Highest Paying Job Titles**
   

2. **Average Salary by Experience Level**
   

3. **Distribution of Remote Work**
   
![visuals](https://github.com/jeremiahwarinner/Salary-Trends-Visualizer/assets/158241209/85a19575-670d-4329-9e44-7d851b85f755)

## How to Use

To run the analysis and generate the visualizations:

1. Clone the repository:
   ```bash
   git clone https://github.com/jeremiahwarinner/Salary-Trends-Visualizer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd SalaryTrendsVisualizer
   ```
3. Install the required dependencies:
   ```bash
   pip install pandas matplotlib
   ```
4. Run the analysis script:
   ```bash
   python analyze_salary_data.py
   ```

## Conclusion

**SalaryTrendsVisualizer** provides valuable insights into salary trends across various dimensions. These insights can help guide career decisions, inform salary negotiations, and support organizational hiring strategies.
