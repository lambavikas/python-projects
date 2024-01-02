import pandas as pd
from wordcloud import STOPWORDS

# Step 3: Read the Excel file
file_path = 'C:/dev/python/Project2/testfile.xlsx'
data = pd.read_excel(file_path)

# Step 4: Concatenate the text data
text_data = ' '.join(data['Text'])

# Step 5: Split the text into individual words
words = text_data.split()

# Step 6: Count the frequency of each word
word_counts = pd.Series(words).value_counts().reset_index()

# Step 7: Rename the columns in the word_counts DataFrame
word_counts.columns = ['Word', 'Frequency']

# Step 8: Sort the words by frequency in descending order and reset index
word_counts = word_counts.sort_values(by='Frequency', ascending=False).reset_index(drop=True)

# Step 9: Add the rank column
word_counts['Rank'] = word_counts.index + 1

# Step 10: Get custom stopwords from the column named "Text"
custom_stopwords = set(data['Text'].astype(str))
stopwords = set(STOPWORDS).union(custom_stopwords)

# Step 11: Remove stopwords from the word_counts DataFrame
word_counts = word_counts[~word_counts['Word'].isin(stopwords)]

# Step 12: Write the ranked words (after removing stopwords) to a new tab in the same Excel file
with pd.ExcelWriter(file_path, mode='a') as writer:
    word_counts.to_excel(writer, sheet_name='Ranked Words (Without Stopwords)', index=False)

print("Ranked words (after removing stopwords) have been written to the 'Ranked Words (Without Stopwords)' tab in the Excel file.")
