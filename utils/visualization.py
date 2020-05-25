# Visualization Util

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from utils.constants import *


def word_cloud_visulization(df_column, description, stopword=True):
    """
    Word Cloud Visualization
    :param df_column:
    :param description:
    :param stopword:
    :return:
    """
    comment_words = ''
    stopwords = ''
    if stopword:
        stopwords = set(STOPWORDS)

    # iterate through the csv file
    for val in df_column:

        # typecaste each val to string
        val = str(val)

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens) + " "

    wordcloud = WordCloud(width=300, height=300,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    # plot the WordCloud image
    plt.figure(figsize=(15, 15))
    plt.title("WordCloud of {} column".format(description), fontdict=TITLE_FONT)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
