import pandas as pd
from sklearn.model_selection import train_test_split

# Read the CSV file
df = pd.read_csv('calories.csv')

# Split into train and test datasets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=20)

# Save train and test datasets
train_df.to_csv('calories_train.csv', index=False)
test_df.to_csv('calories_test.csv', index=False)

# Split train dataset into two separate datasets
train_df1, train_df2 = train_test_split(train_df, test_size=0.5, random_state=20)

# Save the two separate datasets
train_df1.to_csv('calories_train_1.csv', index=False)
train_df2.to_csv('calories_train_2.csv', index=False)
