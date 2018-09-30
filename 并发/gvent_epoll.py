import gevent
from gevent import monkey;monkey.patch_all()
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
import time
client = Elasticsearch([{'host': '192.168.128.101', 'port': 9200}])


def search(keyword,key):
    result = client.search(index='kamailio_error_log_2018.09.28', q='%s:"%s"~1' % (keyword, key), size=1000)
    # print(result)
monitor_project = {"kamailio_log": ["curl_easy_init() failed",
                                        "REQ_ERR DELAYED should have been caught much earlier",
                                        "no resolved dst to retransmit"],
                                   "level": ["CRITICAL"]}
start_time = time.time()
for i in range(100):
    for keyword in monitor_project:
        gevent_list = [gevent.spawn(search,keyword,key) for key in monitor_project[keyword] ]
# print(gevent_list)
gevent.joinall(gevent_list)
print(time.time()-start_time)

print(1231212)