#import psycopg2 as pg
#from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
import sqlalchemy


engine = sqlalchemy.create_engine("postgresql://postgres:NEWUSER123456#@localhost/dw")
con = engine.connect()
print(engine.table_names())
#handel if the data alreay exists.
table_name = 'STARSHIP_DETAILS_T'
starShipDF.to_sql(table_name, con ,schema='dw_starwars',if_exists='replace')
le_name1 ='STARSHIP_FILM_RELATION_T'
starshipAndFilmRelDF.to_sql(table_name1, con ,schema='dw_starwars',if_exists='replace')
table_name3 ='FILMS_DETAILS_T'
filmsDF.to_sql(table_name3, con ,schema='dw_starwars',if_exists='replace')