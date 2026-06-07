"""
VectorDB AI - Universal vector database adapter

Switch between vector databases without changing code.
No vendor lock-in. Portable data format.
"""

__version__ = "0.1"
__author__ = "FlossWare (sfloess)"
__license__ = "GPL-3.0"

from vectordb_ai.base import VectorStore, ContentChunk, Fact
from vectordb_ai.factory import VectorStoreFactory
from vectordb_ai.embeddings import EmbeddingGenerator, embed

__all__ = [
    "VectorStore",
    "ContentChunk",
    "Fact",
    "VectorStoreFactory",
    "EmbeddingGenerator",
    "embed",
]
