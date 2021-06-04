import numpy as np

names = np.array(["Susan","Jim","Joe","Jane","Sam","Michelle"])
row_names = np.array([["________"],["Susan   "],["Jim     "],["Joe     "],["Jane    "],["Sam     "],["Michelle"]])

# Data below has already been normalized from given example data
# Code is not capable normalizing data

gender_data = np.array([[0],[1],[1],[0],[1],[0]])

nomimal_data = np.array([["B", "O-"],
                         ["R", "O+"],
                         ["R", "AB-"],
                         ["G", "A+"],
                         ["B", "A-"],
                         ["B", "O-"]])

# Health Data Conversions
#   0       = Poor
#   0.33    = Fair
#   0.66    = Good
#   1       = Excellent  
general_health_data = np.array([[1],[0.66],[0.33],[0],[0.66],[0.66]])

# Test1 Data was normalized
# Original Data: 75, 65, 64, 83, 71, 90
test1_data = np.array([[0.42307692307],
                       [0.03846153846],
                       [0],
                       [0.73076923076],
                       [0.26923076923],
                       [1]])

# Asymmetric Binary Data
asym_data = np.array([[0,0],
                      [0,0],
                      [0,1],
                      [1,1],
                      [0,0],
                      [0,0]])


