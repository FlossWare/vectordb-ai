"""
VectorDB AI - Universal vector database adapter

Switch between vector databases without changing code.
Supports 9 backends with portable data format.
"""

from setuptools import setup, find_packages

setup(
    name="vectordb-ai",
    version="0.1",
    author="FlossWare (sfloess)",
    description="Universal vector database adapter for AI applications",
    long_description=open("../README.md").read() if __file__ else "",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/cee/sfloess/vectordb-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "sentence-transformers>=2.2.0",
        "numpy>=1.21.0",
    ],
    extras_require={
        # Tier 1: Embedded/Cloud-native
        "chromadb": ["chromadb>=0.4.0"],
        "pinecone": ["pinecone-client>=2.0.0"],
        "qdrant": ["qdrant-client>=1.0.0"],

        # Tier 2: Enterprise search
        "elasticsearch": ["elasticsearch>=8.0.0"],
        "solr": ["pysolr>=3.9.0"],

        # Tier 3: Specialized
        "weaviate": ["weaviate-client>=3.0.0"],
        "milvus": ["pymilvus>=2.0.0"],
        "pgvector": ["psycopg2-binary>=2.9.0"],
        "redis": ["redis>=4.0.0", "redis-py>=4.0.0"],

        # All backends
        "all": [
            "chromadb>=0.4.0",
            "pinecone-client>=2.0.0",
            "qdrant-client>=1.0.0",
            "elasticsearch>=8.0.0",
            "pysolr>=3.9.0",
            "weaviate-client>=3.0.0",
            "pymilvus>=2.0.0",
            "psycopg2-binary>=2.9.0",
            "redis>=4.0.0",
        ],
    },
)
