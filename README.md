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

## **Conclusion**  
The SVM model demonstrated the best performance and reliability for detecting fake reviews. This project showcases the power of machine learning in addressing real-world challenges.  
