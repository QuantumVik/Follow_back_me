# Instagram Follow-Back Prediction Data Generation

This project simulates user interaction data on Instagram, focusing on predicting the likelihood of a user following back based on various factors such as follower count, engagement rate, interaction frequency, and account type. It generates synthetic datasets for training and testing purposes.

## Project Structure

The project consists of two Python scripts:

1. **Train_data_making.py**: This script generates synthetic training data based on several features that influence whether a user follows back.
2. **Test_data_making.py**: This script generates a separate test dataset with slight variations for model evaluation.

### Features Simulated

Both the training and testing data include the following features:

- **User_ID**: A unique identifier for each user.
- **Follower_Count**: Number of followers for each user, following a log-normal distribution.
- **Following_Count**: Number of accounts the user follows, derived from the follower count.
- **Posts_Count**: Number of posts made by the user, correlated with follower count.
- **Engagement_Rate**: Estimated engagement rate for the user, inversely proportional to the follower count.
- **Account_Type**: Whether the account is personal (0) or business (1).
- **Interaction_Frequency**: The frequency of interactions (likes, comments) based on the engagement rate.
- **Follow_Back**: Whether the user is likely to follow back (1) or not (0), based on the above features.

### Data Generation Logic

- **Follower Count and Following Count**: Users with fewer followers tend to follow back more frequently. The follower count is generated using a log-normal distribution, and the following count is proportional to the follower count.
  
- **Posts Count**: Larger accounts tend to post more frequently, but there’s variability in this relationship.

- **Engagement Rate**: Smaller accounts typically have higher engagement rates, while larger accounts tend to have lower rates. Business accounts generally have lower engagement than personal ones.

- **Follow Back**: Personal accounts with lower follower counts, higher engagement rates, and more frequent interactions are more likely to follow back.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/instagram-follow-back-prediction.git
   cd instagram-follow-back-prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install pandas numpy
   ```

## Usage

1. To generate the training dataset, run:
   ```bash
   python Train_data_making.py
   ```

2. To generate the test dataset, run:
   ```bash
   python Test_data_making.py
   ```

Both scripts will generate CSV files named `Instagram_dataset.csv` and `Instagram_test_dataset.csv`, respectively, in the specified directory.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
