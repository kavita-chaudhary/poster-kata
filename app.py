#packgaes for 
import json
import requests
import pandas as pd
import re
import sqlalchemy
from faker import Faker
import numpy as np
import random
import string



#constant value and link required.
GetURLStar='http://swapi.dev/api/starships/'
GetURLfilms="http://swapi.dev/api/films/"
respStarshipList = []
respStarshipAndFilmRelationList = []
respFilmsList = []
filmUrlRegex ="http:\/\/swapi.dev\/api\/films\/(\d+)"




# Call a given link.
# Input: API link to ping

def callAPI(link):
    #print(link)
    response = requests.get(link)
    return response

# method to form starships-films relation List
def buildStarShipFilmRelationList(idx,filmList):
    for filmUrl in filmList:
        #print(filmUrl)
        x = re.search(filmUrlRegex, filmUrl)
        if x:
            #print(x.group(1))
            ssDict = {"ss_id":idx, "f_id":x.group(1)}
            respStarshipAndFilmRelationList.append(ssDict)
            getFilmsList(x.group(1),filmUrl)
        else:
            print("No match")

            
# method to form films list 
def getFilmsList(f_id,filmUrl):
            film_Response= callAPI(filmUrl)
            if(film_Response.status_code != 200):
                print(film_Response.status_code)
                pass
            filmJsonResponse = json.loads(film_Response.text)
            filmJsonResponse['f_id']= f_id
            respFilmsList.append(filmJsonResponse)
            
#starship genration        
x = range(1, 16)
for i in x:
    apiResponse = callAPI(GetURLStar + str(i) + "/")
    if(apiResponse.status_code != 200):
        print(apiResponse.status_code)
        continue
    jsonResponse = json.loads(apiResponse.text)
    jsonResponse['ss_id']= i
    #print(jsonResponse)
    buildStarShipFilmRelationList(i,jsonResponse.get('films'))
    jsonResponse.pop('films',None)
    respStarshipList.append(jsonResponse)
    
    
 #creation of startship DF   
starShipDF=pd.DataFrame(respStarshipList)
starShipDF=starShipDF[['ss_id','name', 'model','manufacturer', 'crew','passengers','starship_class']]    
print(starShipDF)

#creation of XREF starshipANDFilm DF
starshipAndFilmRelDF=pd.DataFrame(respStarshipAndFilmRelationList)
print(starshipAndFilmRelDF)

#creation of film DF
filmsDF=pd.DataFrame(respFilmsList)
filmsDF=filmsDF[['f_id','title','release_date']].drop_duplicates(['f_id','title','release_date'])
print(filmsDF)


###loading tables dw

engine = sqlalchemy.create_engine("postgresql://postgres:NEWUSER123456#@localhost/dw")
con = engine.connect()
print(engine.table_names())

table_name1 ='STARSHIP_FILM_RELATION_T'
starshipAndFilmRelDF.to_sql(table_name1, con ,schema='dw_starwars',if_exists='replace')

table_name3 ='FILMS_DETAILS_T'
filmsDF.to_sql(table_name3, con ,schema='dw_starwars',if_exists='replace')


####salesdb  loading with dummy fake data and creation of starship table

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





    
    