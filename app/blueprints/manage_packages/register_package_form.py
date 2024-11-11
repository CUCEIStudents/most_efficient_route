from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Regexp
from wtforms_sqlalchemy.orm import QuerySelectField
from app.models import Status, Permit

class RegisterPackageForm(FlaskForm):
    USR_email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    USR_telephone = StringField('Teléfono', validators=[DataRequired(), Regexp('^\d{10}$')])
    plain_password = PasswordField('Contraseña', validators=[DataRequired(), Regexp('^(?=.*[A-Z])(?=.*[!@#$%^&*(),.?":{}|<>])(?=.{8,})')])
    USR_name = StringField('Nombre', validators=[DataRequired()])
    USR_last_name = StringField('Apellido', validators=[DataRequired()])
    USR_address = StringField('Dirección', validators=[DataRequired()])
    status = QuerySelectField(
        'Estado', 
        query_factory=lambda: Status.query.filter_by(ST_status_type=1).all(), 
        get_label='ST_value', 
        validators=[DataRequired()]
    )
    permit = QuerySelectField(
        'Tipo de usuario', 
        query_factory=lambda: Permit.query.all(), 
        get_label='PMT_type', 
        validators=[DataRequired()]
    )
