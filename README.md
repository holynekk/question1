# Evreka Technical Question Set - Question 1

I implemented all relevant functionality inside api app at BASE_DIR.

The function that return requested data is in BASE_DIR/api/views.py

## Small Description

I started with creating models as it was written on question text and added proper attribute fields and methods (format_date method that gives proper date format like in the examples) to use later on. Afterward, I imported rest_framework to visualize and serialize the data easily. Then, I created the function latest_records that gives the query_set of requested data. The function calculates the 48 hours of range between now and the past. Then filters the data. After getting all the navigation records for the last 48 hours, I ordered them with respect to datetime in reverse order (descending) and then picked the distinct vehicle_plate ones.

If you hit the api endpoint at /api/recent-records , you can see the requested data with django rest framework interface.

## Suggestions
- If a vehicle creates a new NavigationRecord instance every time it reaches another destination or any arbitrary point on the road, there will be a huge amount of common queries after some time. This will have an impact on performance. If we don't need to consider previous navigation information for a vehicle, we can simply update the current one whenever it's needed. This way, we only need to filter datetime for 48 hours of range, and we will get the requested data.
- Instead of holding datetime in NavigationRecord model, we can have it inside the Vehicle model. With that update on database models, the content of the data will not change, but it will represent the last time that specific vehicle changed its position. This way, we can directly get the navigation records without sorting datetime attributes by just finding vehicles that moved in the last 48 hours.

These are the ones I can suggest. Since the models and the queries are not complex enough to have a big impact on the performance, I think changing the way it holds the information is enough. It also depends on the program's overall functionality, but we don't have in-depth information on that. Therefore, changing models and their functionality in this way is possible.