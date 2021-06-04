# poster-kata

## DataOps Challenge
### Star wars posters
​
## Recommended Tools
### Language( : Python + SQL
### github.com - repo `poster-kata`
### travis-ci -  for CI/CD
### PostgresQL - for DW and salesdb

## Instructions
###### We want for you to show how to automate pulling data from two sources to get a merged view of the data.
###### You should use docker/docker-compose to create your fake customer database (named `salesdb`), and a separate merged database (named `dw`).  You will use data from the https://swapi.dev/ API as well, to lookup missing product information and filter out certain kinds of items.
​
###### We will be looking for realistic looking data and automation around its generation.
​
### Requirements for dw
### Please extract, transform, then load (ETL) the data into the `dw` database with the following requirements in mind:
### • "We only care about starship posters, though we sell starship, character and planet posters"
### • "We need to know which films the ship appears in and when the film was made to understand potential demographic correlations."
### • "We want to be able to summarize the data."
### • "Customer emails should never be ingested."
### • "We only want to ingest data relevant to our mission."


### The Starwars:

### Target -- dw ( having three tables, you will get the ,merged view of output)
### Source -- db( having one table )

### source -- the source code genration table  was automatic and radom/fake.

### API -- two API's is taken care ( startships and films)
### store the starships with creating an id .
### store the films with creating an id.
### New table xref which is basically showing relationship between starships and films.

## commands to use :
## docker-compose up -d --build
