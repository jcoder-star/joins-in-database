import sqlite3

database ="database.sqlite"
conn = sqlite3.connect(database)


print("connection successful")


import pandas as pd
tables =pd.read_sql("""
    SELECT *FROM sqlite_master WHERE type= "table";
                     """,conn)

print(tables)


joined_city =pd.read_sql("""
    SELECT Country.Country_id,Country.Country_Name,city.city_Name
    FROM Country
    INNER JOIN city
    ON Country.Country_id==city.Country_id                                          
                                              
                         """,conn)
print(joined_city)