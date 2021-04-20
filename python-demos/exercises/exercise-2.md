# Exercise 2

1. Install the "requests" package from PyPi.org. We did this yesterday, but if you did not do it, then you will need to install it now.

2. Using the "requests" package API, call the following URL for each date returned from the "business_days" function.

https://api.ratesapi.io/api/2019-01-01?base=USD&symbols=EUR

Iterate over a range of 20 business days, and run the above request for each day.

3. Create a list of text values from each response. The text value is formatted as JSON. Do not parse the JSON. Just put each JSON response in the list.

4. Display each list item in the console.

5. Test your rates client code with both APIs. Ensure both APIs work with no code changes. Also, record the time it takes to call each API for all of the business days.
