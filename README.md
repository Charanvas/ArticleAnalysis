# **YouTube Article Analysis Project**

## **Project Overview**
This project extracts articles from URLs, performs text analysis using NLP techniques, and saves the results in an Excel file. The analysis includes sentiment scores, readability metrics, and linguistic statistics.

## **Project Structure**
```
Project/
│── src/
│   │── extract_articles.py      # Extracts article text from URLs
│   │── text_analysis.py         # Performs text analysis
│   │── main.py                  # Main execution script
│── data/
│   │── input.xlsx               # Input file with URLs
│   │── stopwords/               # Folder containing stopword files
│── output/
│   │── Output Data Structure.xlsx  # Output file
│── requirements.txt             # Required Python libraries
│── README.md                    # Instructions for running the project
```

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repository/project.git
cd project
```

### **2. Install Dependencies**
Ensure you have Python installed (>=3.8). Install dependencies using:
```bash
pip install -r requirements.txt
```

## **Input File Format (`data/input.xlsx`)**
The input Excel file must contain two columns:
| URL_ID  | URL |
|---------|-------------------------------------------------|
| 1001    | https://example.com/article1 |
| 1002    | https://example.com/article2 |

## **Usage Instructions**

### **1. Extract Articles**
This script fetches text from the URLs and saves them as text files.
```bash
python src/extract_articles.py
```
#### **Output:**
Extracted articles are stored in `/output/articles/` as `.txt` files.

---

### **2. Perform Text Analysis**
This script processes extracted articles and generates linguistic statistics.
```bash
python src/main.py
```
#### **Output:**
The results are saved in `/output/Output Data Structure.xlsx`.

## **Output File Format (`Output Data Structure.xlsx`)**
| URL_ID | URL | POSITIVE SCORE | NEGATIVE SCORE | POLARITY SCORE | ... |
|--------|-----|---------------|---------------|---------------|-----|
| 1001   | https://example.com/article1 | 12 | 5 | 0.3 | ... |

## **Analysis Metrics**
| Metric | Description |
|------------|---------------------------------------------------------|
| Positive Score | Count of positive words in the article |
| Negative Score | Count of negative words in the article |
| Polarity Score | Sentiment polarity: (Positive - Negative) / Total |
| Subjectivity Score | Measure of opinionated words in the text |
| Avg Sentence Length | Words per sentence |
| Percentage of Complex Words | % of words with >2 syllables |
| FOG Index | Readability score |
| Complex Word Count | Number of complex words |
| Word Count | Total words |
| Syllable per Word | Average syllables per word |
| Personal Pronouns | Count of personal pronouns |
| Avg Word Length | Average characters per word |

## **Troubleshooting**
### **1. Failed to Fetch URLs**
- Ensure the URLs are correct.
- Check your internet connection.
- Some websites block bots; try using a VPN or modifying headers.

### **2. Encoding Issues (UnicodeDecodeError)**
- Ensure your terminal supports UTF-8.
- Run: `export PYTHONIOENCODING=utf-8`

### **3. Pandas Excel Write Error**
- Install `openpyxl`: `pip install openpyxl`

## **License**
This project is open-source under the MIT License.

---

Now you're ready to analyze articles! 🚀

