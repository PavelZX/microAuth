
from config import get_config
from db_client import db
from models.base import Base
from models.users import User
from utils import encrypt_pass

appConfig = get_config()


def init_db():
    try:
        print("Creating tables and default admin account \n")

        Base.metadata.create_all(bind=db.engine)
        admin = User(emailAddress=appConfig.ADMIN_EMAIL,
                     password=encrypt_pass(appConfig.ADMIN_PASSWORD), userRole="ADMIN", isValidated=True)

        db.connect()
        db.session.add(admin)
        db.session.commit()
        db.close()

        print("---------")
        print("Database succesfully initialized")
        print("---------")

    except Exception as e:
        print("---------")
        print(e)
        print("---------")