"""
Vector database backend implementations

Tier 1: ChromaDB, Pinecone, Qdrant
Tier 2: Elasticsearch, Solr
Tier 3: Weaviate, Milvus, pgvector, Redis
"""

# Backends are imported dynamically by factory to avoid requiring all dependencies
