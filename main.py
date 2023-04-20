import os
import sqlite3

import flask

from services import customers_generator, tracks_generator


app = flask.Flask(__name__)


@app.route("/")
def index_view():
    return flask.render_template("index.html")


@app.route("/names/")
def customers_names_view():
    con = sqlite3.connect("music_app.db")
    cur = con.cursor()
    r = cur.execute("SELECT DISTINCT first_name FROM customers")
    names = r.fetchall()
    return flask.render_template("names.html", names=names)


@app.route("/tracks/")
def count_tracks_view():
    con = sqlite3.connect("music_app.db")
    cur = con.cursor()
    r = cur.execute("SELECT COUNT(*) FROM tracks")
    count = r.fetchall()
    return flask.render_template("count_tracks.html", count=count)


@app.route("/tracks-sec/")
def tracks_view():
    con = sqlite3.connect("music_app.db")
    cur = con.cursor()
    r = cur.execute("SELECT track_name, track_time FROM tracks")
    tracks = r.fetchall()
    return flask.render_template("tracks-sec.html", tracks=tracks)


def main():
    if not os.path.exists("music_app.db"):
        con = sqlite3.connect("music_app.db")
        cur = con.cursor()

        cur.execute("""
        CREATE TABLE customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            first_name TEXT NOT NULL, 
            last_name TEXT NOT NULL, 
            email TEXT NOT NULL)
        """)

        cur.execute("""
        CREATE TABLE tracks(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            track_name TEXT NOT NULL,
            track_time INTEGER NOT NULL)
        """)

        customers = customers_generator.generate_customers()
        cur.executemany("INSERT INTO customers VALUES(NULL, :first_name, :last_name, :email)", customers)

        tracks = tracks_generator.generate_tracks()
        cur.executemany("INSERT INTO tracks VALUES(NULL, :track_name, :track_time)", tracks)

        con.commit()
    app.run()


if __name__ == "__main__":
    main()
