import sqlite3


conn = sqlite3.connect('Chinook_Sqlite.sqlite')


cursor = conn.cursor()

sel_date = '''
SELECT InvoiceDate, TrackId FROM Invoice
JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId
'''

sel_track = '''
SELECT Name, TrackId FROM Track
'''

cursor.execute(sel_date)
dates = cursor.fetchall()

cursor.execute(sel_track)
tracks = cursor.fetchall()
l = []
for track in tracks:
    for date in dates:
        if track[1] == date[1] and not(track[0] in l):
            if int(date[0][:4]) >= 2010:
                print(track[0])
                l.append(track[0])
conn.close()