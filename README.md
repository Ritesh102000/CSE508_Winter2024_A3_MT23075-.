# CSE508_Winter2024_A3_MT23075-.
# Amazon Electronics Product Review Analysis

This repository contains Python code for analyzing the Amazon Electronics Product Review dataset. Below is a detailed description of the steps involved in the analysis:

## Dataset Retrieval and Preparation
- Download the 5-core dataset for the Electronics Category from [Amazon Reviews Dataset](link).
- Read the file into a dataframe. Product metadata is kept in a separate dataframe.

## Product Selection and Initial Analysis
- Choose a product (e.g., 'Headphones') for analysis.

## Data Processing and Descriptive Statistics
- Calculate descriptive statistics for the chosen product:
  - Number of Reviews.
  - Average Rating Score.
  - Number of Unique Products.
  - Number of Good Ratings (threshold >= 3 as 'Good' and rest as 'Bad').
  - Number of Bad Ratings.
  - Number of Reviews corresponding to each Rating.

## Text Preprocessing
- Preprocess text data:
  - Remove HTML Tags.
  - Remove Accented Characters.
  - Expand Acronyms.
  - Remove Special Characters.
  - Lemmatization.
  - Create a Text Normalizer function.

## Exploratory Data Analysis (EDA)
- Conduct EDA to extract relevant statistics:
  - Top 20 Most Reviewed Brands.
  - Top 20 Least Reviewed Brands.
  - Most Positively Reviewed Product.
  - Count of Ratings Over 5 Consecutive Years.
  - Word Clouds for 'Good' and 'Bad' Ratings.
  - Distribution of Ratings vs. Number of Reviews.
  - Year with Maximum Reviews.
  - Year with the Highest Number of Customers.

## Feature Engineering and Model Evaluation
- Feature Engineering:
  - Bag of Words (BoW) Model using CountVectorizer.
- Rating Class Division:
  - 'Good', 'Average', and 'Bad' categories based on ratings.
- Train-Test Split (75:25 ratio).
- Model Evaluation:
  - Logistic Regression.
  - Decision Tree.
  - Random Forest.
  - AdaBoost.
  - K-Nearest Neighbors (KNN).
- Generate classification report for each model.

## Collaborative Filtering
- Implement user-user and item-item recommender systems:
- User-Item Rating Matrix.
- Normalization using min-max scaling.
- User-User Recommender System:
  - Find top N similar users using cosine similarity.
  - Perform K-fold validation (K=5) and report MAE for different values of N.
- Item-Item Recommender System:
  - Similar steps as user-user recommender system.
- Plot MAE Against K for both systems.

## Top 10 Products by User Sum Ratings
- Report the top 10 products by the sum of ratings.

## Repository Structure
- `data/`: Contains the dataset.
- `notebooks/`: Jupyter notebooks for analysis.
- `scripts/`: Python scripts for preprocessing and modeling.
- `results/`: Output files and visualizations.

## Usage
- Clone the repository.
- Download the dataset from the provided link.
- Run the notebooks or scripts for analysis.

## Dependencies
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- NLTK
- WordCloud


