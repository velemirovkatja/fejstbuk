import bottle
import sqlite3

bottle.debug(True)
datoteka_baze = "knjiga_obrazov.sqlite"

@bottle.route('/prijatelji/<id>')
@bottle.view('prijatelji')
def prijatelji(id):
    c = baza.cursor()
    c.execute("""SELECT ime, priimek From osebe WHERE id = ?""", [id])
    
##    """SELECT osebe.ime, osebe.priimek FROM osebe
##       JOIN prijateljstva ON osebe.id = prijateljstva.drugi
##       WHERE prijateljstva.prvi = 2
##    """)
    
    oseba = c.fetchone()

    if oseba is None:
        c.close()
        return {'obstaja': False}
    else:
        (ime, priimek) = oseba
        c.execute(
        """SELECT osebe.ime, osebe.priimek
           FROM osebe JOIN prijateljstva ON osebe.id = prijateljstva.drugi
           WHERE prijateljstva.prvi = ?""", [id])
        prijatelji = c.fetchall()
        c.close()
        return {'obstaja': True, 'ime': ime, 'priimek': priimek, 'prijatelji': prijatelji}
    
##    seznam_imen = ", ".join(i + " " + p for (i, p) in c.fetchall())
##    print(seznam_imen)
##    return seznam_imen


baza = sqlite3.connect(datoteka_baze, isolation_level = None)


bottle.run(host='localhost', port=8080)


