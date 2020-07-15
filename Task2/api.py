#!C:\Users\prince\Anaconda3\python.exe
import flask
import pandas as pd
import numpy as np

app = flask.Flask(__name__)
app.config["DEBUG"] = True
#Load the dataset
Dataset = pd.read_csv('Data.csv')


@app.route('/api1', methods=['GET'])
def task_1():
   rs1 = Dataset.groupby(['City','Product line'])
   rs1= rs1.apply(lambda x: x.sort_values(by = 'Rating',ascending = False).head(1))
   rs1 = rs1.sort_values('Rating',ascending=False)
   rs1 = rs1.apply(lambda x: x.groupby(['City']).head(5))
   rs1 = rs1[['City','Product line','Rating']]
   rs1 = rs1.apply(lambda x: x.groupby(['City','Product line']))
   return rs1.to_json()

@app.route('/api2', methods=['GET'])
def task_2():
   rs2 = Dataset.iloc[:,9:11]
   rs2 = rs2.groupby(['Payment Mode']).sum()
   return rs2.to_json(orient='index')
    
	
@app.route('/api3', methods=['GET'])
def task_3():
   rs3 = Dataset.groupby(['Branch','Product line']).mean()
   result = rs3.Rating
   return result.to_json(orient= 'index')

app.run(port=82)
