from transformers import pipeline

pretrained_name = "w11wo/indonesian-roberta-base-sentiment-classifier"

nlp = pipeline(
    "sentiment-analysis",
    model=pretrained_name,
    tokenizer=pretrained_name
)

def analytics(text):
    query = nlp(text)
    return query[0]['label']

# print(analytics("Jangan sampai saya telpon bos saya ya!"))
