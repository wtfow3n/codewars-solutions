# ow3n
# 
# December 15, 2022
#

def order(sentence):
    if sentence == "":
        return sentence
    else:
        words = []
        for i in range(1,10):
            for word in sentence.split():
                if str(i) in word:
                    words.append(word)
        return " ".join(words)
