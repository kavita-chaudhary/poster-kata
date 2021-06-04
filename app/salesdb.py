#genration of salesDB with automatic genration of all the columns except film list and ss_id
import pandas as pd
from faker import Faker
import numpy as np
import random
import string

result=[]
fake = Faker()
nrow = 10
salseDBDF = pd.DataFrame()

salseDBDF['email'] = [fake.email()
              for _ in range(nrow)]

data = np.random.randint(5,30,size=20)
salseDBDF['quantity'] = pd.DataFrame(data, columns=['quantity'])

data = np.random.randint(1,3,size=20)
salseDBDF['price'] = pd.DataFrame(data, columns=['quantity'])

salseDBDF['sales_rep'] = [fake.email()
              for _ in range(nrow)]

for i in range(10):
    # get random string of length 4 without repeating letters
    result_str = ''.join(random.sample(string.ascii_lowercase, 4))
    result .append(result_str)

salseDBDF['promo_code'] = result

salseDBDF[['poster_content','ss_id']]= starShipDF[['name','ss_id']].sample(n=9)

salseDBDF

engine = sqlalchemy.create_engine("postgresql://postgres:NEWUSER123456#@localhost/salesdb")
con = engine.connect()
table_name1 ='STARSHIP_POSTER_SALES_T'
salseDBDF.to_sql(table_name1, con ,schema='sales_db',if_exists='replace')

##creation of customer table merging two datasets:salesDB and above creatd starship DF
result = pd.merge(starShipDF, salseDBDF[['quantity','price','promo_code','ss_id','poster_content']],how='inner' ,left_on=['ss_id','name'], right_on=['ss_id','poster_content'], )
del result["poster_content"]
result

#creation of starship table
engine = sqlalchemy.create_engine("postgresql://postgres:NEWUSER123456#@localhost/dw")
con = engine.connect()
table_name = 'STARSHIP_DETAILS_T'
result.to_sql(table_name, con ,schema='dw_starwars',if_exists='replace')