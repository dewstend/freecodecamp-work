## Initial file provided by freeCodeCamp

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult_data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"] == "Male"]["age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df["education"].value_counts()["Bachelors"]
    percentage_bachelors = (bachelors_count / len(df.index) * 100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    higher_education_mask = df["education"].isin(["Bachelors", "Masters", "Doctorate"])

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[higher_education_mask]
    lower_education = df[~higher_education_mask]

    # count with salary >50K
    higher_education_rich_count = higher_education[
        higher_education["salary"] == ">50K"
    ].shape[0]
    lower_education_rich_count = lower_education[
        lower_education["salary"] == ">50K"
    ].shape[0]

    # percentage with salary >50K
    higher_education_rich = round(
        higher_education_rich_count / higher_education.shape[0] * 100, 1
    )
    lower_education_rich = round(
        lower_education_rich_count / lower_education.shape[0] * 100, 1
    )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hour_workers = df[df["hours-per-week"] == min_work_hours]
    num_min_workers = min_hour_workers.shape[0]

    min_hour_workers_rich = min_hour_workers[min_hour_workers["salary"] == ">50K"]

    rich_percentage = num_min_workers / min_hour_workers_rich.shape[0]

    # What country has the highest percentage of people that earn >50K?
    highest_earners = df[df["salary"] == ">50K"]

    highest_earners_by_country = highest_earners["native-country"].value_counts()

    country_counts = df["native-country"].value_counts()

    highest_earner_percentages_by_country = highest_earners_by_country / country_counts

    highest_earning_country = highest_earner_percentages_by_country.idxmax()
    highest_earning_country_percentage = (
        highest_earner_percentages_by_country.max() * 100
    ).round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    highest_earners_in_india = highest_earners[
        highest_earners["native-country"] == "India"
    ]
    top_IN_occupation = highest_earners_in_india["occupation"].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
