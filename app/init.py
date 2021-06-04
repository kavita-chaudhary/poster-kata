#packgaes for 
import json
import requests
import pandas as pd
import re



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


starShipDF

