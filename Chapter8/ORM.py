import sqlite3

# Создание класса для представления альбома
class Album:
    def __init__(self, album_id, title, artist_id):
        self.album_id = album_id
        self.title = title
        self.artist_id = artist_id

    def __repr__(self):
        return f"Album(id={self.album_id}, title='{self.title}', artist_id={self.artist_id})"

# Создание класса для представления исполнителя
class Artist:
    def __init__(self, artist_id, name):
        self.artist_id = artist_id
        self.name = name

    def __repr__(self):
        return f"Artist(id={self.artist_id}, name='{self.name}')"

# Функция для подключения к базе данных
def get_connection(db_file):
    return sqlite3.connect(db_file)

# Функция для получения всех альбомов
def get_all_albums(connection):
    cursor = connection.cursor()
    sel_alb = """SELECT Title FROM Album"""
    cursor.execute(sel_alb)
    titles = cursor.fetchall()
    for title in titles:
        print(title)

# Функция для получения исполнителей
def get_all_artists(connection):
    cursor = connection.cursor()
    sel_art = """SELECT Name FROM Artist"""
    cursor.execute(sel_art)
    names = cursor.fetchall()
    for name in names:
        print(name)

# Функция для получения треков, выпущенных после 2010 года
def get_tracks_after_2010(connection):
    cursor = connection.cursor()
    sel_track = """SELECT TrackId FROM InvoiceLine
    JOIN Invoice ON Invoice.InvoiceId = InvoiceLine.InvoiceId
    WHERE InvoiceDate >= 2010-01-01 
    """
    cursor.execute(sel_track)
    tracksid = cursor.fetchall()
    for id in tracksid:
        sel_name = """SELECT Name FROM Track Where TrackId = ?"""
        cursor.execute(sel_name, id)
        name = cursor.fetchall()
        print(name)


