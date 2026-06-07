# VectorDB AI

**Universal vector database adapter for AI applications**

Switch between 9 vector database backends without changing your code. No vendor lock-in.

## Features

✅ **9 Vector Database Backends**
- **Tier 1:** ChromaDB, Pinecone, Qdrant (embedded + cloud)
- **Tier 2:** Elasticsearch, Solr (enterprise search)
- **Tier 3:** Weaviate, Milvus, pgvector, Redis (specialized)

✅ **Portable Data Format**
- Export from any backend
- Import to any backend
- JSON-based interchange

✅ **Semantic Embeddings**
- 384-dimensional vectors (all-MiniLM-L6-v2)
- Automatic embedding generation
- Configurable models

✅ **Production Ready**
- Abstract interface
- Type hints
- Comprehensive error handling

## Quick Start

```python
from vectordb_ai import VectorStoreFactory, ContentChunk, embed

# Create store (ChromaDB by default)
store = VectorStoreFactory.create(
    backend='chromadb',
    collection='my-docs'
)

# Add documents
chunks = [
    ContentChunk(
        chunk_id='doc1',
        content='Python is awesome',
        source='tutorial.pdf',
        embedding=embed('Python is awesome')
    )
]
store.add_chunks(chunks)

# Search
results = store.search_chunks(
    query_embedding=embed('programming languages'),
    top_k=5
)
```

## Switch Backends

```python
# Start with ChromaDB (embedded)
store = VectorStoreFactory.create(backend='chromadb', collection='docs')

# Export data
store.export('data.json')

# Switch to Pinecone (cloud)
store = VectorStoreFactory.create(
    backend='pinecone',
    collection='docs',
    api_key='your-key'
)
store.import_from('data.json')
```

## Supported Backends

| Backend | Type | Use Case | Install |
|---------|------|----------|---------|
| ChromaDB | Embedded | Development, small-scale | `pip install vectordb-ai` |
| Pinecone | Cloud | Production, scalable | `pip install vectordb-ai[pinecone]` |
| Qdrant | Cloud/Self-hosted | Production | `pip install vectordb-ai[qdrant]` |
| Elasticsearch | Self-hosted | Enterprise | `pip install vectordb-ai[elasticsearch]` |
| Solr | Self-hosted | Enterprise | `pip install vectordb-ai[solr]` |
| Weaviate | Cloud/Self-hosted | GraphQL API | `pip install vectordb-ai[weaviate]` |
| Milvus | Self-hosted | High performance | `pip install vectordb-ai[milvus]` |
| pgvector | Postgres | Existing Postgres | `pip install vectordb-ai[pgvector]` |
| Redis | Self-hosted | In-memory | `pip install vectordb-ai[redis]` |

## Installation

### From PyPI (Recommended)
```bash
# Basic (ChromaDB only)
pip install vectordb-ai

# With specific backend
pip install vectordb-ai[pinecone]
pip install vectordb-ai[qdrant]

# All backends
pip install vectordb-ai[all]
```

### From packagecloud.io (Enterprise)
```bash
pip install --index-url https://packagecloud.io/FlossWare/releases/pypi/simple vectordb-ai
```

### From GitHub (Latest)
```bash
pip install git+https://github.com/FlossWare/vectordb-ai.git
```

### For Development
```bash
git clone https://github.com/FlossWare/vectordb-ai.git
cd vectordb-ai/python
pip install -e .
```

## Part of FlossWare AI

- **vectordb-ai** - Vector database adapter (this project)
- **semantic-search-ai** - Search enhancements
- **consensus-ai** - Multi-AI orchestration
- **knowledge-ai** - Knowledge ingestion
- **universal-ai** - AI platform

## License

GPL-3.0 - FlossWare (sfloess)

