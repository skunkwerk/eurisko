from cloudant.account import Cloudant
client = Cloudant('eurisko', 'nox721!carpe', account='eurisko')
# or using url
# client = Cloudant(USERNAME, PASSWORD, url='https://acct.cloudant.com')

# Connect to the account
client.connect()

# Perform client tasks...
session = client.session()
print session['userCtx']['name']
print client.all_dbs()

db = client['eurisko']

inserted_counter = 0

# now connec to local sqlite3
def parse_results(results):
    """
    """
    for result in results:
        print 'parsing result'
        data = {}
        data['customer_id'] = 0
        data['tags'] = []
        data['title'] = result[0]
        data['content'] = result[1]
        data['timestamp'] = result[2]
        insert_to_cloudant(data)

def insert_to_cloudant(data):
    """
    """
    global inserted_counter
    # Create document content data
    # Create a document using the Database API
    my_document = db.create_document(data)

    # Check that the document exists in the database
    if my_document.exists():
        print 'SUCCESS!!'
        inserted_counter += 1

import sqlite3
conn = sqlite3.connect('database-fts.sqlite')
c = conn.cursor()

c.execute("SELECT title, content, timestamp FROM notes WHERE title='2visit'")
results = c.fetchall()
parse_results(results)

# Disconnect from the account
client.disconnect()

print inserted_counter