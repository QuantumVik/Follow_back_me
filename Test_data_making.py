import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(24)

# Number of records to simulate for test data
num_test_records = 20000

# Create User_IDs for test data
User_ID_test = np.arange(1, num_test_records + 1)

# Follower_Count: Use similar log-normal distribution but with slight variations
Follower_Count_test = np.random.lognormal(mean=9, sigma=1.3, size=num_test_records).astype(int)
Follower_Count_test = np.clip(Follower_Count_test, 50, 50000)  # Same clipping range

# Following_Count: Proportional to follower count but with slight variability
Following_Count_test = (Follower_Count_test * np.random.uniform(0.05, 0.6, size=num_test_records)).astype(int)

# Posts_Count: Same logic as training data, with added noise for variability
Posts_Count_test = (Follower_Count_test * np.random.uniform(0.01, 0.04, size=num_test_records)).astype(int)
Posts_Count_test = np.clip(Posts_Count_test, 5, 1500)  # Same realistic range

# Engagement_Rate: Similar to training but with slightly adjusted logic
Engagement_Rate_test = np.clip(10 / (np.log(Follower_Count_test + 1) + np.random.uniform(0.7, 1.6, size=num_test_records)), 0.01, 10)

# Account_Type: Same 70% personal, 30% business distribution
Account_Type_test = np.random.choice([0, 1], size=num_test_records, p=[0.7, 0.3])

# Adjust Engagement Rate for business accounts (introduce more noise for test data)
Engagement_Rate_test[Account_Type_test == 1] = Engagement_Rate_test[Account_Type_test == 1] * np.random.uniform(0.5, 0.85)

# Interaction_Frequency: Same logic as training data but with more noise in the distribution
Interaction_Frequency_test = np.round(Engagement_Rate_test * np.random.uniform(10, 120, size=num_test_records)).astype(int)

# Follow_Back Logic for Test Data: Loosen conditions slightly
Follow_Back_test = (
    (Engagement_Rate_test > 1.0) &  # Keep the engagement rate condition similar to training data
    (Interaction_Frequency_test > 5) &  # Slightly relaxed interaction frequency condition
    (Follower_Count_test < 20000) &  # Same as in training data
    (Account_Type_test == 0)  # Personal accounts more likely to follow back
).astype(int)

# Create the test DataFrame
test_data = pd.DataFrame({
    'User_ID': User_ID_test,
    'Follower_Count': Follower_Count_test,
    'Following_Count': Following_Count_test,
    'Posts_Count': Posts_Count_test,
    'Engagement_Rate': Engagement_Rate_test,
    'Account_Type': Account_Type_test,
    'Interaction_Frequency': Interaction_Frequency_test,
    'Follow_Back': Follow_Back_test
})



# Save the dataset to a CSV file
test_data.to_csv(r'C:\Users\Asus\User_follow_back\pythonProject1\Instagram_test_dataset.csv', index=False)

