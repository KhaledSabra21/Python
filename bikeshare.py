import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': '/home/khaled/Documents/chicago.csv',
             'new york city': '/home/khaled/Documents/new_york_city.csv',
             'washington': '/home/khaled/Documents/washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike share data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("would you like to see data about chicago, new york city or washington? ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print('please you need to choose a city')
        city = input('choose chicago, new york city or washington: ').lower()

    # get user input for month (all, january, february, ... , june)
    month = input("would you like to see data for Jan, Feb, March, May, April, June or All ").lower()
    while month not in ['jan', 'feb', 'march', 'may', 'april', 'june', 'all']:
        month = input('please choose: Jan, Feb, March, May, April, June or All ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('choose: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All ').lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input('please choose: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['month_name'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['jan', 'feb', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    popular_month = df['month_name'].mode()[0]
    count_month = df['month_name'].value_counts().max()
    print('Most Popular month: ', popular_month, ',count month:', count_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    count_day = df['day_of_week'].value_counts().max()
    print('Most Popular popular day of week: ', popular_day, ',count day:', count_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    count_hour = df['hour'].value_counts().max()
    print('Most Popular Start Hour:', popular_hour, ',count hour:', count_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    count_start_station = df['Start Station'].value_counts().max()
    print('most popular Start Station: ', popular_start_station, ',count start station:', count_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    count_end_station = df['End Station'].value_counts().max()
    print('most popular End Station', popular_end_station, ',count end station:', count_end_station)

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + df['End Station']
    most_common_trip = df['Trip'].mode()[0]
    count_trip = df['Trip'].value_counts().max()
    print('most common trip from start to end station: ', most_common_trip, ',count trip:', count_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time: ', total_travel_time)

    # display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print('average travel time: ', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('count of each user type: ')
    print(user_types)

    # Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('counts of each gender: ')
        print(counts_of_gender)
    except KeyError:
        print('there is no data for gender')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('earliest birth year: ', earliest_year)
        most_recent_year = df['Birth Year'].max()
        print('most recent birth year: ', most_recent_year)
        most_common_year = df['Birth Year'].mode()[0]
        count_common_year = df['Birth Year'].value_counts().max()
        print('most common year of birth: ', most_common_year, ',count common year:', count_common_year)
    except KeyError:
        print('there is no data for birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def row_data(df):
    a = 0
    n = 5
    data = 'yes'
    while True:
        c_data = input('would you like to see row data? yes or no ')
        if c_data == data:
            a += 5
            n += 5
            j =  pd.set_option("display.max_columns", 200)
            print(df.iloc[a:n], j)
        else:
            break
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
