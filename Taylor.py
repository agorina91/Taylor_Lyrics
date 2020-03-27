import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/agorina/Desktop/taylor_swift_lyrics.csv', engine='python')

df.head()


album_by_year = df.groupby('year')['album'].count()

album_by_year.plot.bar()

import markovify
import string
import re

def strip_punct(string):
    no_punct_string = re.sub(r'[^\w\s]','', string)
    return no_punct_string

df['lyric'] = df.apply(lambda row: strip_punct(row['lyric']), axis=1)

text_model = markovify.NewlineText(df.lyric, state_size = 2)

for i in range(15):
    print(text_model.make_sentence())

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

text = " ".join(word for word in df.lyric)

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
