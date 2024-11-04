import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
print(data.info())
print(data.describe())
data.fillna(data.mean(), inplace=True)
filtered_data = data[data['age'] > 30]
gender_age_mean = data.groupby('gender')['age'].mean()
data['age'].hist(bins=10)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
gender_age_mean.plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Average Age')
plt.title('Average Age by Gender')
plt.show()
