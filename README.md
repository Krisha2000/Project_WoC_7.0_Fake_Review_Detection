# **Project WoC 7.0 - Fake Review Detection**  
**Winter of Code (DA-IICT)**  

Fake reviews have become a significant challenge in maintaining the authenticity of online platforms. This project leverages machine learning techniques to combat this issue by analyzing review data, identifying fraudulent patterns, and building accurate detection models. By enhancing trust in online reviews, the project contributes to a more reliable digital ecosystem.  

---

## **Progress**  

### **Checkpoint 1: Data Preparation**  
- Addressed missing values to ensure data completeness.  
- Processed text data by tokenizing, cleaning, and removing noise like stop words and punctuation.
- Apllied Word_to_vec model for vectorization.
- Aplied One hot encoding for cetagorical data. 
- Prepared a clean and structured dataset for modeling.  

### **Checkpoint 2: Model Training and Evaluation**  
- **Data Split:** Divided the preprocessed dataset into 80% training and 20% testing.  
- **Model Exploration:** Experimented with Random Forest, SVM, and Logistic Regression classifiers.  
- **Pipeline Creation:** Designed streamlined pipelines combining preprocessing steps and model application.  
- **Performance Metrics:** Evaluated models using accuracy, precision, recall, and F1 score.  

#### **Results**  
| **Model**               | **Accuracy** | **Precision** | **Recall** | **F1 Score** |  
|--------------------------|--------------|---------------|------------|--------------|  
| Random Forest            | 0.8409       | 0.8450        | 0.8409     | 0.8404       |  
| Support Vector Machine   | 0.8845       | 0.8846        | 0.8845     | 0.8844       |  
| Logistic Regression      | 0.8577       | 0.8578        | 0.8577     | 0.8577       |  

- **Model Selection:** SVM emerged as the best-performing model.  
- **Model Serialization:** Saved trained models (`Random_Forest_model.pkl`, `SVM_model.pkl`, and `Logistic_Regression_model.pkl`) for reuse.  

#### **SVM Model**  
[Download SVM Model](https://drive.google.com/file/d/1Ag5Mu9cIZ6UvugAEaRq4qClc3Q_prL89/view?usp=sharing)  

---

### **Checkpoint 3: Web Scraping Script for Review Collection**  
- **Web Scraping Script:** Developed a Python script to scrape reviews from any product URL.  
- **Libraries Used:** The script uses `requests` to fetch web content, `BeautifulSoup` for HTML parsing, and `pandas` for data handling and storage.  
- **Data Collection:** Extracted review details, including reviewer name, rating, review text, and review date.  
- **Result Storage:** The script saves the extracted reviews in a CSV file (`Reviews.csv`).  
- **Error Handling:** Added error handling for failed requests and issues with scraping.  
- **Input Flexibility:** The script accepts any product URL and scrapes the corresponding reviews.

---
I have trained a Multi-Layer Perceptron (MLP) model for fake review detection. Below are its performance metrics:

| **Model**               | **Accuracy** | **Precision** | **Recall** | **F1 Score** |  
|--------------------------|--------------|---------------|------------|--------------|  
| MLP                      | 0.8766       |0.88           | 0.88     |  0.88        |  

The MLP model provides competitive results and adds another option for classification. There is only a minor difference between SVM and MLP for these metrics, making both models viable choices for fake review detection.

---
### **Checkpoint 4: Web Application for Fake Review Detection**  
- **Language Filtering:** Implemented a filter to process only English-language reviews to ensure model compatibility.  
- **Streamlit Web App:** Developed an interactive web application using `Streamlit`, allowing users to input product URLs and classify reviews.  
- **Model Selection Feature:** Users can choose between `SVM` and `MLP` models for review classification.  
- **Visualization:** Integrated `Plotly` to display a pie chart representing the percentage of real vs. fake reviews.  
- **Result Display:** The app shows classified reviews with their corresponding labels for better transparency.  
- **Project Structure:** Modularized the codebase into separate scripts for scraping (`scraping.py`), preprocessing (`preprocessing.py`), and model inference (`model.py`).  

---

**Future Enhancements:** 
- Expand dataset to include multilingual reviews.  
- Experiment with deep learning models for enhanced accuracy.  
- Optimize the web scraper, which can scrape all reviews of that particular product.
- Deploy web application.
