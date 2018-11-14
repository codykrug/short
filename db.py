import sqlite3

conn = sqlite3.connect('Homes.db')

c = conn.cursor()

createHomes = "CREATE TABLE Homes(Parcel TEXT, Name TEXT, Address TEXT, LandUseCode INT, SaleDate DATE, SalePrice INT, TotalRecordCount INT)"

c.execute(createHomes)

#read file

data = open('os.txt', 'r')

#bulk insert

c.executemany("insert into Homes(Parcel, Name, Address, LandUseCode, SaleDate, SalePrice, TotalRecordCount) values (?,?,?,?,?,?,?)", Homes)

conn.close()
