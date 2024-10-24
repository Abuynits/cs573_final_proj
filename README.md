# Predict Students' Dropout and Academic Success

## Team Composition

- **Shruti Ugalmugale**
- **Mohini Anand**
- **Alexiy Buynitsky**
- **Sang Hyun Kim**

## Project Topic

The project topic we have chosen is *Predict Students' Dropout and Academic Success*. This is a significant issue in the educational system, as early identification of students at risk of dropping out can enable institutions to intervene and provide necessary support, potentially lowering dropout rates and improving academic success. Our dataset includes features such as academic performance, socioeconomic status, attendance, and demographic data. Using these features, we will compare different data mining algorithms, including Decision Trees, K-means Clustering, and Support Vector Machines (SVM), to identify patterns and relationships. This analysis will allow us to provide insights into factors influencing dropout rates and academic success.

## Project Implementation

### Literature Survey

We will review relevant academic papers, focusing on research around student dropout predictions and academic performance prediction models. We aim to identify common algorithms used for these predictions, as well as any existing challenges or gaps in the current research where our project may contribute.

### Data Understanding and Exploration

We will start by downloading the database and pre-processing the data to ensure normalization. Then we will perform Exploratory Data Analysis (EDA) to visualize the data and identify critical features worth further analysis. Then, using the information discovered in our EDA, we will analyze the distribution of critical features and the correlation between features and target variables such as dropout.

### Algorithm Selection and Design

We will employ a **Classification Model** to classify students according to their risk of dropping out. We will compare and analyze the following algorithms to predict students' risk of dropping out:

- **XGBoost or LightGBM**: Gradient Boosting-based algorithms that boast high prediction performance. In particular, LightGBM is more memory-efficient than XGBoost, making it advantageous when handling large amounts of data. However, both models take a long time to train and may require complex hyperparameter tuning.

- **Multi-Layer Perceptron (MLP)**: A neural network model that excels at learning nonlinear relationships and shows high performance through complex interactions between various features. However, it requires a lot of computational resources, and hyperparameter tuning can be difficult and time-consuming.

- **Support Vector Machine (SVM)**: A model that is strong in linearly separating data in high-dimensional space. It is particularly effective in small datasets and can also handle nonlinear patterns well through kernels. However, performance degradation may occur in large datasets.

- **Decision Tree (or Gradient Boosting Decision Trees)**: An easy-to-interpret tree-based model that can easily explain the structure of data. Applying Gradient Boosting improves performance but increases computational cost. Pruning is essential to prevent overfitting.

- **K-Means Clustering**: An unsupervised learning algorithm that groups data points into similar clusters. It is fast, simple, and suitable for large datasets, but it is sensitive to the initial cluster center value and has the disadvantage of having to set the number of clusters in advance.

After considering the above algorithms first, we will analyze the data more deeply through the Data Exploration and Data Mining processes before selecting the final algorithm.

### Model Training and Evaluation

Once the algorithms are selected and designed, we will train them on the dataset. We will use cross-validation to ensure the generalizability of our models and measure performance using metrics like accuracy, precision, recall, and F1 score. For clustering, we will evaluate the quality of clusters using metrics like the silhouette score and the Davies-Bouldin index.

### Interpretation and Analysis

We will identify which features are the most influential in predicting dropout or academic success and create visualizations to better understand the model predictions. We will also study cases where the model performs poorly.

## Expected Outcome

We expect to achieve the following through our project:

- **Accurate identification of at-risk students**: We hope to identify students who are at risk of dropping out by using the historical data available. The classification model will be used to classify students into their risk level of dropping out by using features such as attendance, academic performance, socioeconomic factors, and demographic information.
  
- **Insights into influential factors**: Our analysis should give us insights into which factors (e.g., attendance, socioeconomic status) most strongly influence dropout rates and academic performance. This information could potentially allow targeted interventions and student support strategies.

## Evaluation Metrics

We will use the following evaluation metrics to determine the success of our project:

- **Classification Metrics**: We will assess the performance of our model using metrics such as the F1 score that balances precision and recall, and accuracy by identifying the proportion of correctly classified students.
  
- **Confusion Matrix Analysis**: We will use a confusion matrix to provide true positives, true negatives, false positives, and false negatives. This will allow us to identify specific areas for improvement in the model.
  
- **Receiver Operating Characteristic (ROC) Curve**: We will plot the ROC curves to visualize the trade-off between sensitivity and specificity at various thresholds to select an optimal decision boundary to classify students.

## Project Timeline

By the midterm report due date, we expect to have completed the literature survey, data exploration, and algorithm selection.

| **Activity**                   | **Duration** | **Expected Completion** |
|---------------------------------|--------------|-------------------------|
| Literature Survey               | 1 week       | September 28, 2024       |
| Data Understanding and Exploration | 2 weeks      | October 12, 2024         |
| Algorithm Selection and Design  | 2 weeks      | October 26, 2024         |
| Model Training and Evaluation   | 2 weeks      | November 13, 2024        |
| Interpretation and Analysis     | 1 week       | November 17, 2024        |
| Report Writing                  | 1 week       | November 24, 2024        |

## Citation

Realinho, V., Vieira Martins, M., Machado, J., & Baptista, L. (2021). Predict Students' Dropout and Academic Success [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5MC89.
