# 문제 3: 문자열 찾기

def find_word(words, word) :
    words = words.lower()
    word = word.lower()
    words_list = words.split()
    
    adj_words_list = []
    for i in words_list :
        if i.endswith(',') :
            i = i.replace(',',"")
            adj_words_list.append(i)
        elif i.endswith('.') :
            i = i.replace('.',"")
            adj_words_list.append(i)
        else :
            adj_words_list.append(i)
    
    result = []
    for i in range(len(adj_words_list)) :
        if adj_words_list[i] == word :
            result.append(i)

    return result
