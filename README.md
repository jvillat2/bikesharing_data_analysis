# Project Description
Conducted an in-depth analysis of Cyclistic bike-share 12 month data to uncover behavioral patterns and usage differences between members and casual riders. Used Python libraries (Pandas, NumPy, Matplotlib) for exploration, data cleaning, data manipulation, feature engineering, visualization. Used a Machine learning model (KNeighborsClassifier) to handle missing values during data cleaning. Provided actionable recommendations to convert casual riders into annual members based on the findings.

This notebook is 9 parts:
- Introduction
- Loading Dataset
- Exploring data
- Data Cleaning
- Data Manipulation and Feature Engineering
- Analysis
- Visalization
- Finding
- Recommendations

  # Summary of Insights
Rider Distribution:
* The data shows a significant difference between the number of casual riders and members, with members outnumbering casual riders by 1,643,974 riders.
  
Seasonal Riding Patterns:
* Both casual riders and members exhibit increased activity during spring and summer. However, casual riders peak in July, while members peak in August. Both groups see a decline in ride counts during the fall and winter months.

Ride Duration:
* Casual riders tend to have longer ride durations compared to members. The average ride time for casual riders is 28.20 minutes, whereas members average 12.92 minutes. Throughout the week, casual riders generally have rides exceeding 20 minutes, while members average below 13 minutes.

Weekly Ride Activity:
* There are distinct patterns in ride activity between the two groups. Members’ ride counts are highest on weekdays, peaking on Thursday and tapering off over the weekend. Conversely, casual riders are more active on weekends, with their counts peaking on Saturday.

Popular Start and End Stations:
* For casual riders, the most frequented starting station to casual rider's ride is Streeter Dr & Grand Ave, followed by Dusable Lake Shore Dr & Monroe St, Millennium Park, Theater on the Lake, and Michigan Ave & Oak St. As for end stations, Streeter Dr & Grand Ave emerges as the most popular end station, followed by Dusable Lake Shore Dr & Monroe St, Dusable Lake Shore Dr & North Blvd, Michigan Ave & Oak St, and Theater on the Lake.

* Members, on the other hand, prefer starting station Clark St & Elm St followed by Clinton St & Washington Blvd, Wabash Ave & Grand Ave, Canal St & Adams St, and Dearborn St & Monroe St. For ending stations, Kingsbury St & Kinzie St is the most popular followed by Wilton Ave & Belmont Ave, Canal St & Adams St, LaSalle St & Illinois St, and Dearborn Pkwy & Delaware Pl.

  # Recommendations 
To address the question of how to convert casual riders into annual members, I have made three recommendations. 
* Targeted Membership Campaigns: Set up targeted membership ads during the months when casual riders are most active, specifically June, July, and August. Given that casual riders are particularly active on weekends, with peak activity on Saturdays, focus these ads on weekend days to maximize visibility and engagement. This strategy will capture the attention of casual riders during their highest activity periods and encourage them to sign up for annual memberships.
* Strategic Station Marketing: Implementing membership advertisements at the top 3 most popular starting stations (Streeter Dr & Grand Ave, Dusable Lake Shore Dr & Monroe St, Millennium Park) and top 3 most popular ending stations (Streeter Dr & Grand Ave, Dusable Lake Shore Dr & Monroe St, Dusable Lake Shore Dr & North Blvd) could effectively encourage more casual riders to become members.
* Highlighting Membership Value for Longer Rides: On average, casual riders ride for 28 minutes per trip. Highlighting the cost savings of a membership compared to day passes for longer rides could further incentivize casual riders to sign up for memberships.
