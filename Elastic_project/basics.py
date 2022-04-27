from elasticsearch import Elasticsearch
import os
import sys

# es = Elasticsearch("http://localhost:9200")
es = Elasticsearch([{"host":"localhost","port":9200,"scheme":"http"}])
print(es.ping())

### create index(table)
# print(es.indices.create(index='my-table',ignore=400))

## to get all indices
# res = es.indices.get_alias()
# for i in res:
#     print(i)

## delete index(table)
# print(es.indices.delete(index='my-foo'))
# print(es.indices.delete(index='my-table'))

# es.bulk(index='netflix',body=[])