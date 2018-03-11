from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

res = es.search(index="items"
                , body={"query": {"match_all": {}}, "_source": ["id", "name", "description"]})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print(hit["_source"]["name"] + ":" + hit["_source"]["description"])