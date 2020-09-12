from flask import Flask, render_template, request, session, redirect, url_for
import pickle
from flask_cors import cross_origin

app = Flask(__name__)
model = pickle.load(open('bank.pkl', 'rb'))
app.secret_key = '123'


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    global home_ownership, income_category, purpose, interest, grade, results
    if request.form.get('home_own') == 'Rent':
        home_ownership = 1
    elif request.form.get('home_own') == 'Own':
        home_ownership = 2
    elif request.form.get('home_own') == 'Mortgage':
        home_ownership = 3

    if request.form.get('inc_cat') == 'Low':
        income_category = 1
    elif request.form.get('inc_cat') == 'Medium':
        income_category = 2
    elif request.form.get('inc_cat') == 'High':
        income_category = 3

    if request.form.get('purpose') == 'Credit card':
        purpose = 1
    elif request.form.get('purpose') == 'Car':
        purpose = 2
    elif request.form.get('purpose') == 'Small business':
        purpose = 3
    elif request.form.get('purpose') == 'Other':
        purpose = 4
    elif request.form.get('purpose') == 'Wedding':
        purpose = 5
    elif request.form.get('purpose') == 'Debt consolidation':
        purpose = 6
    elif request.form.get('purpose') == 'Home improvement':
        purpose = 7
    elif request.form.get('purpose') == 'Major purchase':
        purpose = 8
    elif request.form.get('purpose') == 'Medical':
        purpose = 9
    elif request.form.get('purpose') == 'Moving':
        purpose = 10
    elif request.form.get('purpose') == 'Vacation':
        purpose = 11
    elif request.form.get('purpose') == 'House':
        purpose = 12
    elif request.form.get('purpose') == 'Renewable energy':
        purpose = 13

    if request.form.get('interest_cat') == 'Low':
        interest = 1
    elif request.form.get('interest_cat') == 'High':
        interest = 2

    if request.form.get('grade') == 'A':
        grade = 1
    elif request.form.get('grade') == 'B':
        grade = 2
    elif request.form.get('grade') == 'C':
        grade = 3
    elif request.form.get('grade') == 'D':
        grade = 4
    elif request.form.get('grade') == 'E':
        grade = 5
    elif request.form.get('grade') == 'F':
        grade = 6
    elif request.form.get('grade') == 'G':
        grade = 7

    emp_lenght = request.form['emp']
    # home_ownership = request.form['home_own']
    annual_income = request.form['ann_inc']
    # income_category = request.form['inc_cat']
    loan_amount = request.form['loan']
    term = request.form['term']
    # purpose = request.form['purpose']
    # interest = request.form['interest_cat']
    Interest_rate = request.form['Interest_rate']
    # grade = request.form['grade']
    dti = request.form['dti']
    total_payment = request.form['tot_pay']
    principal_amount = request.form['tot_prncp']
    installments = request.form['installments']

    values = [
        [float(emp_lenght), float(home_ownership), float(annual_income), float(income_category), float(loan_amount),
         float(term), float(purpose), float(interest),
         float(Interest_rate), float(grade), float(dti), float(total_payment), float(principal_amount),
         float(installments)]]

    prediction = model.predict(values)
    print(prediction)
    if int(prediction[0]) == 0:
        results = 'This is a Good loan and mostly he or she is not a defaulter'

    else:
        results = 'This is a bad loan and mostly he or she is a defaulter'

    session["res"] = results

    return redirect(url_for('result'))


@app.route('/result', methods=['GET'])
@cross_origin()
def result():
    if 'res' in session:
        res = session['res']
        return render_template('result.html', result=res)
    else:
        return redirect(url_for('home'))

