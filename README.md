# Parkinson-s-Disease-Detection


- Overview
This repository contains code and documentation for a machine learning project aimed at detecting Parkinson's Disease based on input features like tremors, voice recordings, and other relevant clinical data.
 This project utilizes Python, Flask/Django for the user interface, and machine learning algorithms for accurate disease prediction.

- Dataset
The dataset used for this project includes clinical and biomedical voice measurements of patients, including attributes such as:
MDVP: Fo (Hz) - Average vocal fundamental frequency
MDVP: Fhi (Hz) - Maximum vocal fundamental frequency
MDVP: Flo (Hz) - Minimum vocal fundamental frequency
Jitter (%), Jitter (Abs), RAP, PPQ - Measures of variation in fundamental frequency
Shimmer, Shimmer (dB) - Measures of variation in amplitude
NHR, HNR - Measures of ratio of noise to tonal components in the voice
Status - Health status of the subject (Parkinson's - 1, Healthy - 0)

- 
Here's a README template for a GitHub repository focused on Parkinson's Disease detection:

Parkinson's Disease Detection
Overview
This repository contains code and documentation for a machine learning project aimed at detecting Parkinson's Disease based on input features like tremors, voice recordings, and other relevant clinical data. This project utilizes Python, Flask/Django for the user interface, and machine learning algorithms for accurate disease prediction.

Dataset
The dataset used for this project includes clinical and biomedical voice measurements of patients, including attributes such as:

MDVP: Fo (Hz) - Average vocal fundamental frequency
MDVP: Fhi (Hz) - Maximum vocal fundamental frequency
MDVP: Flo (Hz) - Minimum vocal fundamental frequency
Jitter (%), Jitter (Abs), RAP, PPQ - Measures of variation in fundamental frequency
Shimmer, Shimmer (dB) - Measures of variation in amplitude
NHR, HNR - Measures of ratio of noise to tonal components in the voice
Status - Health status of the subject (Parkinson's - 1, Healthy - 0)


- Repository Structure
data/: Contains the dataset used for training and testing.
notebooks/: Jupyter notebooks for different stages of the project.
01-Data-Exploration.ipynb: Initial exploration of the dataset.
02-Feature-Engineering.ipynb: Preprocessing and feature engineering steps.
03-Model-Training.ipynb: Training machine learning models for detection.
04-Model-Evaluation.ipynb: Evaluating model performance and results.
app/: Flask/Django application files for the user interface.
templates/: HTML templates for the web interface.
static/: Static files (CSS, JS, images) used in the web interface.
app.py: Main application script for running the Flask/Django app.
models/: Saved trained models.


- Requirements
Python 3.x
Flask (for the web interface)
Jupyter Notebook
Pandas, NumPy, Scikit-learn (for data manipulation and machine learning)
Matplotlib, Seaborn (for data visualization)

- Contributing
Contributions are welcome! If you find any issues or have improvements to suggest, please fork this repository, make your changes, and submit a pull request.
