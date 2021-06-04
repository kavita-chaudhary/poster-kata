import pandas as pd
from faker import Faker
import numpy as np
import random
import string

result=[]

fake = Faker()

nrow = 5

dataf = pd.DataFrame()


dataf['email'] = [fake.email()
              for _ in range(nrow)]

data = np.random.randint(5,30,size=20)
dataf['quantity'] = pd.DataFrame(data, columns=['quantity'])

data = np.random.randint(1,3,size=20)
dataf['price'] = pd.DataFrame(data, columns=['quantity'])

dataf['sales_rep'] = [fake.email()
              for _ in range(nrow)]

for i in range(5):
    # get random string of length 6 without repeating letters
    result_str = ''.join(random.sample(string.ascii_lowercase, 4))
    result .append(result_str)

dataf['promo_code'] = result

dataf[['poster_content','ss_id']]= starShipDF[['name','ss_id']].sample(n=7)

dataf

engine = sqlalchemy.create_engine("postgresql://postgres:NEWUSER123456#@localhost/salesdb")
con = engine.connect()
table_name1 ='STARSHIP_POSTER_SALES_T'
dataf.to_sql(table_name1, con ,schema='sales_db',if_exists='replace')