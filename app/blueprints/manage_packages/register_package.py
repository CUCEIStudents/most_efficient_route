from flask import render_template, flash, redirect, url_for
from flask.views import MethodView

from app.models import User, Status, Permit
from app.blueprints.manage_users.set_user_info_form import SetUserInfoForm
from app.extensions.auth import require, has_permit_type
from app.extensions.database import db


class RegisterUserView(MethodView):
    @require(lambda: has_permit_type("Administrador"))
    def get(self):
        form = SetUserInfoForm()
        return render_template(
            "manage_users/set_user_info_form.html",
            form=form,
            url=url_for("manage_users.register_package"),
        )

    def post(self):
        form = SetUserInfoForm()

        if form.validate_on_submit():
            existing_user = User.query.filter_by(USR_email=form.USR_email.data).first()
            if existing_user:
                flash("¡El correo electrónico ya está registrado!", "error")
            else:
                newUser = User(
                    USR_email=form.USR_email.data,
                    plain_password=form.plain_password.data,
                    USR_name=form.USR_name.data,
                    USR_last_name=form.USR_last_name.data,
                    USR_telephone=form.USR_telephone.data,
                    USR_address=form.USR_address.data,
                    USR_PER_permitId=form.permit.data.PMT_permitId,
                    USR_ST_statusId=form.status.data.ST_statusId,
                )
                db.session.add(newUser)
                db.session.commit()
                flash("¡Usuario registrado exitosamente!", "success")
                return redirect(url_for("manage_users.manage_users"))

        status_choices = [
            (status.ST_statusId, status.ST_value)
            for status in Status.query.filter_by(ST_status_type=1).all()
        ]
        permit_choices = [
            (permit.PMT_permitId, permit.PMT_type) for permit in Permit.query.all()
        ]

        return render_template(
            "manage_users/set_user_info.html",
            title="Registrar nuevo usuario",
            form=form,
            status_choices=status_choices,
            permit_choices=permit_choices,
        )