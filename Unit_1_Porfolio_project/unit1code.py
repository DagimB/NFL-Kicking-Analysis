import pandas as pd
# from google.colab import files
# files.upload()

nfl = pd.read_csv('nfl2008_fga.csv')

nfl.head()

nfl.shape

nfl.value_counts()

nfl['GOOD'].value_counts()

import numpy as np

total_kicks = 900 + 139

good_pct = nfl['GOOD'].value_counts(normalize = 100)*100

print(total_kicks)

print(good_pct)

import seaborn as sns
sns.catplot(x= 'GOOD' , data=nfl, kind= 'count')

nfl['kickdiff'].mean()

kick_dist_marg = pd.crosstab(index= nfl['homekick'], columns= nfl['GOOD'], margins=True)
kick_dist_marg

kick_dist = pd.crosstab(index= nfl['homekick'], columns= nfl['GOOD'])
kick_dist

kick_dist.plot(kind="bar")

nfl['kickdiff'].value_counts()

nfl['abskickdiff'] = abs(nfl['kickdiff'])
nfl

nfl['abskickdiff'].value_counts()

from scipy.stats import chi2_contingency
g, p, dof, expctd= chi2_contingency(pd.crosstab(index= nfl['homekick'], columns= nfl['GOOD']))

print(g)
print(p)
print(dof)
print(expctd)

pd.DataFrame(expctd)

print(p)

Good = nfl[nfl['GOOD'] == 1]
Not_Good = nfl[nfl['GOOD'] == 0]

fig, ax = plt.subplots()
ax.hist(Good['abskickdiff'], label= 'Good')
ax.hist(Not_Good['abskickdiff'], label = 'Not Good')


ax.set_xlabel('Difference In Score') 
ax.set_ylabel('Frequency') 
# ax.set_title('Age of Titanic Passengers by Sex') 

ax.legend()

plt.show()

stats.ttest_ind(Distance_Good['distance'], Distance_NotGood['distance'])

nfl['distance'].value_counts()

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.hist(nfl['distance'])

Good = nfl[nfl['GOOD'] == 1]
Not_Good = nfl[nfl['GOOD'] == 0]

fig, ax = plt.subplots()
ax.hist(Good['distance'], label= 'Good')
ax.hist(Not_Good['distance'], label = 'Not Good')


ax.set_xlabel('Distance') 
ax.set_ylabel('Frequency') 
# ax.set_title('Age of Titanic Passengers by Sex') 

ax.legend()

plt.show()

Distance_Good

from scipy import stats
stats.ttest_ind(Good['distance'], Not_Good['distance'])

print(Distance_Good['distance'].mean())
print(Distance_NotGood['distance'].mean())


Good = nfl[nfl['GOOD'] == 1]
Not_Good = nfl[nfl['GOOD'] == 0]

fig, ax = plt.subplots()
ax.hist(Good['abskickdiff'], label= 'Good')
ax.hist(Not_Good['abskickdiff'], label = 'Not Good')


ax.set_xlabel('Difference In Score') 
ax.set_ylabel('Frequency') 
# ax.set_title('Age of Titanic Passengers by Sex') 

ax.legend()

plt.show()

stats.ttest_ind(Good['abskickdiff'], Not_Good['abskickdiff'])
