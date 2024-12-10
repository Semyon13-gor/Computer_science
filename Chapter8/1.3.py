import sqlite3


conn = sqlite3.connect('Chinook_Sqlite.sqlite')


cursor = conn.cursor()

sel_cin = '''
SELECT AlbumId, InvoiceId FROM InvoiceLine
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
'''
cursor.execute(sel_cin)
cins = cursor.fetchall()

sel_alb = '''
SELECT Title, AlbumId FROM Album
'''
cursor.execute(sel_alb)
albs = cursor.fetchall()

lcins = set(cins)
for alb in albs:
    count_buy = 0
    for cin in lcins:
        if alb[1] == cin[0]:
            count_buy += 1
    print(alb[0], count_buy)



conn.close()