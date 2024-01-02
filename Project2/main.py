import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Step 3: Read the Excel file
data = pd.read_excel('C:/dev/python/Project2/testfile.xlsx')

# Step 4: Concatenate the text data
text_data = ' '.join(data['Text'])

# Step 5: Create a set of stopwords
stopwords = set(STOPWORDS)

# Step 6: Get custom stopwords from the column named "STOPWORDS"
custom_stopwords = set(data['STOPWORDS'].astype(str))
stopwords = stopwords.union(custom_stopwords)

# Step 7: Generate the word cloud with stopwords
wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords)

# Step 8: Generate word cloud by processing the text data
wordcloud.generate(text_data)

# Step 9: Represent the word cloud as a plot of words
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.show()


