import numpy as np
import pandas as pd
import scipy

import statsmodels
import statsmodels.formula.api import ols


#1. What Staticial test would you use for the following scenarios?
#(a) Does a student's current year (e.g., freshman, sophomore, etc.) effect their GPA?
    # Turkey HSD
#(b) Has the amount of snowfall in the mountains changed over time?
    #T Test
#(c) Over the last 10 years, have there been more hikers on average in Estes Park in the spring or summer?
# T Test
#(d) Does a student's home state predict their highest degree level?
# Anova

def generateDataset(filename):
    data = pd.read_csv(filename)
    df = data[0:]
    df = df.dropna()
    return data,df

def runTTest(ivA, ivB, dv):
    ttest = scipy.stats.ttest_ind(ivA[dv], ivB[dv])
    print(ttest)

def runAnova(data,formula):
    model = ols(formula, data).fit()
    aov_table = sm.stats.annova_lm (model, typ=2)
    print (aov_table)

rawData, df = generateDataset('simpsons_paradox.csv')

print("Does gender correlate with admissions?")
men = df[(df['Gender']=='Male')]
women = df[(['Gender'])=='Female']
runTTest(men,women,'Admitted')

print("Does department correlate with admissions?")
simpleFormula = 'Admitted ~ C(Deparment) + C(Gender)
runAnova(rawData, simpleFormula)

print("Does gender and Department correlate with admissions?")
moreComplex = 'Admitted~ C(Department) + C(Gender)'
runAnova(rawData, more Complex)

print(df.'simpsons_paradox'())
