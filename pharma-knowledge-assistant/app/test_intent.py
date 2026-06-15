from services.intent_classifier import classify_intent

question = input("Question: ")

intent = classify_intent(question)

print(intent)