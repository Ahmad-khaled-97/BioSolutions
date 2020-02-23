import gensim
import nltk
import numpy as np
from gensim import models
from nltk.stem import WordNetLemmatizer, SnowballStemmer
np.random.seed(2018)
import codecs
import re
import os
from nltk import sent_tokenize


nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
fileDir = os.path.dirname(os.path.realpath('__file__'))

def load_Data():
    file1 = open("Data/DNA-Sequence-Acquisition.txt", "r")
    doc1=file1.readlines()

    file1 = open("Data/Sequence-Alignment.txt", "r")
    doc2 = file1.readlines()

    file1 = codecs.open("Data/Binding-Site-Prediction.txt", "r",'utf-16-le')
    doc3 = file1.readlines()

    file1 = codecs.open("Data/Genome-Assembly.txt", "r",'utf-16-le')
    doc4 = file1.readlines()

    file1 = codecs.open("Data/Phylogenetic-Analysis.txt", "r",'utf-16-le')
    doc5 = file1.readlines()

    file1 = codecs.open("Data/Protein-Structure-Prediction.txt", "r",'utf-16-le')
    doc6 = file1.readlines()
    result=(doc1,doc2,doc3,doc4,doc5,doc6)

    return result

#Preprocessing is done as follows:
#1-Tokenization
#2-Lemmatization and stemming
#3-Removing stop words
def Model_data_preprocessing(doc):
    result = []
    stemmer=SnowballStemmer("english")
    for token in gensim.utils.simple_preprocess(doc):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) >= 3:
            result.append(stemmer.stem(WordNetLemmatizer().lemmatize(token, pos='v')))

    return result



def Query_processing(query,ldaModel):
    result = []
    probmatrix=[]
    maxTopics=[]
    stemmer = SnowballStemmer("english")

    #Sentence splitting
    sentences=re.split('and |before |after |then |\.',query)

    for sentence in sentences:
        # POS Tagging
        print(sentence)

        for token in gensim.utils.simple_preprocess(sentence):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) >= 3:

                result.append(stemmer.stem(WordNetLemmatizer().lemmatize(token, pos='v')))

        #making freq of each word=1
        querylist_set = set(result)
        unique_querylist = (list(querylist_set))

        #Probmatrix is a matrix containing topic probability distribution for each sentence.
        probmatrix.append(feed_into_LDA(unique_querylist,ldaModel))

        result=[]


    v=[]

    #Getting maximum probability for each sentence
    for sentProb in probmatrix:
        print (sentProb)
        maxP = sentProb[0][1]
        maxT=sentProb[0][0]
        for topic in sentProb:
            v.append(topic[1])
            if (topic[1] > maxP):
                maxP = topic[1]
                maxT=topic[0]
        # Remove topics with variabce equal zero
        print(np.var(v))
        if(np.var(v)<0.0001):
            v = []
            continue

        v=[]
        maxTopics.append(maxT)


    print(maxTopics)



    return maxTopics





def get_key(s):
    for k, v in dictionary.iteritems():
        if (v==s):
            return k

#Converting our corpus(each document) into a bag of words, as a preparation step for LDA running.
def lda_preparation(docs):
    dictionary = gensim.corpora.Dictionary(docs)
    #id for each word

    #Filter extremes
    dictionary.filter_extremes(no_below=0, no_above=0.67, keep_n=100000)


    bow_corpus = [dictionary.doc2bow(doc) for doc in docs]
    #Bag of words is a collection if vectors of size=vocabulary size.each vector represents a document.and each value=number of occurrence of this word in this document.
    tfidf = models.TfidfModel(bow_corpus)
    corpus_tfidf = tfidf[bow_corpus]

    return  dictionary,bow_corpus,corpus_tfidf

def etaValueSetting():
    eta = np.ones((6, len(dictionary))) * 0.5
    #Setting priors for topic 0 i.e Alignment
    eta[0,get_key("similar")]*=10
    eta[0, get_key("align")] *= 10
    eta[0, get_key("score")] *= 10
    eta[0, get_key("local")] *= 10
    eta[0, get_key("compar")] *= 10

    #Setting priors for topic 1 i.e Gene Aquisition
    eta[1, get_key("databas")] *= 10
    eta[1, get_key("format")] *= 10
    eta[1, get_key("download")] *= 10
    eta[1, get_key("retriev")] *= 10

    #Setting priors for tpoic 2 i.e binding site predicton

    eta[2, get_key("interact")] *= 10
    eta[2, get_key("bind")] *= 10
    eta[2, get_key("drug")] *= 10
    eta[2, get_key("ligand")] *= 10


    #Setting priors for topic 3 i.e Genome assembly

    eta[3, get_key("assembl")] *= 10
    eta[3, get_key("fragment")] *= 10
    eta[3, get_key("shotgun")] *= 10
    eta[3, get_key("reconstruct")] *= 10
    eta[3, get_key("contig")] *= 10


    #Setting priors for topic 4 i.e Phylogeny
    eta[4, get_key("phylogeni")] *= 10
    eta[4, get_key("tree")] *= 10
    eta[4, get_key("evolut")] *= 10
    eta[4, get_key("ancestor")] *= 10
    eta[4, get_key("branch")] *= 10


    #Setting priors for topic 5 i.e Protein structure prediction

    eta[5, get_key("structur")] *= 10
    eta[5, get_key("helic")] *= 10
    eta[5, get_key("conform")] *= 10
    eta[5, get_key("sheet")] *= 10

    return eta


def lda(dictionary,bow_corpus,corpus_tfidf):
    eta=etaValueSetting()



    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus_tfidf,
                                                id2word=dictionary,
                                                num_topics=6,
                                                random_state=100,
                                                update_every=1,
                                                chunksize=100,
                                                passes=15,
                                                alpha=0.7,
                                                per_word_topics=True
                                                ,eta=eta)




    return lda_model



# def visualizeModel(ldaModel):
#     for idx, topic in ldaModel.print_topics(-1):
#         print("Topic: {} \nWords: {}".format(idx, topic))
#         print("\n")
#
#     cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]
#
#     cloud = WordCloud(stopwords=gensim.parsing.preprocessing.STOPWORDS,
#                       background_color='white',
#                       width=2500,
#                       height=1800,
#                       max_words=10,
#                       colormap='tab10',
#                       color_func=lambda *args, **kwargs: cols[i],
#                       prefer_horizontal=1.0)
#
#     topics = ldaModel.show_topics(formatted=False)
#
#     fig, axes = plt.subplots(3, 2, figsize=(10, 10), sharex=True, sharey=True)
#
#     for i, ax in enumerate(axes.flatten()):
#         fig.add_subplot(ax)
#         topic_words = dict(topics[i][1])
#         cloud.generate_from_frequencies(topic_words, max_font_size=300)
#         plt.gca().imshow(cloud)
#         plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
#         plt.gca().axis('off')
#
#     plt.subplots_adjust(wspace=0, hspace=0)
#     plt.axis('off')
#     plt.margins(x=0, y=0)
#     plt.tight_layout()
#     plt.show()


#Feeding query into LDA model and return probabilities for each topic
def feed_into_LDA(query,ldaModel):

    bow_vector = dictionary.doc2bow(query)

    probabilities=ldaModel.get_document_topics(bow_vector,minimum_probability=0)

    return probabilities

def get_topic(index):
    if (index==0):
        return "Sequence Alignment"
    elif (index==1):
        return "DNA-Sequence-Acquisition"
    elif (index==2):
        return "Binding-Site-Prediction"
    elif (index==3):
        return "Genome-Assembly"
    elif (index==4):
        return "Phylogenetic-Analysis"
    elif (index==5):
        return "Protein-Structure-Prediction"

all_docs=load_Data()

processed_docs=[]
for doc in all_docs:

    processed_docs.append(Model_data_preprocessing(str(doc)))

dictionary,bow_corpus,corpus_tfidf=lda_preparation(processed_docs)
ldaModel=lda(dictionary,bow_corpus,corpus_tfidf)


# visualizeModel(ldaModel)

maxtopics=Query_processing('Welcome to 3abood 3al 7odod gene protein prediction',ldaModel)
ret=[]
for i in range(len(maxtopics)):
    ret.append(get_topic(maxtopics[i]))

print(ret)