from modules.chatbot import ask_chatbot

question = input("Ask: ")

answer, sources = ask_chatbot(question)

print("\nAnswer:\n")
print(answer)

print("\nSources:\n")

for source in sources:
    print(source)