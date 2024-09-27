import sqlite3
import re
con = sqlite3.connect("anime-list.db", check_same_thread=False)

def create_db():
    sql = """
CREATE TABLE animes (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR(255) NOT NULL,
link VARCHAR(255) NOT NULL,
genere VARCHAR(35) NOT NULL
)"""
    with con:
        cur = con.cursor()
        cur.execute(sql)
    print("\033[01;32m Tabela Criada!")


def neo(name:str, link:str, genere:str):
    sql = "INSERT INTO animes (name, link, genere) VALUES (?,?,?)"
    with con:
        cur = con.cursor()
        cur.execute(sql, (name, link, genere))
        con.commit()

def genero(genere:str):
    sql="SELECT * FROM animes WHERE genere=?"
    info = {}
    with con:
        cur = con.cursor()
        cur.execute(sql,(genere,))

        animename = cur.fetchall()
        for data in animename:
            info[data[1]] = data[2]

        return info


def show_all():
    sql = "SELECT * FROM animes"
    response = {}
    with con:
        cur = con.cursor()
        cur.execute(sql)
        todos = cur.fetchall()

        for nome in todos:
            response[nome[1]] = nome[2]

        return response


def delete(name):
    sql = "DELETE FROM animes WHERE name= ?"
    with con:
        cur = con.cursor()
        cur.execute(sql, (name,))
        con.commit()


if __name__ == "__main__":
    print("All Data In DB")
#    neo("", "", "ecchi")
#    delete("Jimihen!! Jimiko o Kae Chau Jun Isei Kouyuu")


    print("==============")

    print("\nAnime select to genero")
    ct = 0
    for i in genero("ecchi"):
        ct += 1
        print(f"[{ct}] - {i}")
