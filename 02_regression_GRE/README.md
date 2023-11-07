# Regression Analysis Using Tensorflow

#### This project involves looking at Graduate Record Examination (GRE) scores and seeing if a student's score would allow them admission into a variety of universities.

Files:
1. `generate_scores.py`: Generates random scores that allow admission into the University of Southern California Chemistry Program.
- This file may generate four different text files, which store the data:
    - `combined_data.txt` which includes the data for both the verbal and quantitative assessments
    - `admit_data.txt` which includes whether or not (or maybe) a student would be admitted given their scores and assigns a value of 0 (no admission), 1 (maybe admission), and 2 (definite admission). (WORK IN PROGRESS - MUST BE CORRECTED)
    - `quantitative_data.txt` and `verbal_data.txt` which was an old test on how to produce the data files. No longer in use, but holds the data scores for each independent test area.
2. `GRE_regression.py`: Trains and predicts the machine learning model. Still does not provide the most accurate results, but most likely due to bad data.
3. `scores_plot.png`: Visualizes the score data in terms of the admissions data.
- This file may generate three different plots:
    - `verbal.png` which is the verbal scores versus admission
    - `quant.png` which is the quantitative scores versus admission
    - `scores_plot.png` which is just a scatter plot of the quantitative and verbal data
