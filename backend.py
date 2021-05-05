import pymysql

mypass = "password_here"
mydatabase="database_name_here"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

try:
    cur.execute("USE Music;")
    cur.execute('''CREATE TABLE Artist(
                id integer auto_increment,
                artist_name varchar(50) unique,
                primary key(id));''')
    cur.execute('''CREATE TABLE Genre(
                id integer auto_increment,
                genre_name varchar(50) unique,
                primary key(id));''')
    cur.execute('''CREATE TABLE Album(
                id integer auto_increment,
                album_name varchar(50) unique,
                artist_id integer,
                primary key(id),
                foreign key(artist_id) references artist(id) on delete cascade);''')
    cur.execute('''CREATE TABLE Track(
                title varchar(50) unique,
                album_id integer,
                genre_id integer,
                artist_id integer,
                rlsyr integer,
                primary key(title),
                foreign key(album_id) references album(id) on delete cascade,
                foreign key(genre_id) references genre(id) on delete cascade,
                foreign key(artist_id) references artist(id) on delete cascade);''')
    con.commit()
    print("Done Papi!")
except:
    print('Database Connection Failed!')








