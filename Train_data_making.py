import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of records to simulate
num_records = 100000

# Create User_IDs
User_ID = np.arange(1, num_records + 1)

# Follower_Count: Users with fewer followers are more likely to engage and follow back
Follower_Count = np.random.lognormal(mean=9, sigma=1.2, size=num_records).astype(int)
Follower_Count = np.clip(Follower_Count, 50, 50000)  # Clipping to reflect realistic range

# Following_Count: Users tend to follow fewer accounts relative to their follower count
Following_Count = (Follower_Count * np.random.uniform(0.05, 0.5, size=num_records)).astype(int)

# Posts_Count: Users with more followers tend to post more, but it's not always proportional
Posts_Count = (Follower_Count * np.random.uniform(0.01, 0.03, size=num_records)).astype(int)
Posts_Count = np.clip(Posts_Count, 5, 1500)  # A more realistic range for post counts

# Engagement_Rate: Smaller accounts tend to have higher engagement, larger ones lower
Engagement_Rate = np.clip(10 / (np.log(Follower_Count + 1) + np.random.uniform(0.5, 1.5, size=num_records)), 0.01, 10)

# Account_Type: 70% personal, 30% business
Account_Type = np.random.choice([0, 1], size=num_records, p=[0.7, 0.3])  # 0: Personal, 1: Business

# Adjust Engagement Rate for business accounts (business accounts generally have lower engagement rates)
Engagement_Rate[Account_Type == 1] = Engagement_Rate[Account_Type == 1] * np.random.uniform(0.5, 0.9)

# Interaction_Frequency: Higher engagement leads to more interactions (likes/comments)
Interaction_Frequency = np.round(Engagement_Rate * np.random.uniform(10, 100, size=num_records)).astype(int)

# Loosen the conditions in Follow_Back logic for training data
# Further loosen the conditions in Follow_Back logic
Follow_Back = (
    (Engagement_Rate > 1.0) &  # Further lower the engagement rate threshold
    (Interaction_Frequency > 5) &  # Reduce the interaction frequency threshold more
    (Follower_Count < 20000) &  # Increase the follower count threshold for follow back
    (Account_Type == 0)  # Still focus on personal accounts, which are more likely to follow back
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

