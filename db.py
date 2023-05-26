from dotenv import load_dotenv
load_dotenv()
import os
import mysql.connector

connection = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USERNAME"),
  passwd=os.getenv("DB_PASSWORD"),
  db=os.getenv("DB_DATABASE"),
  autocommit = True,
)

cursor = connection.cursor();

def getCities():
  cursor.execute("SELECT * FROM TRAJET;")
  pairs = []
  cities = set()
  for row in cursor:
    city1 = row[0].split(",")
    city2 = city1[1].strip()
    city1 = city1[0].strip()
    cities.add(city1)
    cities.add(city2)
    pairs.append(((city1, city2), row[1]))

  return cities, pairs;
def getCitiesPairs():
    cursor.execute("SELECT * FROM TRAJET;")
    pairs_national = []
    pairs_regional = []
    pairs_non_national = []
    pairs_non_regional = []
    cities = set()
    for row in cursor:
        city1 = row[0].split(",")
        city2 = city1[1].strip()
        city1 = city1[0].strip()
        cities.add(city1)
        cities.add(city2)
        if row[2]:
            pairs_national.append(((city1, city2), row[1]))
        else:
            pairs_non_national.append(((city1, city2), row[1]))
        if row[3]:
            pairs_regional.append(((city1, city2), row[1]))
        else:
            pairs_non_regional.append(((city1, city2), row[1]))
    return cities, pairs_national, pairs_regional, pairs_non_national, pairs_non_regional


def getCout():
    cursor.execute("SELECT * FROM COUT;")
    cout_r = 0
    cout_n = 0
    for row in cursor:
        cout_r = row[0]
        cout_n = row[1]
    return cout_r, cout_n