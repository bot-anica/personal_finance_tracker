from datetime import datetime

from flask import Flask, request, redirect, url_for, render_template

from config import Config
from project.db import Transaction, db_session
from project.forms import AddTransactionForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/dashboard')
def index():  # put application's code here
    page = request.args.get("page") if request.args.get("page") and request.args.get("page").isdigit() else None
    limit = 10

    transactions = (Transaction.query
                    .offset(0 if page is None else (int(page) - 1) * limit)
                    .limit(limit)
                    .all())

    print(type(transactions), transactions)

    return render_template('index.html', data=transactions)


@app.route('/transactions/<transaction_id>')
def transaction(transaction_id):
    if (transaction_id is None) or not transaction_id.isdigit():
        return redirect(url_for('index'))

    transaction = Transaction.query.get(transaction_id)
    return render_template('transaction.html', transaction=transaction)


@app.route('/add_transaction', methods=["GET", "POST"])
def add_transaction():  # put application's code here
    form = AddTransactionForm()
    if form.validate_on_submit():
        date = datetime(*(int(item) for item in request.form.get("date").split("-")))
        description = request.form.get("description")
        type = request.form.get("type")
        amount = request.form.get("amount")

        print(date, description, type, amount)

        transaction = Transaction(date, type, amount, description)
        db_session.add(transaction)
        db_session.commit()

        return redirect(url_for('index'))

    return render_template('add_transaction.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
