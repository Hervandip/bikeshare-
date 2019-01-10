import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
    	city = input('\nWhich city do you like to see? (Chicago, New york city, Washington)\n')
    	if city.lower() not in cities:
    		print ('Please input valid city')
    	else:
    		break

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
    	month = input('\n Which month do you want? (January, February, March, April, May, June, or all)\n')
    	if month.lower() not in months:
    		print ('Please input valid month')
    	else:
    		break	

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
    	day = input('\n Which day do you like? (Monay, Tuesday, Wednesday, Thursday, Friday, Saturday, SUnday, or all)\n')
    	if day.lower() not in days:
    		print ('Please input valid day')
    	else:
    		break

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
    # load data file
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create new column for month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month
    if  month.lower() != 'all':
    	months = ['january', 'february', 'march', 'april', 'may', 'june']
    	month = months.index(month) + 1
    	df = df.loc[df['month'] == month.lower()]

    # filter by day
    if day.lower() != 'all':
    	df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print ('The most common month: ', most_common_month)

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print ('The most common day: ', most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print ('The most common start hour: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print ('The most commonly used start station: ', most_start_station)

    # display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print ('The most commonly used end station: ', most_end_station)

    # display most frequent combination of start station and end station trip
    most_combination_station = (df['Start Station'].append(df['End Station'])).mode()[0]
    print ('The most frequent combination of start station and end station trip: ', most_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print ('Total travel time: ', total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print ('Mean travel time: ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user = df['User Type'].value_counts()
    print ('Count of user types: ', counts_of_user)

    # Display counts of gender
    if city.lower() == 'washington':
    	print('There is no gender data in this city')
    else:	
    	counts_of_gender = df['Gender'].value_counts()
    	print ('Counts of gender: ', counts_of_gender)
    	
    # Display earliest, most recent, and most common year of birth
    if city.lower() == 'washington':
    	print ('There is no year of birth data in this city')
    else:	
    	earliest_birth = df['Birth Year'].min()
    	print ('The earliest year of birth: ', earliest_birth)
    	most_recent_birth = df['Birth Year'].max()
    	print ('The most recent year of birth: ', most_recent_birth)
    	most_common_birth = df['Birth Year'].mode()[0]
    	print ('The most commonly year of birth: ', most_common_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
