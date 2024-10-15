from heapq import nlargest
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

#text = """Artificial intelligence (AI) has become an integral part of many industries, ranging from healthcare to finance. Its ability to process large amounts of data and generate insights has revolutionized how businesses operate. In healthcare, for instance, AI algorithms help doctors make better decisions by analyzing patient data to predict outcomes. In the finance sector, AI-powered tools assist in risk management and fraud detection, making transactions more secure. However, there are concerns about privacy and the ethical use of AI. As AI systems become more powerful, it's important to ensure they are used responsibly and transparently. Researchers are working on ways to make AI more explainable so that people can trust and understand the decisions made by machines."""

def summarizer(rawdocs):
    print("========Test========")
    stopwords = list(STOP_WORDS)
    #print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    #print(doc)
    tokens = [token.text for token in doc]
    #print(tokens)

    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text] += 1

    #print(word_freq)

    max_freq = max(word_freq.values())
    #print(max_freq)

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq
    #print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    #print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
    #print(sent_scores)
    select_len = int(len(sent_tokens) * 0.3)
    #print(select_len)
    summary = nlargest(select_len, sent_scores, key = sent_scores.get)
    #print(summary)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    # print("Text : ",text)
    # print("Summary : ",summary)
    # print()
    # print("Length of original text : ",len(text.split(' ')))
    # print("Length of summary text :",len(summary.split(' ')))

    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))



print("--------------End Test------------------")