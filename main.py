from demographic_data_analyzer import load_data, count_race, average_age_of_men, percentage_bachelors
from demographic_data_analyzer import percentage_high_earners_with_advanced_education, percentage_high_earners_without_advanced_education
from demographic_data_analyzer import minimum_hours_per_week, percentage_min_hours_high_earners
from demographic_data_analyzer import country_with_highest_percentage_of_high_earners, most_popular_occupation_in_india

file_path = '__pycache__\demographic_data.csv'
df = load_data(file_path)

print("Count of Each Race:")
print(count_race(df))

print("\nAverage Age of Men:")
print(average_age_of_men(df))

print("\nPercentage with Bachelor's Degree:")
print(percentage_bachelors(df))

print("\nPercentage of People with Advanced Education Earning >50K:")
print(percentage_high_earners_with_advanced_education(df))

print("\nPercentage of People Without Advanced Education Earning >50K:")
print(percentage_high_earners_without_advanced_education(df))

print("\nMinimum Number of Hours Worked Per Week:")
print(minimum_hours_per_week(df))

print("\nPercentage of Minimum Hour Workers Earning >50K:")
print(percentage_min_hours_high_earners(df))

print("\nCountry with Highest Percentage Earning >50K:")
country, percentage = country_with_highest_percentage_of_high_earners(df)
print(f"{country}: {percentage}%")

print("\nMost Popular Occupation for High Earners in India:")
print(most_popular_occupation_in_india(df))
