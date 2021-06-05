import collections
import math
from typing import DefaultDict
import ir_lib


# This function calculates the tf for a given file 
def tf(file_name:str):

    file = open(file_name,mode='r')
    file_content = file.readline()
    file.close()

    # n = len(file_content)

    counter = dict()
    for char in file_content:
        if char in counter:
            counter[char]+=1
        else:
            counter[char]=1  
            
    max = list(counter.values())[0]
    for val in counter.values():
        if val>max:
            max= val


    for key in counter:
        counter[key]/=max
    return counter 
#  This function calculates the frequencies of letters from all given files
def calculate_letters_from_documents_frequencies(file_names:list):

    freq = dict()
    for file_name in file_names:
        file = open(file_name,mode='r')
        file_content = file.readlines()[0]
        for char in file_content:
            if char not in freq:
                freq[char]=1
            else:
                freq[char]+=1
    
    return freq         

#  This function calculates the idf for every letter
def idf(number_of_documents:int=1000, counter:dict={}):    
    char_idf = dict()
    for key in counter:
        char_idf[key]=math.log2(number_of_documents/counter[key])

    return char_idf;


    counter = dict()
    query = query.replace('<','').replace('>','').replace(' ','').upper()
    for sp  in query.split(';'):
        result = sp.split(':')
        # print(result[0],result[1])
        key = result[0]
        value= result[1]
        counter[key]=float(value) 

    return counter

#  This function calculates the tf_idf of every letter for the given list of files
def tf_idf(files_list:list):
        freq = calculate_letters_from_documents_frequencies(files_list)
        # print(freq)
        tf_idf_container=dict()
        idfs=idf(10000,freq)
        for file in files_list:
           file_tf= tf(file)
        #    print(idfs)
           tf_idf_char = DefaultDict()
           for key in file_tf:
               if key not in idfs: continue
               tf_idf_char[key] = idfs[key]*file_tf[key] 
               
           tf_idf_container[file]=tf_idf_char

        return tf_idf_container
#  This function calculates the similarity between a given file and a query string
def sim(document_file,query:str):
    file_tf = tf(document_file)
    file = open('query.txt',mode='w')
    file.write(query)
    file.flush()
    file.close()

    query_tf = tf('query.txt')

    sum = 0
    for key in query_tf:
        sum+=query_tf[key]*file_tf[key]

    return sum    

#  This function calculates the similarity between a given list of files and a query
def sim_all(file_names:list,query:str):
    result=DefaultDict()
    for file in file_names:
        result[file] = sim(file,query)
    return result    

#  This function generates random files, then calculates the similarity between them and a given query
def calculate(query:str):
    files = ir_lib.generate_random_files()
    result = sim_all(files,query)
    results_ranked = list()
    for key in result:
        results_ranked.append(tuple([result[key],key]))

    results_ranked.sort()
    results_ranked.reverse()
    return results_ranked

#  This function calculates the weights squared for each element in a list
def weights_sqrt(weights:list):
    sum = 0
    for w in weights:
        sum+=w*w
    return math.sqrt(sum)    

# This function calculates the cosine similarity for a query and a list of randomly generated files
def calculate_cos_sim(query:str):
    files = ir_lib.generate_random_files()
    result = sim_all(files,query)
    makam=DefaultDict()
    query_tf =tf("query.txt")
    makam["query.txt"]=query_tf
    for file in files:
        file_tf = tf(file)
        makam[file]=(weights_sqrt(file_tf.values())*weights_sqrt(query_tf.values()))
        
    cos_sim=DefaultDict()
    for file in files:
        cos_sim[file] = result[file]/makam[file]

    results_ranked = list()
    for key in cos_sim:
        results_ranked.append(tuple([cos_sim[key],key]))

    results_ranked.sort()
    results_ranked.reverse()
    return results_ranked   


# if __name__ == '__main__':
#     files = []
#     for i in range(0,10):
#         files.append('generated/file_name_{}.txt'.format(i))
#     # tf_idfs = tf_idf(files)
#     calculate_cos_sim('<A:0.2;B:0.9;D:0.8>')


