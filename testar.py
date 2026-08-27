import sqlite3 

con = sqlite3.connect('banco.db')

cursor = con.cursor()

cursor.execute("""
    ALTER TABLE note ADD COLUMN favoritado BOOLEAN DEFAULT FALSE;
""")
con.commit()
con.close()