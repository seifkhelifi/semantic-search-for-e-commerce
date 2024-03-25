from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer


app = Flask(__name__)

try:
    es = Elasticsearch(
        "https://localhost:9200",
        basic_auth=("seif", "rafting123456"),
        ca_certs=r"C:\Users\dell\Desktop\elasticsearch-8.12.2\config\certs\http_ca.crt"
    )
except ConnectionError as e:
    print("Connection Error:", e)
    
if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")
    
    
def search(input_keyword):
    model = SentenceTransformer('all-mpnet-base-v2')
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "DescriptionVector",
        "query_vector": vector_of_input_keyword,
        "k": 10,
        "num_candidates": 1799
    }
    res = es.knn_search(index="all_products_final", knn=query , source=["ProductName","Description"])
    results = res["hits"]["hits"]

    return results



@app.route('/search', methods=['POST'])
def search_endpoint():
    data = request.json
    query_text = data.get('queryText')

    # Call your search function with the query text
    results = search(query_text)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)