import nltk
import textstat
import re
import os
from collections import Counter
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download("punkt")

# Load stopwords
stopwords_dir = "../data/stopwords/"
stopwords_list = set()

for filename in os.listdir(stopwords_dir):
    with open(os.path.join(stopwords_dir, filename), "r", encoding="utf-8", errors="ignore") as f:
        stopwords_list.update(f.read().split())

# Load positive & negative words
with open("../data/MasterDictionary/positive-words.txt", "r") as f:
    positive_words = set(f.read().split())

with open("../data/MasterDictionary/negative-words.txt", "r") as f:
    negative_words = set(f.read().split())

def analyze_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Compute Scores
    positive_score = sum(1 for word in words if word.lower() in positive_words)
    negative_score = sum(1 for word in words if word.lower() in negative_words)
    polarity_score = (positive_score - negative_score) / max((positive_score + negative_score), 1)
    subjectivity_score = (positive_score + negative_score) / max(len(words), 1)

    avg_sentence_length = len(words) / max(len(sentences), 1)
    complex_word_count = sum(1 for word in words if textstat.syllable_count(word) > 2)
    percentage_complex_words = (complex_word_count / max(len(words), 1)) * 100
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

    syllables_per_word = sum(textstat.syllable_count(word) for word in words) / max(len(words), 1)
    avg_word_length = sum(len(word) for word in words) / max(len(words), 1)
    personal_pronouns = len(re.findall(r"\b(I|we|my|ours|us)\b", text, re.IGNORECASE))

    return [
        positive_score, negative_score, polarity_score, subjectivity_score,
        avg_sentence_length, percentage_complex_words, fog_index,
        complex_word_count, len(words), syllables_per_word, personal_pronouns, avg_word_length
    ]
