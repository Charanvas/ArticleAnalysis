import pandas as pd
import os
from text_analysis import analyze_text

# Load input file
input_file = "../data/input.xlsx"
df = pd.read_excel(input_file)

# Prepare output DataFrame
columns = [
    "URL_ID", "URL", "POSITIVE SCORE", "NEGATIVE SCORE", "POLARITY SCORE", "SUBJECTIVITY SCORE",
    "AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS", "FOG INDEX",
    "COMPLEX WORD COUNT", "WORD COUNT", "SYLLABLE PER WORD", "PERSONAL PRONOUNS", "AVG WORD LENGTH"
]
output_df = pd.DataFrame(columns=columns)

# Analyze extracted articles
article_dir = "../output/articles"

for _, row in df.iterrows():
    file_path = os.path.join(article_dir, f"{row['URL_ID']}.txt")

    if os.path.exists(file_path):
        analysis_results = analyze_text(file_path)
        output_df = output_df.append(pd.Series([row["URL_ID"], row["URL"]] + analysis_results, index=columns), ignore_index=True)

# Save to Excel
output_file = "../output/Output Data Structure.xlsx"
output_df.to_excel(output_file, index=False)
print(f"Results saved to {output_file}")
