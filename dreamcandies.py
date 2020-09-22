import csv
import time
import sys

args = sys.argv[1:]
if len(args) == 3:
    cust, inv, inv_item = sys.argv[1:]
else:
    files = input('Input the 3 file names, separated by spaces:\n').split(' ')
    if len(files) == 3:
        cust, inv, inv_item = files
    else:
        cust, inv, inv_item = 'customer', 'invoice', 'invoice_item'
    
start_time = time.time()
# two sets to store ids and provide O(1) lookups
customer_ids = set()
invoice_ids = set()

# assume filename for sample input is 'customer_sample.csv'
# and filenames for full extraction files are 'customer.csv', 'invoice.csv', 'invoice_item.csv'
with open('customer_sample.csv') as df:
    # iterator for csv to get sample customer ids
    customer_samples = csv.reader(df)
    # skip header
    next(customer_samples)
    for row in customer_samples:
        customer_ids.add(row[0])

# function to extract data from larger files
def extract_file(filename):
    if (filename == 'invoice_item'):
        ids = invoice_ids
    else:
        ids = customer_ids

    with open('{}.csv'.format(filename)) as df1:
        # read from larger file
        data = csv.reader(df1)
        with open('{}_extract.csv'.format(filename), mode='w') as df2:
            fieldnames = next(data)
            # extract/write to smaller file
            data_extract = csv.writer(df2, quoting=csv.QUOTE_ALL)
            data_extract.writerow(fieldnames)
            # assuming that there is only one row per customer in customer.csv, keep track of ids seen
            # (there are multiple entries per customer_id/invoice_id for invoice.csv and invoice_item.csv)
            id_count = 0
            for row in data:
                # (Since the files are ASCII, I'm using standard quotes. When copying the example data 
                # from the pdf, the quote marks did not seem standard.)
                # see if customer_id (for customer & invoice) or invoice_id (for invoice_item) in ids set
                if row[0] in ids:
                    data_extract.writerow(row)
                    # get invoice_id and add to set
                    if filename == 'invoice':
                        invoice_ids.add(row[1])
                    elif filename == 'customer':
                        id_count += 1
                        # if all customer_ids seen, no need to search anymore
                        if id_count == len(customer_ids):
                            break

extract_file(cust)                   
extract_file(inv)
extract_file(inv_item)
print("--- %s seconds ---" % (time.time() - start_time))