from flask_wtf import FlaskForm
from wtforms.fields import DateField, FloatField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp


class AddTransactionForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=255)])
    type = SelectField('Type', choices=[('income', 'Income'), ('expense', 'Expense')])
    amount = FloatField('Amount', validators=[])
    submit = SubmitField('Submit')
