import joblib
import numpy as np
import json

def predict():

	# # ***** For current directory use only *****
	# with open("Heart_model.pkl","rb") as file:
	# 	clfr=joblib.load(file)

	# with open("parameters.txt","r") as file:
	# 	parameters=json.loads(file.read().replace("'",'"'))


	# ***** Use with Java ******

	with open("src/main/resources/static/python/Heart_model.pkl","rb") as file:
		clfr=joblib.load(file)

	with open("src/main/resources/static/python/parameters.txt","r") as file:
		parameters=json.loads(file.read().replace("'",'"'))

	# reshaping needs to be done for numpy prediction
	inputFeature=np.asarray(list(parameters.values())).reshape(1,-1)
	prediction=clfr.predict(inputFeature)
	print(prediction[0])

if __name__=='__main__':
	predict()