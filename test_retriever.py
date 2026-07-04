from modules.retriever import retrieve_documents

query = input("Ask a question: ")

results = retrieve_documents(query)

print("\nTop Retrieved Chunks:\n")

for i in range(len(results["documents"][0])):

    print(f"Result {i+1}")
    print(results["documents"][0][i][:300])
    print("Source:", results["metadatas"][0][i])
    print("-"*60)