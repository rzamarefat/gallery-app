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

        self._mapping_face = {
            "mappings":{
                "properties":{
                    "embedding":{
                        "type": "dense_vector",
                        "dims": 512
                    }
                }
            }
        }
        self._mapping_text = {
            "mappings":{
                "properties":{
                    "embedding":{
                        "type": "dense_vector",
                        "dims": 1536
                    }
                }
            }
        }

        self._index_name_face = "gallery-index-face"
        self._index_name_text = "gallery-index-text"
        if not self._es.indices.exists(index=self._index_name_face):
            self._es.indices.create(index=self._index_name_face, body=self._mapping_face)
        if not self._es.indices.exists(index=self._index_name_text):
            self._es.indices.create(index=self._index_name_text, body=self._mapping_text)
            

    def push_index(self, index_id, embedding, mode):
        document = {
                "embedding": embedding
        }
        if mode == "text":    
            response = self._es.index(index=self._index_name_text, id=index_id, document=document)
        elif mode == "face":
            response = self._es.index(index=self._index_name_face, id=index_id, document=document)
                
        return response

    def query_index(self):
        pass

