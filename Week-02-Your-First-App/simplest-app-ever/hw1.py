from transformers  import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I really like fried chicken")
print(res)