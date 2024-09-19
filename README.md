# Cyclistic Bike-Share Analysis and Recommendations

## Project Background
Cyclistic, a fictional company, introduced a successful bike-share program in 2016. Since its inception, it has expanded to include about 5,824 geotracked bicycles, which can be locked into any of the 692 stations spread throughout Chicago. Cyclistic serves two groups: casual riders, who use the service infrequently without a membership, and members, who hold annual memberships. The company has significant amounts of data from May 2023 to June 2024 on their user’s ride date and time, the stations user’s start and end their rides, and bike type used on their ride that has been previously underutilized. This project thoroughly analyzes and synthesizes this data in order to uncover critical insights on the difference of casual rider and members to then use to craft strategic marketing strategies that could potentially help convert casual riders into annual members.


Insights and recommendations are provided on the following key areas: 
* Rider Distribution: examining the total number of bike-share users is divided between casual riders and members 
* Seasonal Riding Patterns: Insights into how rider activity changes throughout the year for both groups.
* Ride Duration: examining average ride by year and by day of the week times between casual riders and members.
* Weekly Ride Activity: An evaluation of ride counts by day of the week for each rider group.
* Popular Start and End Stations: Identification of the top stations used by casual riders and members.

## Data Structure & Information
Cyclistic’s dataset contains 5,743,278 rows and 13 columns, columns included in the dataset are as followed:
* Ride_id: Unique identifier for each ride.
* Rideable_type: Type of bike used (electric, classic, docked)
* Started_at: Date and time when the ride began.
* Ended_at: Date and time when the ride ended.
* Start_station_name: Name of the station where the ride began.
* Start_station_id: ID of the station where the ride began.
* End_station_name: Name of the station where the ride ended.
* End_station_id: ID of the station where the ride ended.
* Start_lat: Starting latitude.
* Start_lng: Starting longitude.
* End_lat: Ending latitude.
* End_lng: Ending longitude.
  
The dataset was cleaned and pre-processed using Python libraries such as Pandas and NumPy. Missing data regarding ‘end_station_name’ were handled using the KNeighborsClassifier machine learning model to ensure the dataset was complete for analysis. New columns were created to provide deeper insights during analysis. 

## Executive Summary
### Overview of Findings
The analysis reveals distinct differences in riding patterns between casual riders and members. Members outnumber casual riders by 1,643,974, and both groups show seasonal peaks in activity during the summer with casual riders reaching their highest in July and members peaking in August. Ride counts for both decline during fall and winter. Casual riders tend to have longer ride durations, averaging 28.20 minutes compared to members' 12.92 minutes. Weekly patterns show members riding more frequently on weekdays, peaking on Thursday, while casual riders are most active on weekends, especially Saturday. Station preferences also differ, with casual riders frequently starting at Streeter Dr & Grand Ave, while members prefer Clark St & Elm St. Ending station choices follow similar trends, with distinct preferences between the two groups.

Rider Distribution:
The data shows a significant difference between the number of casual riders and members, with members outnumbering casual riders by 1,643,974 riders.

Seasonal Riding Patterns:
Both casual riders and members exhibit increased activity during spring and summer. However, casual riders peak in July, while members peak in August. Both groups see a decline in ride counts during the fall and winter months.

Ride Duration:
Casual riders tend to have longer ride durations compared to members. The average ride time for casual riders is 28.20 minutes, whereas members average 12.92 minutes. Throughout the week, casual riders generally have rides exceeding 20 minutes, while members average below 13 minutes.

Weekly Ride Activity:
There are distinct patterns in ride activity between the two groups. Members’ ride counts are highest on weekdays, peaking on Thursday and tapering off over the weekend. Conversely, casual riders are more active on weekends, with their counts peaking on Saturday.

Popular Start and End Stations:
For casual riders, the most frequented starting station to casual rider's ride is Streeter Dr & Grand Ave, followed by Dusable Lake Shore Dr & Monroe St, Millennium Park, Theater on the Lake, and Michigan Ave & Oak St. As for end stations, Streeter Dr & Grand Ave emerges as the most popular end station, followed by Dusable Lake Shore Dr & Monroe St, Dusable Lake Shore Dr & North Blvd, Michigan Ave & Oak St, and Theater on the Lake.

Members, on the other hand, prefer starting station Clark St & Elm St followed by Clinton St & Washington Blvd, Wabash Ave & Grand Ave, Canal St & Adams St, and Dearborn St & Monroe St. For ending stations, Kingsbury St & Kinzie St is the most popular followed by Wilton Ave & Belmont Ave, Canal St & Adams St, LaSalle St & Illinois St, and Dearborn Pkwy & Delaware Pl.

## Recommendations
To address the question of how to convert casual riders into annual members, I have made three recommendations.

Targeted Membership Campaigns: Set up targeted membership ads during the months when casual riders are most active, specifically June, July, and August. Given that casual riders are particularly active on weekends, with peak activity on Saturdays, focus these ads on weekend days to maximize visibility and engagement. This strategy will capture the attention of casual riders during their highest activity periods and encourage them to sign up for annual memberships.

Strategic Station Marketing: Implementing membership advertisements at the top 3 most popular starting stations (Streeter Dr & Grand Ave, Dusable Lake Shore Dr & Monroe St, Millennium Park) and top 3 most popular ending stations (Streeter Dr & Grand Ave, Dusable Lake Shore Dr & Monroe St, Dusable Lake Shore Dr & North Blvd) could effectively encourage more casual riders to become members.

Highlighting Membership Value for Longer Rides: On average, casual riders ride for 28 minutes per trip. Highlighting the cost savings of a membership compared to day passes for longer rides could further incentivize casual riders to sign up for memberships.
