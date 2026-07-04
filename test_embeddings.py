from modules.embeddings import create_embedding

embedding = create_embedding("Python is a programming language.")

print(type(embedding))
print(len(embedding))