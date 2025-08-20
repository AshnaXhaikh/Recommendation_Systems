# AI-Powered Book Recommender

## Objective

To build an AI-powered system that provides personalized book recommendations quickly and accurately, helping readers discover books matching their interests.

## Features

* Uses **sentence embeddings** (all-MiniLM-L6-v2) to understand book themes.
* Implements **FAISS** for fast similarity searches.
* Interactive **Streamlit** interface displaying book covers, ratings, and summaries.
* Supports various genres: sci-fi, self-help, fiction, and hidden gems.

## Approach

1. **Data Processing:** Extracted book descriptions and metadata.
2. **Embedding:** Converted text descriptions into numerical vectors using pre-trained transformer models.
3. **Similarity Search:** FAISS indexes embeddings for lightning-fast nearest-neighbor searches.
4. **UI Development:** Built an interactive interface with Streamlit for user-friendly recommendations.

## Live Demo

Check out the live demo here: [Book Recommender on HuggingFace](https://huggingface.co/spaces/ashnaxhaikh/book-recommender)

## Outcome

Users can quickly receive personalized book suggestions based on the content and themes they like, all through an intuitive and interactive UI.

## Skills Demonstrated

* Python (Data processing, AI/ML implementation)
* NLP (Sentence embeddings, semantic search)
* FAISS (High-speed similarity search)
* Streamlit (Interactive web interface)
