# sqlalchemy-challenge
SQLAlchemy Homework - Surfs Up!<p></p>
Before You Begin<p></p>
<ol>
  <li>Create a new repository for this project called sqlalchemy-challenge. Do not add this homework to an existing repository. </li>
  <li>Clone the new repository to your computer.</li>
  <li>Add your Jupyter notebook and app.py to this folder. These will be the main scripts to run for analysis.</li>
  <li>Push the above changes to GitHub or GitLab.</li>
</ol>
<hr><p></p>
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.
<hr><p></p>
Step 1 - Climate Analysis and Exploration<br>
To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

<ul>
<li>Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.</li>
<li>Use SQLAlchemy create_engine to connect to your sqlite database.</li>
<li>Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.</li>
<li>Link Python to the database by creating an SQLAlchemy session.</li>
<li>Important Don't forget to close out your session at the end of your notebook.</li>
</ul>

Precipitation Analysis<br>
<ul>
  <li>Start by finding the most recent date in the data set.</li>
<li>Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. Note you do not pass in the date as a variable to your query.</li>
<li>Select only the date and prcp values.</li>
<li>Load the query results into a Pandas DataFrame and set the index to the date column.</li>
<li>Sort the DataFrame values by date.</li>
<li>Plot the results using the DataFrame plot method.</li>
<li>Use Pandas to print the summary statistics for the precipitation data.</li>
</ul>
<br>
Station Analysis<br>
<ul>
<li>Design a query to calculate the total number of stations in the dataset.</li>
<li>Design a query to find the most active stations (i.e. which stations have the most rows?).</li>
  <ul>
    <li>List the stations and observation counts in descending order.</li>
    <li>Which station id has the highest number of observations?</li>
    <li>Using the most active station id, calculate the lowest, highest, and average temperature.</li>
    <li>Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.</li>
  </ul>
  <li>Design a query to retrieve the last 12 months of temperature observation data (TOBS).</li>
  <ul>
    <li>Filter by the station with the highest number of observations.</li>
    <li>Query the last 12 months of temperature observation data for this station.</li>
    <li> Plot the results as a histogram with bins=12.</li>
    <li>Close out your session.</li>
  </ul
<hr><p></p>
Step 2 - Climate App<br>
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.
<ul>
  <li>Use Flask to create your routes.</li>
<br>
Routes
<ul>
  <li>/</li>
  </ul>
  <ul>
    <li>Home page.</li>
    <li>List all routes that are available.</li>
<ul>
  <li>/api/v1.0/precipitation</li>
    
<ul>
  <li>Convert the query results to a dictionary using date as the key and prcp as the value.</li>
  <li>Return the JSON representation of your dictionary.</li>

<li>/api/v1.0/stations</li>
  <ul>
    <li>Return a JSON list of stations from the dataset.</li>



/api/v1.0/tobs


Query the dates and temperature observations of the most active station for the last year of data.


Return a JSON list of temperature observations (TOBS) for the previous year.




/api/v1.0/<start> and /api/v1.0/<start>/<end>


Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.


When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.





Hints


You will need to join the station and measurement tables for some of the queries.


Use Flask jsonify to convert your API data into a valid JSON response object.




Bonus: Other Recommended Analyses


The following are optional challenge queries. These are highly recommended to attempt, but not required for the homework.


Use the provided temp_analysis_bonus_1_starter.ipynb and temp_analysis_bonus_1_starter starter notebooks for each bonus challenge.



Temperature Analysis I


Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?


Use pandas to perform this portion.


Convert the date column format from string to datetime.


Set the date column as the DataFrame index


Drop the date column




Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.


Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?



Temperature Analysis II


You are looking to take a trip from August first to August seventh of this year, but are worried that the weather will be less than ideal. Using historical data in the dataset find out what the temperature has previously looked like.


The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.


Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from a previous year (i.e., use "2017-08-01").


Plot the min, avg, and max temperature from your previous query as a bar chart.


Use "Trip Avg Temp" as the title.


Use the average temperature as the bar height (y value).


Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).






Daily Rainfall Average


Now that you have an idea of the temperature lets check to see what the rainfall has been, you don't want a when it rains the whole time!


Calculate the rainfall per weather station using the previous year's matching dates.

Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.



Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures. You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic TOBS that match that date string.


Set the start and end date of the trip.


Use the date to create a range of dates.


Strip off the year and save a list of strings in the format %m-%d.


Use the daily_normals function to calculate the normals for each date string and append the results to a list called normals.




Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.


Use Pandas to plot an area plot (stacked=False) for the daily normals.



Close out your session.



Copyright
Trilogy Education Services © 2020. All Rights Reserved.
