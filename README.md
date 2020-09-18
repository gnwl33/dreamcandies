# DreamCandies

Script is in 'dreamcandies.ipynb'

## Process:
After reading the specifications, I came up with the solution that the customer ids from the customer_sample.csv could be used to identify and extract the relevant rows from customer.csv as well as invoice.csv, and the invoice ids of the extracted rows from invoice.csv could be used to extract from invoice_item.csv. I then researched efficient ways to read and write csvs. Pandas is a popular choice, but it seemed that csv was faster (given that all of the data fields are treated as strings). In terms of searching through the data, the best we can do for unsorted data is O(n) by going line by line. If the data was sorted, we could use binary search for O(logn) time complexity. However, we would have to store all the data at once in a dataframe or break it into chunks, which would increase the runtime. And if the data was stored in a database, querying would be faster. Initially, I thought of storing the customer and invoice ids in lists but realized sets would be faster with O(1) lookups when searching through the data. I also added more specific comments in the code.
