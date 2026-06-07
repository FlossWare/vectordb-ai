"""
Vector Store Factory - Create backend instances

Supports all major vector database backends.
"""

from typing import Dict, Any
from vectordb_ai.base import VectorStore


class VectorStoreFactory:
    """Factory to create vector store backends"""

    # Backend registry
    _backends = {}

    @classmethod
    def register(cls, name: str, backend_class: type):
        """Register a backend"""
        cls._backends[name] = backend_class

    @classmethod
    def create(cls, backend: str, **config) -> VectorStore:
        """
        Create vector store instance

        Args:
            backend: Backend name (chromadb, pinecone, qdrant, etc.)
            **config: Backend-specific configuration

        Returns:
            VectorStore instance

        Raises:
            ValueError: If backend not found or dependencies missing
        """
        if backend not in cls._backends:
            raise ValueError(
                f"Unknown backend: {backend}. "
                f"Available: {list(cls._backends.keys())}"
            )

        backend_class = cls._backends[backend]

        try:
            return backend_class(**config)
        except ImportError as e:
            raise ImportError(
                f"Backend '{backend}' requires additional dependencies. "
                f"Install with: pip install knowledge-forge[{backend}]\n"
                f"Error: {e}"
            )

    @classmethod
    def list_backends(cls) -> Dict[str, str]:
        """List all available backends with descriptions"""
        return {
            'chromadb': 'ChromaDB - Embedded vector database (default)',
            'pinecone': 'Pinecone - Managed cloud vector database',
            'qdrant': 'Qdrant - High-performance vector database',
            'weaviate': 'Weaviate - GraphQL vector database',
            'milvus': 'Milvus - Scalable vector database',
            'solr': 'Apache Solr - Search platform with vector support',
            'elasticsearch': 'Elasticsearch - Search with vector support',
            'pgvector': 'pgvector - PostgreSQL vector extension',
            'redis': 'Redis - In-memory vector database'
        }


# Auto-register backends (lazy loading)
def _register_all_backends():
    """Register all available backends"""

    # Tier 1: Must Have
    try:
        from vectordb_ai.backends.chromadb import ChromaDBStore
        VectorStoreFactory.register('chromadb', ChromaDBStore)
    except ImportError:
        pass

    try:
        from vectordb_ai.backends.pinecone import PineconeStore
        VectorStoreFactory.register('pinecone', PineconeStore)
    except ImportError:
        pass

    try:
        from vectordb_ai.backends.qdrant import QdrantStore
        VectorStoreFactory.register('qdrant', QdrantStore)
    except ImportError:
        pass

    # Tier 2: Should Have
    try:
        from vectordb_ai.backends.elasticsearch import ElasticsearchStore
        VectorStoreFactory.register('elasticsearch', ElasticsearchStore)
    except ImportError:
        pass

    try:
        from vectordb_ai.backends.solr import SolrStore
        VectorStoreFactory.register('solr', SolrStore)
    except ImportError:
        pass

    try:
        from vectordb_ai.backends.weaviate import WeaviateStore
        VectorStoreFactory.register('weaviate', WeaviateStore)
    except ImportError:
        pass

    # Tier 3: Nice to Have
    try:
        from vectordb_ai.backends.milvus import MilvusStore
        VectorStoreFactory.register('milvus', MilvusStore)
    except ImportError:
        pass

    try:
        from vectordb_ai.backends.pgvector import PgVectorStore
        VectorStoreFactory.register('pgvector', PgVectorStore)
    except ImportError:
        pass

    try:
        from vectordb_ai.backends.redis import RedisStore
        VectorStoreFactory.register('redis', RedisStore)
    except ImportError:
        pass


# Register on import
_register_all_backends()
