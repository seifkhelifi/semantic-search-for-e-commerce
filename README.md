# Jewelry E-Commerce Search Engine

This project implements a semantic search engine for a jewelry e-commerce dataset using Elasticsearch and the `all-mpnet-base-v2` sentence transformer model. The system allows users to search for products using natural language queries, with results ranked by semantic similarity to the query.

## Project Overview

The system consists of:
1. Data preparation and vectorization pipeline
2. Elasticsearch index configuration for vector search
3. Flask API for interacting with the search engine

## Key Features

- **Semantic Search**: Finds products based on meaning rather than just keyword matching
- **Vector Embeddings**: Uses the `all-mpnet-base-v2` model to convert product descriptions into 768-dimensional vectors
- **Scalable Search**: Leverages Elasticsearch's kNN capabilities for efficient similarity search
- **REST API**: Provides easy integration with frontend applications

## Technical Components

### Data Processing
- Loads jewelry product data from CSV
- Handles missing values
- Generates vector embeddings for product descriptions
- Indexes data in Elasticsearch with proper mapping for vector fields

### Search Engine
- Elasticsearch 8.x with kNN search capabilities
- Custom index mapping optimized for vector search
- Support for semantic similarity ranking

### API Endpoints
- Flask-based REST API for search operations
- Accepts natural language queries
- Returns semantically relevant products

## Setup Instructions

### Prerequisites
- Python 3.8+
- Elasticsearch 8.x
- Elasticsearch Python client
- SentenceTransformers library
- Flask

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Elasticsearch:
   - Configure Elasticsearch with security settings
   - Place your CA certificate in the specified location

4. Prepare your dataset:
   - Place your CSV file in the `dataset` folder
   - Update the file path in the code if needed

### Running the Application
1. Start the Flask API:
   ```bash
   python app.py
   ```

2. The API will be available at `http://localhost:5000`

## API Usage

### Search Endpoint
- **URL**: `/search`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "query": "your search query"
  }
  ```

- **Response**:
  ```json
  {
    "results": [
      {
        "product_name": "...",
        "description": "...",
        "score": 0.95
      },
      ...
    ]
  }
  ```

## Example Queries

1. Search for floral-themed products:
   ```json
   {
     "query": "products with flower designs"
   }
   ```

2. Search for gold jewelry:
   ```json
   {
     "query": "gold necklaces and bracelets"
   }
   ```

