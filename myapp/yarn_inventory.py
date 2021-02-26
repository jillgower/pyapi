#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_yarn():
    return render_template('newyarn.html')


@app.route('/yarninv', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        data = request.json
        if data:
            print(data)
            br = data["brand"]
            color = data["colorway"]
            ln = data["length"]
            wt = data["weight"]
            qty = data["qty"]
        else:
            br = request.form["brand"]
            color = request.form["colorway"]
            ln = request.form["length"]
            wt = request.form["weight"]
            qty = request.form["qty"]
        try:
            with sql.connect("database.db") as con:
                cur = con.cursor()
                print(br, color, ln, wt, qty)
                cur.execute("INSERT INTO yarn (br,color,ln,wt,qty) VALUES (?,?,?,?,?)", (br, color, ln, wt, qty))
                con.commit()
                msg = "Record successfully added"
        except sql.OperationalError as err:
            try:
                con.rollback()
            except Exception:
                pass
            msg = f"error in insert operation: {err}"
        finally:
            con.close()
            return render_template("result.html", msg=msg)


def get_yarn():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from yarn")

    rows = cur.fetchall()
    return rows


@app.route('/list')
def list_yarn():
    rows = get_yarn()
    return render_template("list.html", rows=rows)


@app.route('/yarn')
def json_students():
    rows = get_yarn()
    data = []
    for row in rows:
        row_data = {}
        print(row)
        row_data["brand"] = row["brand"]
        row_data["colorway"] = row["colorway"]
        row_data["length"] = row["length"]
        row_data["weight"] = row["weight"]
        row_data["qty"] = row["qty"]
        data.append(row_data)
    return jsonify(data)


if __name__ == '__main__':
    try:
        conn = sql.connect('database.db')
        print("Opened database successfully")
                                                        #(br,color,ln,wt,qty)
        conn.execute('CREATE TABLE IF NOT EXISTS yarn (br TEXT, color TEXT, ln INT, wt TEXT, qty INT)')
        print("Table created successfully")
        conn.close()
        app.run(host="0.0.0.0", port=2224, debug=True)
    except Exception:
        print("App failed on boot")
