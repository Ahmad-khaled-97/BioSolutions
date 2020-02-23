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
from gensim.test.utils import datapath
import json
import pickle
from gensim.corpora import Dictionary
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

tools = {}

def load_lda():
    lda = gensim.models.ldamodel.LdaModel.load('Main/model.sav')
    return lda

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

def feed_into_LDA(query,ldaModel):
    dictionary = Dictionary.load('Main/dictionary.dict')
    bow_vector = dictionary.doc2bow(query)

    probabilities=ldaModel.get_document_topics(bow_vector,minimum_probability=0)

    return probabilities


def Query_processing(query,ldaModel):
    result = []
    probmatrix=[]
    maxTopics=[]
    stemmer = SnowballStemmer("english")

    #Sentence splitting
    sentences=re.split('and |before |after |then |\.',query)

    for sentence in sentences:
        # POS Tagging
        #print(sentence)

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
        #print (sentProb)
        maxP = sentProb[0][1]
        maxT=sentProb[0][0]
        for topic in sentProb:
            v.append(topic[1])
            if (topic[1] > maxP):
                maxP = topic[1]
                maxT=topic[0]
        # Remove topics with variabce equal zero
        #print(np.var(v))
        if(np.var(v)<0.0001):
            v = []
            continue

        v=[]
        maxTopics.append(maxT)


    #print(maxTopics)



    return maxTopics

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

def unique(list1): 
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    return unique_list

def read_tools(fileName):
    with open(fileName) as fp: 
        prob = '' 
        for line in fp:
            if ('>' in line):
                prob = line[1:].strip()
                tools[prob] = []
            else:
                tool = line.split('|')
                tool_object = {
                    'name': tool[0].strip(),
                    'description': tool[1],
                    'link':tool[2].strip()
                }
                tools[prob].append(tool_object)

def write_dict_to_json(fileName,dic):
    with open(fileName, 'w') as json_file:
        json.dump(dic, json_file)

def problems_to_tools(problems):
    returned_tools = {}
    for problem in problems:
       returned_tools[problem]= []
       returned_tools[problem].append(tools[problem])
    return returned_tools


################################### main run #####################################
read_tools('Main/tools.txt')
query = input()
lda = load_lda()
maxtopics=Query_processing(query,lda)
topics=[]
for i in range(len(maxtopics)):
    topics.append(get_topic(maxtopics[i]))
unique_topics = unique(topics)

result = problems_to_tools(unique_topics)
write_dict_to_json('Main/result.json',result)
json_string = json.dumps(result)
print(json_string)