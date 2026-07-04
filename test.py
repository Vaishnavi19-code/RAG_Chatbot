from modules.ingest import extract_text_from_folder
from modules.preprocess import create_chunks
from modules.vector_store import create_vector_database

# Step 1: Extract text
pages = extract_text_from_folder("data/pdfs")

# Step 2: Create chunks
chunks = create_chunks(pages)

# Step 3: Store in ChromaDB
collection = create_vector_database(chunks)

print("\nKnowledge Base Created Successfully!")