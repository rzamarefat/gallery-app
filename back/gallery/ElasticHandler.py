from elasticsearch import Elasticsearch

class ElasticHandler:
    def __init__(self):
        ELASTICSEARCH_HOST = 'localhost'
        ELASTICSEARCH_PORT = 9200
        SCHEME = 'http'  
        self._es = Elasticsearch(
            hosts=[{
                'host': ELASTICSEARCH_HOST,
                'port': ELASTICSEARCH_PORT,
                'scheme': SCHEME
            }]
        )

        if self._es.ping():
            print("Connected to Elasticsearch")
        else:
            print("Could not connect to Elasticsearch")
            exit()

        self._mapping = {
            "mappings":{
                "properties":{
                    "embedding":{
                        "type": "dense_vector",
                        "dims": 1536
                    }
                }
            }
        }


        self._index_name = "gallery-index"
        if not self._es.indices.exists(index=self._index_name):
            self._es.indices.create(index=self._index_name, body=self._mapping)

    def push_index(self, index_name, index_id, embedding):
        document = {
            "embedding": embedding
        }
        response = self._es.index(index=index_name, id=index_id, document=document)
        return response

    def query_index(self):
        pass

