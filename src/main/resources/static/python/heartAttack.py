import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
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
	df=pd.read_csv("processed.cleveland.data",names=columns)
	df.loc[df['AHD']>1,'AHD']=1

	# find most common values per column to combat '?' values
	# QM = Question Mark
	replaceQMwithMode(df)

	X=df.drop(['AHD'],axis=1).values
	y=df['AHD'].values
	scale=StandardScaler()
	X=scale.fit_transform(X)
	X_train, X_test, Y_train, Y_test = train_test_split(X,y,test_size=0.3, random_state=42)
	model=RandomForestClassifier()
	model.fit(X_train,Y_train)
	Y_pred=model.predict(X_test)

	# ****** Accuracy ********

	score=round(accuracy_score(Y_pred,Y_test)*100,2)
	print("Accuracy score using Random Forest Classifier is: "+str(score)+" %")


	# ****** Cross validation Scores *******
	k_folds=10
	scores_train=cross_val_score(model,X_train,Y_train,cv=k_folds)


	print("Cross Validation Train Scores: ", scores_train)
	print("Average Train CV Score: ", scores_train.mean())

	scores_test=cross_val_score(model,X_train,Y_train,cv=k_folds)

	print("Cross Validation Test Scores: ", scores_test)
	print("Average Test CV Score: ", scores_test.mean())

	# ****** Save the model ****

	joblib.dump(model,'Heart_model.pkl')

if __name__ == "__main__":
	logic()  