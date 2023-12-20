import requests
import psycopg2
import os
from dotenv import load_dotenv
from random import sample

# cur = conn.cursor()

# create_query = 'CREATE TABLE countries (id serial primary key, name varchar, capital varchar, flag varchar, subregion varchar, population integer)'
# cur.execute(create_query)
# conn.commit()

# # <!-- Instructions
# # Using this REST Countries API, create the functionality which will write 
# 10 random countries to your database.
# # print(response.text)
# # These are the attributes which you should populate your tables with: name, capital, 
#  flag, subregion, population. -->
# # print(response.json())
# # print(response.headers)

#parameters = {"lat": 31.771959, "lon": 35.217018}


# print(data[0])



class api_to_db:
    def api(self):
        self.name =[]
        self.capital =[]
        self.flag =[]
        self.subregion =[]
        self.population =[]
        response = requests.get("https://restcountries.com/v3.1/all")
        data = response.json()
        random_countries = sample(data, 10)
        for country in random_countries:
            self.name.append(country['name']['official'])
            self.capital.append(country['capital'][0])
            self.flag.append(country['flag'])
            self.subregion.append(country['subregion'])
            self.population.append(country['population'])

    def db(self): 
        load_dotenv()  
        conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        dbname=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT'))

        cur = conn.cursor()

        delete_query = 'DELETE from countries'
        cur.execute(delete_query)
        conn.commit()
        for i in range(len(self.name)):
            insert_query = '''
                INSERT INTO countries (name, capital, flag, subregion, population)
                VALUES (%s, %s, %s, %s, %s)'''
            data_to_insert = (
                self.name[i],
                self.capital[i],
                self.flag[i],
                self.subregion[i],
                self.population[i])
            cur.execute(insert_query, data_to_insert)
            conn.commit()
                            

        # cur.close()
        # conn.close()



countries = api_to_db()
countries.api()
countries.db()

select_query = 'SELECT * from countries'



# print(data[0])
# # >> <class 'dict'>

# print(data["response"][0])

# response = requests.get("http://api.open-notify.org/astros.json")
# data = response.text
# print(response.request.url)
# print(response.request.body)

#Use the Chuck Norris API https://api.chucknorris.io/ to retrieve some jokes in a specific category

# Instructions
# Using this REST Countries API, create the functionality which will write 10 random 
# countries to your database.

# These are the attributes which you should populate your tables with: name, capital, 
# flag, subregion, population.