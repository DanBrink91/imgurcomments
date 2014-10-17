import logging, gensim

id2word = gensim.corpora.Dictionary.load('imgur_comments.dict')

mm = gensim.corpora.MmCorpus('imgur_comments.mm')

lda= gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=10, update_every=0, passes=100)

t = lda.print_topics(10)
for i, topic in enumerate(t):
	print "Topic #%s: %s\n" % (i, topic)
