import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
print ("Setup complte")

file = "melb_data.csv"
data = pd.read_csv(file, index_col="Date", parse_dates=True)
data.head()

plt.figure(figsize=(16, 6))
sns.lineplot(data = data)
