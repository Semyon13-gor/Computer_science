import sqlite3


conn = sqlite3.connect('Chinook_Sqlite.sqlite')


cursor = conn.cursor()
sel_name = '''
SELECT FirstName, LastName, COUNT(InvoiceId) From Customer
JOIN Invoice ON Invoice.CustomerId = Customer.CustomerId
GROUP BY Customer.CustomerId
'''
cursor.execute(sel_name)
names = cursor.fetchall()

for name in names:
    print(name)



conn.close()