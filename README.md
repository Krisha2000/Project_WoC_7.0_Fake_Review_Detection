# Project_WoC_7.0_Fake_Review_Detection

## Preprocessed Dataset Link : https://drive.google.com/file/d/1MDZTVdUgREkeqAqMcyk_MYizTSwaeGzd/view?usp=sharing
(As the File was too big to upload on GitHub)

## Check Point : 1

### Task Breakdown

#### Data Preprocessing Steps

1. **Data Cleaning**:
   - Handle missing values and irrelevant entries.
   - Remove duplicates and incomplete data.

2. **Text Normalization**:
   - Convert all text to lowercase to maintain uniformity.
   - Remove punctuation, special characters, and numbers that are unnecessary for review analysis.

3. **Tokenization**:
   - Split each review into individual words (tokens).

4. **Stopword Removal**:
   - Eliminate common words (e.g., "and", "the") that do not add significant meaning for the analysis.

5. **Lemmatization**:
   - Reduce words to their root or base form (e.g., "running" → "run").

6. **Vectorization**:
   - Convert text data into numerical formats using techniques like Word2Vec to make it suitable for machine learning models.

7. **Label Encoding**:
   - Encode categorical values (e.g., fake or genuine reviews) into numeric format.

