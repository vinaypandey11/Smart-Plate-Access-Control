from transformers import pipeline

classifier = pipeline("sentiment-analysis")
res = classifier("i am happy ")

print(res)