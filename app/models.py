from app import db

class Login(db.Model):
    login_id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    adress_id = db.Column(db.Integer, db.ForeignKey('adress.adress_id'))
    login_adress = db.relationship('Adress', back_populates='adress.adress_login')
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.gender_id'))
    login_gender = db.relationship('Gender', back_populates='gender.gender_login')

class Gender(db.Model):
    gender_id = db.Column(db.Integer, primary_key=True)
    gender_login = db.relationship('Login', back_populates='login.login_gender')
    # name =

association_country_city = db.Table('country_city', db.Model.metadata,
    db.Column('country_id', db.Integer, db.ForeignKey('country.country_id'),
    db.Column('city_id', db.Integer, db.ForeignKey('city.city_id'))))

association_city_district = db.Table('city_district', db.Model.metadata,
    db.Column('city_id', db.Integer, db.ForeignKey('city.city_id'),
    db.Column('district_id', db.Integer, db.ForeignKey('district.district_id'))))

association_adress = db.Table('adress', db.Model.metadata,
    db.Column('country_id', db.Integer, db.ForeignKey('country.country_id')),
    db.Column('city_id', db.Integer, db.ForeignKey('city.city_id')),
    db.Column('district_id', db.Integer, db.ForeignKey('district.district_id')))

association_adress_user = db.Table('adress_user', db.Model.metadata,
    db.Column('adress_id', db.Integer, db.ForeignKey('adress.adress_id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')))

class Country(db.Model):
    country_id = db.Column(db.Integer, primary_key=True)
    country_city = db.relationship('City', secondary=association_country_city, back_populates='city.city_country')
    country_adress = db.relationship('Adress', secondary=association_adress, back_populates='adress.adress_country')
    # name =

class City(db.Model):
    city_id = db.Column(db.Integer, primary_key=True, index=True)
    city_country = db.relationship('Country', secondary=association_country_city, back_populates='country.country_city')
    city_district = db.relationship('District', secondary=association_city_district,
                                    back_populates='district.district_city')
    city_adress = db.relationship('Adress', secondary=association_adress, back_populates='adress.adress_city')
    # name =

class District(db.Model):
    district_id = db.Column(db.Integer, primary_key=True)
    district_city = db. relationship('City', secondary=association_city_district, back_populates='city.city_district')
    district_adress = db.relationship('Adress', secondary=association_adress, back_populates='adress.adress_district')

class Adress(db.Model):
    adress_id = db.Column(db.Integer, primary_key=True)
    adress_country = db.relationship('Country', secondary=association_adress, back_populates='country.country_adress')
    adress_city = db.relationship('City', secondary=association_adress, back_populates='city.city_adress')
    adress_district = db.relationship('District', secondary=association_adress,
                                      back_populates='district.district_adress')
    adress_login = db.relationship('Login', back_populates='login.login_adress')
    adress_user = db.relationship('User', secondary=association_adress_user, back_populations='user.user_adress')

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    date_of_birth = db.Column(db.String(64))
    user_adress = db.relationship('Adress', secondary=association_adress_user, back_populations='adress.adress_user')
    avatar_id = db.Column(db.String(128), db.ForeignKey("user_photo.avatar_id"))
    user_gallery = db.Column(db.String(128), db.ForeignKey("gallery_data.user_gallery"))
    relationship = db.Column(db.String(64))
    self_status = db.Column(db.String(128))
    hobby_id = db.relationship('User_Hobby')
    score = db.Column(db.String(64))
    # user_id = db.Column(db.Integer, foreign_key=True)

class Zodiak_Sign(db.Model):
    zodiak_id = db.Column(db.Integer, primary_key=True)
    # from =
    # to =

class User_Photo(db.Model):
    avatar_id = db.Column(db.String(128), primary_key=True, unique=True)
    # path =

class Gallery_Data(db.Model):
    user_gallery = db.Column(db.String(128), primary_key=True, unique=True)
    # path =

class User_Hobby(db.Model):
    hobby_id = db.Column(db.String(128), db.ForeignKey("user_profile.hobby_id"), primary_key=True, index=True)
    # name =

class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)

class Chat(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey("message.message_id"))
    text = db.Column(db.String(1024), nullable=False)


def __repr__(self):
    return '<User {}>'.format(self.username)

