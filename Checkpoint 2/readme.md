## **Check Point: 2 - Model Training**

**SVM model : https://drive.google.com/file/d/1Ag5Mu9cIZ6UvugAEaRq4qClc3Q_prL89/view?usp=sharing**


(Random Forest and Logistic Regression Model are uploaded)

### **Tasks Completed**

#### 1. Dataset Preparation
- Loaded the preprocessed dataset created during Checkpoint 1.
- Split the dataset into **training (80%)** and **testing (20%)** sets.

#### 2. Model Selection
Experimented with the following classifiers:
- **Random Forest**
- **Support Vector Machine (SVM)**
- **Logistic Regression**

#### 3. Pipeline Creation
Constructed pipelines for efficient preprocessing and classification. These pipelines included:
- **Feature scaling** where necessary.
- Application of machine learning models.

#### 4. Model Training
Trained each classifier using the training dataset.

#### 5. Model Evaluation
Each model was evaluated using the following metrics:
- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**

#### **Model Performance Table**
| **Model**                  | **Accuracy** | **Precision** | **Recall** | **F1 Score** |
|----------------------------|--------------|---------------|------------|--------------|
| Random Forest              | 0.8409       | 0.8450        | 0.8409     | 0.8404       |
| Support Vector Machine (SVM) | 0.8845       | 0.8846        | 0.8845     | 0.8844       |
| Logistic Regression        | 0.8577       | 0.8578        | 0.8577     | 0.8577       |

#### 6. Model Serialization
Saved each trained model for future use with the following filenames:
- `Random_Forest_model.pkl`
- `SVM_model.pkl`
- `Logistic_Regression_model.pkl`

#### 7. Test Predictions
Performed test predictions using the saved models on sample data to validate their functionality.

| Actual | Predicted by SVM |
|--------|------------------|
| 1      | 0                |
| 0      | 1                |
| 1      | 0                |
| 1      | 0                |
| 0      | 0                |
| 0      | 1                |
| 0      | 1                |
| 1      | 0                |
| 1      | 1                |
| 0      | 1                |
(For SVM)


## Conclusion
Based on the evaluation metrics, the Support Vector Machine (SVM) performed the best with the highest F1 Score (0.8844), making it the most suitable model for detecting fake reviews in this task.

