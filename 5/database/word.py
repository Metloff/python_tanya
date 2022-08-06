import sqlite3

class Word:
    def __init__(self):
        self.con = sqlite3.connect('dic.db')
       
    def initdb(self):
        try:
            cur = self.con.cursor()
            # Create table
            cur.execute('''CREATE TABLE IF NOT EXISTS dictionary
                        (word text, translate text)''')

        finally:
            # Save (commit) the changes
            self.con.commit()

    def get_translation(self, en_w):
        cur = self.con.cursor()
        return cur.execute("SELECT * FROM dictionary WHERE word = ?", (en_w,)).fetchall()

    def write_translation(self, en_w, ru_w):
        cur = self.con.cursor()
        cur.execute("insert into dictionary values (?, ?)", (en_w, ru_w))
        # Save (commit) the changes
        self.con.commit()