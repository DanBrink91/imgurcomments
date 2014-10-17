from gensim import corpora, models, similarities
import json

comment_json = json.loads(open("comments2.json", "rb").read())
comments = [caption['caption'] for caption in comment_json['data']['captions']]

stop_words = open("stopwords.txt", "rb").read()
stop_words = [word for word in stop_words.split("\n") if len(word) >= 1]

# tokenize 
# TODO: remove stopwords
texts = [[word for word in comment.lower().split() if word not in stop_words] for comment in comments]

all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once] for text in texts]

dictionary = corpora.Dictionary(texts)
dictionary.save('imgur_comments.dict')

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('imgur_comments.mm', corpus)
print corpus