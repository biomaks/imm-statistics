__author__ = 'erik'
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_principal import Principal, Permission, RoleNeed
from flask_admin import Admin
from flask_mail import Mail

from app.views.user_page_view import user_page


app = Flask(__name__, static_folder='static')
app.config.from_object('config')
app.register_blueprint(user_page)

principal = Principal(app)
admin_permission = Permission(RoleNeed('admin'))

mail = Mail(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from views import views

from app.views.admin_view import UserSettingsView, RoleSettingsView, UserDataSettingsView

admin = Admin(app, name='Admin', base_template='admin/my_admin.jinja2.html')
admin.add_view(UserSettingsView(db.session))
admin.add_view(RoleSettingsView(db.session))
admin.add_view(UserDataSettingsView(db.session))


