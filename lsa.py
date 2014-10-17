import logging, gensim

id2word = gensim.corpora.Dictionary.load('imgur_comments.dict')

mm = gensim.corpora.MmCorpus('imgur_comments.mm')

lsi = gensim.models.lsimodel.LsiModel(corpus=mm, id2word=id2word, num_topics=1)

t = lsi.print_topics(1)
for i, topic in enumerate(t):
	print "Topic #%s: %s" % (i, topic)
