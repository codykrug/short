import csv
import sqlite3

conn = sqlite3.connect('oc.db')
c = conn.cursor()

c.execute('''CREATE TABLE Owner
             (ParcelNumber TEXT, OwnerName TEXT, PropertyAddress TEXT, City TEXT, LandUseCode INT, SaleDate DATE, SalePrice INT, TotalRecordCount INT)''')

#load data and bulk insert

with open('Records.csv','r') as fin:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['ParcelNumber'], i['OwnerName'], i['PropertyAddress'], i['City'], i['LandUseCode'], i['SaleDate'], i['SalePrice'], i['TotalRecordCount']) for i in dr]

c.executemany("INSERT INTO Owner (ParcelNumber, OwnerName, PropertyAddress, City, LandUseCode, SaleDate, SalePrice, TotalRecordCount) VALUES (?,?,?,?,?,?,?,?);", to_db)

conn.commit()
conn.close()
