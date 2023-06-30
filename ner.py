from transformers import pipeline

pretrained_ner = "cahya/bert-base-indonesian-NER"

ner_pipeline = pipeline(
    "ner",
    model=pretrained_ner,
    tokenizer=pretrained_ner,
    aggregation_strategy="simple",
)

def ner(text):
    output = ner_pipeline(text)
    respon = []
    for row in output:
        respon.append({'entity': row['entity_group'], 'word': row['word']})
    return respon

# print(ner("Jokowi kecewa kepada kapolri karena penanganan di kampung bandit tidak berjalan dengan baik"))
