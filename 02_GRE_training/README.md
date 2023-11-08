# Analysis Using Tensorflow

#### This project involves looking at Graduate Record Examination (GRE) scores and seeing if a student's score would allow them admission into the University of Southern California (USC) chemistry program.

Here, two different methods are introduced:
1. `01_classification_training`: Classification
- Here, the `softmax` activation function is used in the last layer of the neural network. This activation function is used in multi-class classification functions to provide a result of probabilities the predicted value is in various classes. Three classes are used in this example. A value of `0` is assigned to "no admission", `1` assigned to "possible admission", and `2` indicates "definite admission".
2. `02_normalized_regression_training`: Regression
- A regression analysis is used to predict the probability of admission instead of classifying the admission as in the first example. Here, a decimal is used to predict the admission, with a value of `0.00` meaning no possible admission and `1.00` given to mean a guaranteed chance of admission.
- This regression analysis further uses <b> normalized data </b> for a more accurate result.
