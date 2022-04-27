from flask import Flask, request
from elasticsearch import Elasticsearch
import io
import json


app = Flask(__name__)
es = Elasticsearch([{'host':'localhost','port':9200,'scheme':'http'}])
es = Elasticsearch("http://localhost:9200")

# data = [{"balance": "$2,410.62", "age": 40, "name": "Bettie Buckner", "gender": "female", "company": "RODEOMAD",
#          "email": "bettiebuckner@rodeomad.com", "phone": "+1 (857) 491-2461"},
#         {"balance": "$1,143.56", "age": 28, "name": "Hanson Gates", "gender": "male", "company": "PEARLESSA",
#          "email": "hansongates@pearlessa.com", "phone": "+1 (825) 524-3896"},
#         {"balance": "$2,542.95", "age": 20, "name": "Audra Marshall", "gender": "female", "company": "COMTRAIL",
#          "email": "audramarshall@comtrail.com", "phone": "+1 (920) 569-2780"},
#         {"balance": "$2,235.86", "age": 34, "name": "Milagros Conrad", "gender": "female", "company": "IDEGO",
#          "email": "milagrosconrad@idego.com", "phone": "+1 (823) 451-2064"},
#         {"balance": "$2,606.95", "age": 34, "name": "Maureen Lopez", "gender": "female", "company": "EVENTEX",
#          "email": "maureenlopez@eventex.com", "phone": "+1 (913) 425-3716"}]

# for i in data:
#     res = es.index(index='bank_details',document=i)
#     print(res)

# i = {
#     "query":{
#         "bool":{
#             "must":[{"match":{"gender":"male"}},{"range":{"age":{'gte':25}}}]
#         }
#
#     }
# }

# res = es.search(index='bank_details',body=i)
# for i in res["hits"]["hits"]:
#     print(f"id = {i['_id']} ")
#     print(f'name = {i["_source"]["name"]}')

# print(f' name = {res["hits"]["hits"]["_source"]["name"]}')


@app.route('/bank_details', methods=['POST'])
def bank():
    data = request.get_json()
    print(data)
    # for i in data.items():
    #     print(i)
    o = {
    "query":{
        "bool":{
            "must":[]
        }
}
        }
    d = o['query']['bool']['must']
    print("################")
    print(d)

    l = len(data)

    for i in data.items():
        print(i)
        new = {"match": {i[0]:i[1]}}
        d.append(new)


    # for i in o['query']['bool']['must']:
    #     i["match"]=data




    print("---------------")
    print(o)
    res = es.search(index='bank_details',body=o)
    print("@@@@@@@@@@@@@@@@@@@@@@")
    print(res)
    for i in res["hits"]["hits"]:
        id = i['_id']
        name = i["_source"]["name"]
        final = {'id':id,'name':name}
    return (json.dumps(final))
    # return ('a')




@app.route("/")
def home():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
