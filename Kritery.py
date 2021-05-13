import matplotlib.pyplot as plt
import pandas
from scipy import stats

df = pandas.read_csv("Dannye.csv")
print(df)

df['count'].plot(kind='bar')

df12 = pandas.DataFrame(data={
    'df1': df['count'],
})
df12.plot.kde()
plt.show()

d1 = df12['df1']
print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=len(d1)))