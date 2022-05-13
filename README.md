# Evreka Technical Question Set - Question 2

I implemented all relevant functionality inside api app at BASE_DIR.
The function that return requested data is in BASE_DIR/api/views.py

## Small Description

I started with creating models as it was written on question text and added proper attribute fields and methods (format_date method that gives proper date format like in the examples) to use later on. Afterward, I imported rest_framework to visualize and serialize the data easily. Then, I created the function latest_records that gives the query_set of requested data. The function calculates the 48 hours of range between now and the past. Then filters the data. After getting all the navigation records for the last 48 hours, I ordered them with respect to datetime in reverse order (descending) and then picked the distinct vehicle_plate ones.

## Suggestions
- a
- a
- a
