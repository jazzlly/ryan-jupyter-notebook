#%%
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['192.168.10.252'], 
    http_auth=('elastic', 'Ryanes12#$'),
    scheme='http', port=9200)

doc = {
    'foo': 'bar',
    'timestamp': datetime.now()
}

res = es.index(index='py-demo-index', id=3, body=doc)
print(res['result'])

#%%

from datetime import datetime
from elasticsearch import Elasticsearch
res=es.get(index='py-demo-index', id=1)
res

#%%
res = es.search(index='py-demo-index', 
    body= {
        "query": {
            "match_all": {}
            }
        }
)

# print(res['hits']['hits'])

import json
for hit in res['hits']['hits']:
    print(json.dumps(hit['_source'], indent=2))

#%%
import json
import time
import random as rand
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers


es = Elasticsearch(
    ['192.168.10.252'], 
    http_auth=('elastic', 'Ryanes12#$'),
    scheme='http', port=9200)

hosts=(
    {
        'name': 'system test server',
        'ip': '192.168.11.78'
    },
    {
        'name': 'system test server',
        'ip': '192.168.10.27'
    },
    {
        'name': 'es cluster 1',
        'ip': '192.168.11.25'
    },
    {
        'name': 'es cluster 2',
        'ip': '192.168.11.26'
    },
    {
        'name': 'es cluster 3',
        'ip': '192.168.11.27'
    },
)

docs=[]
for t in range(int(time.time()), int(time.time() - time.time()/100), -60):
    for host in hosts:
        cpu_usage=[]
        for i in range(4):
            cpu_usage.append(rand.randrange(0, 101))
        rand_usage = {
            '_index': 'py-demo-metrics-index',
            '_source': {
                'ip': host['ip'],
                'host': host['name'], 
                'cpu_usage': cpu_usage,
                'mem_usage': rand.randrange(0, 101),
                'timestamp': datetime.fromtimestamp(t)
            }
        }
        docs.append(rand_usage)
        if (len(docs) >= 2000):
            print(f'begin bulk: {time.time()}')
            helpers.bulk(es, docs)
            docs = []
            print(f'end bulk: {time.time()}')
        # print(json.dumps(rand_usage, indent=2, default=str))

#%%
import time
from datetime import datetime
time.time() - time.time()/50

date = datetime.fromtimestamp(time.time() - time.time()/50)
date
#%%

actions = [
  {
    "_index": "tickets-index",
    "_type": "tickets",
    "_id": j,
    "_source": {
        "any":"data" + str(j),
        "timestamp": datetime.now()}
  }
  for j in range(0, 10)
]


#%% 
import akshare as ak
macro_china_gksccz_df = ak.macro_china_gksccz()

