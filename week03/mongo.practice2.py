from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
target_war_E = db.movies.find_one({'title':'월-E'})
target_star = target_war_E['star']

same_movies = list(db.movies.find({'star':target_star}))

for movie in same_movies:
    print(movie['title'])