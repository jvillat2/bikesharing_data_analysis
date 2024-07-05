import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def data_extraction(file_list):

    df = []
    df = pd.DataFrame(df)
    # Read the Excel file
    for i in file_list:
        read_file = pd.read_csv(i)  
        df_file = pd.DataFrame(read_file)
        df = pd.concat([df, df_file], ignore_index=True)
    

    return df
   

def data_cleaning(df):

    #look for nulls
    column_list = ['ride_id', 'started_at', 'ended_at', 'member_casual']

    for column in column_list:
        null_values = df[df[column].isnull()]
        if not null_values.empty:
            print(f'Null values found in {column}:\n{null_values}\n')
        else:
            print(f'No null values in {column}\n')

    # Convert columns to datetime
    df['started_at'] = pd.to_datetime(df['started_at'])
    df['ended_at'] = pd.to_datetime(df['ended_at'])


    # Calculate the time difference and day of week to stgore them in columns
    df['ride_length'] = pd.to_timedelta(df['ended_at'] - df['started_at'])
    df['ride_length'] = pd.to_timedelta(df['ride_length'])
    df['month_year'] = df['started_at'].dt.to_period('M')
    df['day_of_week'] = df['started_at'].dt.weekday
   


    # Print duplicated rows and delete
    dup_list = df[df['ride_id'].duplicated(keep=False)]

    if not dup_list.empty:
        print('duplicates in ride_id \n', dup_list['ride_id'].count())
        df = df.drop_duplicates(subset='ride_id', keep='first')
        print('dropping duplicates...\n\n')
    else:
        print('No duplicates in Ride_id\n\n')


    #delete rows that are less than or equal to 0 in ride_length
    negative_df = df[df.ride_length <= pd.to_timedelta("0 days 00:00:00")]

    if not negative_df.empty:
        print('Values less than or equal to 0 in ride_length: ', negative_df['ride_length'].count())
        print('\ndropping negatives...\n\n')
        df = df[df.ride_length > pd.to_timedelta("0 days 00:00:00")]
    else:
        print('\nNo values less than or equal to 0 in ride_length\n\n')

    return df



def data_analysis(df):

    #exploring df's data
    '''
    categorical = df.dtypes[df.dtypes == "object"].index
    print("_________________________________Analysis over view on df____________________________________\n", df.describe(),'\n', df[categorical].describe(), '\n\n')
    '''
    
   # create dataframe for the of casual members

    casual_df = df[df['member_casual'] == 'casual']
    member_df = df[df['member_casual'] == 'member']

    #find the mean and count of caual member df grouped by day of the week
    casual_analysis = casual_df.groupby('day_of_week')['ride_length'].mean().reset_index(name='mean_ride_length')
    member_analysis = member_df.groupby('day_of_week')['ride_length'].mean().reset_index(name='mean_ride_length')
    
    casual_analysis['ride_id_count'] = casual_df.groupby('day_of_week')['ride_id'].count().values
    member_analysis['ride_id_count'] = member_df.groupby('day_of_week')['ride_id'].count().values

    #turn mean ride length into minutes 
    casual_analysis['mean_ride_length'] = casual_analysis['mean_ride_length'].dt.total_seconds() / 60
    member_analysis['mean_ride_length'] = member_analysis['mean_ride_length'].dt.total_seconds() / 60

    
    # Group by 'month_year' and count 'ride_id' for casual and member riders
    casual_counts = casual_df.groupby('month_year')['ride_id'].count().reset_index(name='casual_count')
    member_counts = member_df.groupby('month_year')['ride_id'].count().reset_index(name='member_count')
    

    # Extract month names for line chart's x-axis labels
    casual_counts['month_name'] = casual_counts['month_year'].dt.strftime('%B %Y')
    member_counts['month_name'] = member_counts['month_year'].dt.strftime('%B %Y')



    # Plotting Ride Count by Month for Casual and Member Riders
    
    plt.figure(figsize=(12, 6))
    plt.plot(casual_counts['month_name'], casual_counts['casual_count'], label='Casual Riders', color='blue', marker='o')
    plt.plot(member_counts['month_name'], member_counts['member_count'], label='Member Riders', color='green', marker='o')
    plt.xlabel('Months (June 2023 - May 2024)')
    plt.ylabel('Ride Count')
    plt.title('Ride Count by Month for Casual and Member Riders')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # plotting Average Ride Length by Membership Type and Day of the Week (June 2023 - May 2024)
    
    plt.figure(figsize=(10, 6))
    plt.bar(casual_analysis['day_of_week'] - 0.4/2, casual_analysis['mean_ride_length'], width =0.4, color='skyblue', label='Casual Rider')
    plt.bar(member_analysis['day_of_week'] + 0.4/2, member_analysis['mean_ride_length'], width =0.4, color='blue', label='Member Rider')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Ride Length (minutes)')
    plt.title('Average Ride Length by Membership Type and Day of the Week (June 2023 - May 2024)')
    plt.xticks(casual_analysis['day_of_week'],  [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.legend()
    plt.show()


    # Plotting Rider Count by Type of Member and Day of the Week (June 2023 - May 2024)
    
    plt.figure(figsize=(10, 6))
    plt.bar(casual_analysis['day_of_week'] - 0.4/2, casual_analysis['ride_id_count'], width =0.4, color = 'skyblue', label='Casual Rider')
    plt.bar(member_analysis['day_of_week'] + 0.4/2, member_analysis['ride_id_count'], width =0.4, color = 'blue', label='Member Rider')
    plt.xlabel('Day of The Week')
    plt.ylabel('Rider count')
    plt.title('Rider Count by Type of Member and Day of the Week (June 2023 - May 2024)')
    plt.xticks(casual_analysis['day_of_week'], [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.legend()
    plt.show() 
    

    #plotting Average Ride Length
    
    df_analysis = df.groupby('member_casual')['ride_length'].mean().reset_index(name='mean_ride_length')


    #turn mean ride length into minutes 
    df_analysis['mean_ride_length'] = df_analysis['mean_ride_length'].dt.total_seconds() / 60


    # Plot the bar chart Average Ride Length by Type of Member 
    plt.figure(figsize=(10, 6))
    plt.bar(df_analysis['member_casual'], df_analysis['mean_ride_length'], color=['skyblue', 'lightgreen'])
    plt.xlabel('Member Type')
    plt.ylabel('Average Ride Length (minutes)')
    plt.title('Average Ride Length by Type of Member (June 2023 - May 2024)')
    plt.show()
    

def save(file, df):
    for i in file:
        i
    df.to_csv(i, index=False)
 
    
if __name__ == "__main__":
    excelFiles = ['C:\\Users\\jenni\\Documents\\trip_data\\202306-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202307-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202308-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202309-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202310-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202311-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202312-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202401-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202402-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202403-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202404-divvy-tripdata.csv', 'C:\\Users\\jenni\\Documents\\trip_data\\202405-divvy-tripdata.csv']    
    data = data_extraction(excelFiles)
    df_data = data_cleaning(data)
    data_analysis(df_data)
    #save(excelFiles, df)
    
    


           

