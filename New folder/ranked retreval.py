import numpy as np
import math
import Quick_Sort
import index
import Query
list_text = ['t1', 't2', 't3', 't4', 't5', 't6']
query = list(map(str, (input('enter your query :').lower()).split()))
#===============================================
frequnency_word = index.fre_word_doc()
#===============================================
set_querys = Query.query(query)
#===============================================
set_fre_text = {}
list_fre_text = []
list_count_fre_text = [[]for j in range(len(list_text))]
for index1 in range(len(list_text)):
    for word in set_querys:
        if word in frequnency_word[index1]:
            list_fre_text.append(frequnency_word[index1].get(word))
            list_count_fre_text[index1].append(1)
        else:
            list_fre_text.append(0)
            list_count_fre_text[index1].append(0)
    set_fre_text.setdefault(list_text[index1], list_fre_text)
    list_fre_text = []
array_count_fre_text = np.array(list_count_fre_text)
if len(list_text) > 1:
    sum_array = np.sum(array_count_fre_text, 0)
    print('>>>>>>', 'sum_array = ', sum_array)
    print('===============================================')
print('>>>>>>', 'set_fre_text =', set_fre_text)
print('===============================================')
#===============================================
tf_idf_weight = {}
tf_idf_list = []
index4 = 0
if len(list_text) == 1:
    if sum(set_fre_text.get(list_text[0])) > 1:
        print('>>>>>>', list_text[0])
        print('===============================================')
    else:
        print('No results were found')
        print('===============================================')
else:
    for text in list_text:
        while index4 < len(set_fre_text.get(text)):
            if set_fre_text.get(text)[index4] != 0 and sum_array[index4] != 0:
                tf_idf = (1 + math.log(set_fre_text.get(text)[index4])) * math.log(len(list_text)/sum_array[index4])
                index4 += 1
                tf_idf_list.append(tf_idf)
            else:
                tf_idf_list.append(0)
                index4 += 1
        index4 = 0
        tf_idf_weight.setdefault(text, tf_idf_list)
        tf_idf_list = []

    print('>>>>>>', 'tf_idf_weight =', tf_idf_weight)
    print('===============================================')
    #===============================================
    order_text ={}
    list_tf_idf_weight = []
    list_tf_idf_weight_text = []
    for text in list_text:
        order_text.setdefault(text, sum(tf_idf_weight.get(text)))
    for text in list_text:
        if order_text.get(text) != 0:
            list_tf_idf_weight.append(order_text.get(text))
    Quick_Sort.Quick_Sort(list_tf_idf_weight, 0, len(list_tf_idf_weight)-1)
    list_order = list(order_text.items())
    if len(list_tf_idf_weight) != 0:
        count2 = 0
        while count2 < len(list_tf_idf_weight):
            for item in list_order:
                if item[1] == list_tf_idf_weight[count2] and item[1] != 0:
                    if item[0] not in list_tf_idf_weight_text:
                        list_tf_idf_weight_text.append(item[0])
                        count2 += 1
                        break
        print('>>>>>>', 'order_text =', order_text)
        print('===============================================')
        print('>>>>>>', 'list_tf_idf_weight = ', list_tf_idf_weight)
        print('===============================================')
        print('>>>>>>', 'list_tf_idf_weight_text =', list_tf_idf_weight_text)
        print('===============================================')
    else:
        print('No results were found')
        print('===============================================')
#===============================================
query_idf_weight = []
for index2 in range(len(sum_array)):
    if sum_array[index2] != 0:
        idf = math.log(len(list_text) / sum_array[index2])
        query_idf_weight.append(idf)
    else:
        query_idf_weight.append(0)
print('>>>>>>', 'query_idf_weight =', query_idf_weight)
print('===============================================')
#===============================================
list_score = []
set_score = {}
for text3 in list_text:
    for index3 in range(len(query_idf_weight)):
        score = tf_idf_weight.get(text3)[index3] * query_idf_weight[index3]
        list_score.append(score)
    set_score.setdefault(text3, list_score)
    list_score = []
print('>>>>>>', 'set_score =', set_score)
print('===============================================')
#===============================================
cosine_score = {}
list_cosine_score = []
list_cosine_score_text = []
for text in list_text:
    cosine_score.setdefault(text, sum(set_score.get(text)))
for text in list_text:
    if cosine_score.get(text) != 0:
        list_cosine_score.append(cosine_score.get(text))
Quick_Sort.Quick_Sort(list_cosine_score, 0, len(list_cosine_score)-1)
list_order = list(cosine_score.items())
if len(list_cosine_score) != 0:
    count2 = 0
    while count2 < len(list_cosine_score):
        for item in list_order:
            if item[1] == list_cosine_score[count2] and item[1] != 0:
                if item[0] not in list_cosine_score_text:
                    list_cosine_score_text.append(item[0])
                    count2 += 1
                    break
    print('>>>>>>', 'cosine_score =', cosine_score)
    print('===============================================')
    print('>>>>>>', 'list_cosine_score = ', list_cosine_score)
    print('===============================================')
    print('>>>>>>', 'list_cosine_score_text =', list_cosine_score_text)
    print('===============================================')
else:
    print('No results were found')
    print('===============================================')
#===============================================