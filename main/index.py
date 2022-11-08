from flask import Flask, jsonify, request

from main.model.expense import Expense, ExpenseSchema
from main.model.income import Income, IncomeSchema 
from main.model.transaction_type import TransactionType

app = Flask(__name__)

transactions = [
Income('Salary', 5000), Income('Dividends', 200),
Expense('Pizza', 50), Expense('Rock Concert', 100)
]

@app.route('/')
def welcome():
    return 'Welcome to the Homepage'

@app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
        )
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return "", 204

@app.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
        )
    return jsonify(expenses)

@app.route('/expenses', methods=['POST'])
def add_expenses():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return "", 204


if __name__ == "__main__":
    app.run(host='127.0.0.7', port=8080)

