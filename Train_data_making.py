import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of records to simulate
num_records = 100000

# Create synthetic data for each feature
User_ID = np.arange(1, num_records + 1)
Follower_Count = np.random.randint(50, 50000, size=num_records)
Following_Count = np.random.randint(20, 5000, size=num_records)
Posts_Count = np.random.randint(0, 1000, size=num_records)
Engagement_Rate = np.round(np.random.uniform(0.01, 10, size=num_records), 2)
Account_Type = np.random.choice([0, 1], size=num_records, p=[0.7, 0.3])  # 70% personal, 30% business
Interaction_Frequency = np.random.randint(0, 100, size=num_records)

# Create a logic for Follow_Back based on engagement, interaction, and account type
Follow_Back = (
    (Engagement_Rate > 2.5) &
    (Interaction_Frequency > 10) &
    (Follower_Count < 10000)
).astype(int)

# Create the DataFrame
data = pd.DataFrame({
    'User_ID': User_ID,
    'Follower_Count': Follower_Count,
    'Following_Count': Following_Count,
    'Posts_Count': Posts_Count,
    'Engagement_Rate': Engagement_Rate,
    'Account_Type': Account_Type,
    'Interaction_Frequency': Interaction_Frequency,
    'Follow_Back': Follow_Back
})

# Save the dataset to a CSV file
data.to_csv(r'C:\Users\Asus\User_follow_back\pythonProject1\Instagram_dataset', index=False)

