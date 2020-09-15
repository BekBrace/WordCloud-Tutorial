'This program will show you how to generate Word Cloud'
#import dependencies
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Read Shakira csv file

rf = pd.read_csv(r'Youtube01-Psy.csv')
yt_comment_words = ''
stopwords = set(STOPWORDS)

# Iterate throught the CSV file
for value in rf.CONTENT:
    value = str(value)
    tokens = value.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        yt_comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=800, height=800, background_color='black',
                      stopwords=stopwords, min_font_size=10).generate(yt_comment_words)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
