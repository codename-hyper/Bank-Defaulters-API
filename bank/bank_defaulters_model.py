import pandas as pd
import pickle

file = 'loan_defaulter.csv'
loan_data = pd.read_csv(file)

loan_data = loan_data.iloc[:1001,:]

data = loan_data.drop(columns = ['final_d','year','recoveries','id','home_ownership','income_category','application_type','application_type_cat','interest_payments','loan_condition','grade','region','issue_d','purpose','term'])

y = data.pop('loan_condition_cat')
x = data

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.30,random_state = 100)

model_log = LogisticRegression(max_iter=10000)

model_log.fit(x_train,y_train)

pickle.dump(model_log,open('bank.pkl','wb'))

model = pickle.load(open('bank.pkl','rb'))

