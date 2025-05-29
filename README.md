## 🧠 Semantic Search Engine using BERT and Elasticsearch

This project implements a **semantic search engine** for e-commerce jewelry products using **BERT embeddings** and **Elasticsearch's KNN search**. The system allows searching for products based on meaning rather than exact keyword matches, providing a smarter and more intuitive search experience.

Demo on this link : https://drive.google.com/file/d/1S59zps1S0pkXq8kmPwOV7y4WjFJj_8AX/view?usp=sharing


---

## 🚀 Features

- 🔍 Semantic search with Sentence-BERT (`all-mpnet-base-v2`)
- 🔎 Vector similarity search using Elasticsearch 8.x and l2_norm 
- 🧾 Flask-based API to serve search results
- 🔗 Supports CORS for frontend consumption
- 🧠 Preprocessing and ingestion of product descriptions into vector embeddings
- 📁 Elasticsearch index with vector and metadata fields

---

## 📦 Folder Structure

```

.
├── search\_api.py                # Flask API for semantic search
├── indexMappingJewelery.py     # Mapping/schema for Elasticsearch index
├── ingest\_notebook.ipynb       # Ingest data and build vector embeddings
├── dataset/                    # Contains the CSV dataset
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

````

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/semantic-search-engine.git
cd semantic-search-engine
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Ensure Elasticsearch is running

* Make sure Elasticsearch 8.x is installed and running locally.
* Provide your credentials and certificate path inside `search_api.py` and ingestion notebook.

### 4. Ingest data into Elasticsearch

Run the `ingest_notebook.ipynb` notebook to:

* Load product data from CSV
* Generate BERT embeddings for descriptions
* Create the Elasticsearch index
* Index the documents with metadata and vector fields

### 5. Run the Flask API

```bash
python search_api.py
```

---

## 🔄 API Endpoint

### POST `/search`

**Request Body:**

```json
{
  "queryText": "floral necklace"
}
```

**Response:**

```json
{
  "products": [
    {
      "name": "Rose Pendant Necklace",
      "company": "Elegant Bloom",
      "category": "Necklaces",
      "colour": "Gold",
      "description": "A delicate floral-themed pendant...",
      "image": "...",
      "price": 99.99,
      "product_url": "https://..."
    },
    ...
  ]
}
```

---

## 🧠 Technology Stack

* **Elasticsearch 8.x**
* **Flask**
* **SentenceTransformers** (`all-mpnet-base-v2`)
* **Pandas**
* **Python 3.8+**

---

## 📌 Notes

* Ensure `elasticsearch` is configured with KNN enabled.
* Sensitive credentials like certificates and passwords are currently hardcoded; consider securing them using environment variables or secret managers.

---

## 📜 License

This project is open-source under the MIT License.






