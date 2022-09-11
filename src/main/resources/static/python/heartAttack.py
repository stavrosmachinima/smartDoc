import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

import joblib

def findColumnQM(df):
	questionColumn=[]
	for i in df.columns:
		newDf=df.loc[lambda df:df[i]=='?']
		if (not newDf.empty):
			questionColumn.append(i)
	return questionColumn

def replaceQMwithMode(df):
	questionColumn=findColumnQM(df)
	for i in questionColumn:
		df[i].replace('?',df[i].mode().values[0],inplace=True)
	


def diseaseAgeCorrelation(df):
	pd.crosstab(df.Age,df.AHD).plot(kind="bar")
	plt.title('Heart Disease Frequency for Ages')
	plt.ylim(top=15)
	plt.xticks(rotation=0)
	plt.xlabel('Age')
	plt.ylabel('Frequency')
	plt.show()

def diseaseSexCorrelation(df):
	pd.crosstab(df.Sex,df.AHD).plot(kind="bar",figsize=(15,6))
	plt.title('Heart Disease Frequency for Sex')
	plt.xlabel('Sex (0=Female, 1= Male)')
	plt.xticks(rotation=0)
	plt.legend(["Haven't Disease", "Have Disease"])
	plt.ylabel('Frequency')
	plt.show()

def heatMap(df):
	corr=df.corr()
	plt.figure(figsize=(18,10))
	plt.xticks(rotation=0)
	sns.heatmap(corr, annot=True)
	plt.show()

def logic():
	columns=['Age','Sex','ChestPain','RestBP','Chol','Fbs','RestECG','MaxHR','ExAng','Oldpeak','Slope','Ca','Thal','AHD']
	df=pd.read_csv("../data/processed.cleveland.data",names=columns)
	df.loc[df['AHD']>1,'AHD']=1

	# find most common values per column to combat '?' values
	# QM = Question Mark
	replaceQMwithMode(df)
	df['Ca']=df['Ca'].astype(float)
	df['Thal']=df['Thal'].astype(float)

	X=df.drop(['AHD'],axis=1).values
	Y=df['AHD'].values

	# print(np.count_nonzero(Y==0))
	# print(np.count_nonzero(Y==1))
	# Apo ta parapanw apotelesmata diakrinoume oti kamia ta3h den einai overrepresented. Ara dn xreiazetai na xrhsimopoihsoume stratifiedKfold

	# *********** StandardScaler comes into play when the characteristics of the input dataset differ greatly between their ranges, or simply when they are measured in different units of measure. *******
	# scale=StandardScaler()
	# X=scale.fit_transform(X)
	# print('ScaledX:'+str(X))
	X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=42)
	model=LinearDiscriminantAnalysis()
	model.fit(X_train,Y_train)
	Y_pred=model.predict(X_test)

	testArray=[41.0,0.0,3.0,112.0,268.0,0.0,2.0,172.0,1.0,0.0,1.0,0.0,3.0]

	print(model.predict(np.asarray(testArray).reshape(1,-1)))

	# ****** Accuracy ********

	score=round(accuracy_score(Y_pred,Y_test)*100,2)
	print("Accuracy of LinearDiscriminantAnalysis is: "+str(score)+"%")


	# ****** Cross validation Scores *******
	k_folds=10
	scores_train=cross_val_score(model,X_train,Y_train,cv=k_folds,scoring='accuracy')


	# #print("Cross Validation Train Scores: ", scores_train)
	print("Average Train CV Score: "+ str(round(scores_train.mean()*100,2))+"%")

	scores_test=cross_val_score(model,X_train,Y_train,cv=k_folds,scoring='accuracy')

	# #print("Cross Validation Test Scores: ", scores_test)
	print("Average Test CV Score: "+ str(round(scores_test.mean()*100,2))+'%')

	# # ****** Save the model ****
	print('Saving the model...')
	joblib.dump(model,'Heart_model.pkl')

	models=[]
	models.append(('RFC',RandomForestClassifier()))
	models.append(('LR',LogisticRegression(solver='liblinear',multi_class='ovr')))
	models.append(('LDA',model))
	models.append(('KNN',KNeighborsClassifier()))
	models.append(('CART', DecisionTreeClassifier()))
	models.append(('NB', GaussianNB()))
	models.append(('SVM', SVC(gamma='auto')))
	for name,model in models:
		cv_results=cross_val_score(model,X_train,Y_train,cv=k_folds,scoring='accuracy')
		print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))


if __name__ == "__main__":
	logic()  