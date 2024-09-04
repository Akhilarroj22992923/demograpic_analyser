import pandas as pd

def load_data(file_path):
    """Load the data from a CSV file into a DataFrame."""
    df = pd.read_csv(file_path)
    return df

def count_race(df):
    """Count the number of people of each race."""
    return df['race'].value_counts()

def average_age_of_men(df):
    """Calculate the average age of men."""
    men = df[df['sex'] == 'Male']
    return round(men['age'].mean(), 1)

def percentage_bachelors(df):
    """Calculate the percentage of people with a Bachelor's degree."""
    total = len(df)
    bachelors = len(df[df['education'] == 'Bachelors'])
    return round((bachelors / total) * 100, 1)

def percentage_high_earners_with_advanced_education(df):
    """Calculate the percentage of people with advanced education who earn >50K."""
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    high_earners = df[(df['salary'] == '>50K') & advanced_education]
    percentage = (len(high_earners) / len(df[advanced_education])) * 100
    return round(percentage, 1)

def percentage_high_earners_without_advanced_education(df):
    """Calculate the percentage of people without advanced education who earn >50K."""
    no_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    high_earners = df[(df['salary'] == '>50K') & no_advanced_education]
    percentage = (len(high_earners) / len(df[no_advanced_education])) * 100
    return round(percentage, 1)

def minimum_hours_per_week(df):
    """Find the minimum number of hours worked per week."""
    return df['hours-per-week'].min()

def percentage_min_hours_high_earners(df):
    """Calculate the percentage of people who work the minimum number of hours per week and earn >50K."""
    min_hours = minimum_hours_per_week(df)
    min_hours_workers = df[df['hours-per-week'] == min_hours]
    high_earners = min_hours_workers[min_hours_workers['salary'] == '>50K']
    percentage = (len(high_earners) / len(min_hours_workers)) * 100
    return round(percentage, 1)

def country_with_highest_percentage_of_high_earners(df):
    """Find the country with the highest percentage of people earning >50K."""
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    country_salary['percentage'] = country_salary['>50K'] * 100
    return country_salary['percentage'].idxmax(), round(country_salary['percentage'].max(), 1)

def most_popular_occupation_in_india(df):
    # Filter the data for high earners in India
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    
    if india_high_earners.empty:
        return "No data available for high earners in India."

    # Find the most popular occupation
    try:
        most_popular_occupation = india_high_earners['occupation'].mode()[0]
        return most_popular_occupation
    except IndexError:
        return "No occupation data available for high earners in India."

