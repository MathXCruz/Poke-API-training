import sqlite3

conn = sqlite3.connect('poke_api_training.db')
c = conn.cursor()

c.execute(
    """
          CREATE TABLE IF NOT EXISTS pokemon
          ([id] INTEGER PRIMARY KEY, [name] TEXT, [types] TEXT, \
              [weight] REAL, [height] REAL, [sprite] TEXT)
          """
)
