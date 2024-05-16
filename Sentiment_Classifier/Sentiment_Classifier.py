punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
def strip_punctuation(x):
    for i in punctuation_chars:
        x= str(x).replace("%s" % i, '')
    return x

def get_pos(sent):
    l_s = sent.lower()
    non_p = strip_punctuation(l_s)
    splitted_=non_p.split()
    print (splitted_)
    poss= 0 
    for w in splitted_:
        if w in positive_words:
            poss = poss +1
    return poss
def get_neg (sent):
    l_s = sent.lower()
    non_p = strip_punctuation(l_s)
    splitted_=non_p.split()
    print (splitted_)
    neg= 0 
    for w in splitted_:
        if w in negative_words:
            neg = neg +1
    return neg

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

fileop =open("project_twitter_data.csv","r")
data = fileop.readlines()
               
out = open("resulting_data.csv","w")
out.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
out.write("\n")
for i in data[1:]  :   
    row = ""
    new_splt = i.strip().split(",")
    row=("{},{},{},{},{}".format(new_splt[1], new_splt[2], get_pos(new_splt[0]), get_neg(new_splt[0]), (get_pos(new_splt[0])-get_neg(new_splt[0]))))
   
    out.write(row)
    out.write("\n")

out.close()
