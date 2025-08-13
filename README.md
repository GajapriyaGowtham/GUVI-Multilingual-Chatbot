🤖 GUVI Multilingual Chatbot


This project is a smart multilingual chatbot that helps users ask questions about GUVI’s courses, platform, and features. It uses Retrieval-Augmented Generation (RAG) to fetch relevant information from a dataset and provide accurate, context-aware answers in the user’s own language.

✨ Features


Supports multiple languages, including Indian and global ones

Retrieves context using FAISS and SentenceTransformer embeddings

Translates questions and answers using NLLB-200

Generates answers with a lightweight text generation model (LaMini-Flan-T5-783M)

Interactive Gradio interface for seamless user interaction

Robust error handling for translation or generation issues

🛠 Tools & Technologies


Python

Hugging Face Transformers

Sentence Transformers

FAISS (vector search)

NLLB-200 (translation)

Gradio (UI)

NLTK (text preprocessing)

🔍 How It Works


User submits a question in any language.

The chatbot detects the language and translates it to English if needed.

The question is converted into embeddings, and the FAISS index is searched for the most relevant text chunks.

A prompt is built using the retrieved chunks and the user question.

The text generation model produces an answer.

If necessary, the answer is translated back to the user’s language and displayed.

📝 Steps I Took


Collected GUVI-related content from reliable sources like GUVI website, Shiksha, Scribd, ChatGPT, and Perplexity.

Cleaned and split the text into chunks using NLTK.

Created embeddings for each chunk and built a FAISS index.

Designed a RAG pipeline combining translation, retrieval, and generation.

Connected the pipeline to a Gradio interface for interactive use.

Deployed the app on Hugging Face Spaces for public access.


💡 Use Cases



Provide students with instant answers about GUVI courses and platform features.

Suggest relevant courses based on user queries.

Enable quick retrieval of GUVI knowledge without manual searching.

Offer 24/7 assistance in multiple languages.

Make GUVI content accessible to learners worldwide.

Support interactive learning with real-time explanations.

🌐 Try It Live


Experience the chatbot in action here:

👉 GUVI Multilingual Chatbot on Hugging Face Spaces
