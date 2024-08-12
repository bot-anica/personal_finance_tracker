from flask_wtf import FlaskForm
from wtforms.fields import DateField, FloatField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class AddTransactionForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=255)])
    type = SelectField('Type', choices=[('income', 'Income'), ('expense', 'Expense')])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')
