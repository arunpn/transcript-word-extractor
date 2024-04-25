# script to extract the words with a certain frequency from a transcript

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Ensure nltk resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Open and read the transcript file
with open('transcript.txt', 'r', encoding='utf-8') as file:
    transcript = file.read()

# Tokenize the text
tokens = word_tokenize(transcript)

# Convert all tokens to lowercase
lower_tokens = [token.lower() for token in tokens]

# Remove stopwords and non-alphabetic words
filtered_tokens = [word for word in lower_tokens if word.isalpha() and word not in stopwords.words('english')]

# Count the frequency of each word
word_freq = Counter(filtered_tokens)

# Select the 100 least common unique words
filtered_words = [word for word, freq in word_freq.most_common() if freq == 1]

#for word, freq in word_freq.most_common():
#  if freq == 1:
#    print(word)
  


# Printing the words in a Markdown table format
rows = [filtered_words[i:i+5] for i in range(0, len(filtered_words), 5)]
markdown_table = "| " + " | ".join(["Word 1", "Word 2", "Word 3", "Word 4", "Word 5"]) + " |\n" + \
                 "|-------" * 5 + "|\n" + \
                 "\n".join(["| " + " | ".join(row) + " |" for row in rows])

print(markdown_table)