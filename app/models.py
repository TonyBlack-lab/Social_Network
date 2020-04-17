from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login as login_form
from flask_login import UserMixin
# import random


class Regist(UserMixin, db.Model):
    regist_id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(64), index=True, unique=True)
    user_id_number = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    '''def conver_id(self, regist_id, user_id_number):
        if random.randint'''

    @staticmethod
    def load_from_login(mobile_number):
        return Regist.query.filter_by(mobile_number=mobile_number).first()

    def __repr__(self):
        return '<User {}>'.format(self.mobile_number)

@login_form.user_loader
def load_user(mobile_number):
    return Regist.query.get(mobile_number)

'''
class Gender(db.Model):
    gender_id = db.Column(db.Integer, primary_key=True)
    gender_login = db.relationship('Login', back_populates='login.login_gender')
    gender_user = db.relationship('User', back_populates='user.user_gender')

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

association_hobby_user = db.Table('hobby_user', db.Model.metadate,
    db.Column('hobby_id', db.Integer, db.ForeignKey('hobby.hobby_id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')))

association_massage_user = db.Table('massage_user', db.Model.metadate,
    db.Column('massage_id', db.Integer, db.ForeignKey('massage.message_id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')))

association_forum_user = db.Table('forum_user', db.Model.metadate,
    db.Column('forum_id', db.Integer, db.ForeignKey('forum.forum_id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')))

class Country(db.Model):
    country_id = db.Column(db.Integer, primary_key=True)
    country_city = db.relationship('City', secondary=association_country_city, back_populates='city.city_country')
    country_adress = db.relationship('Adress', secondary=association_adress, back_populates='adress.adress_country')

class City(db.Model):
    city_id = db.Column(db.Integer, primary_key=True, index=True)
    city_country = db.relationship('Country', secondary=association_country_city, back_populates='country.country_city')
    city_district = db.relationship('District', secondary=association_city_district,
                                    back_populates='district.district_city')
    city_adress = db.relationship('Adress', secondary=association_adress, back_populates='adress.adress_city')

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
    login_id = db.Column(db.Integer, db.ForeignKey('login.login_id'))
    user_login = db.relationship('Login', back_populates='login.login_user')
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.gender_id'))
    user_gender = db.relationship('Gender', back_populates='gender.gender_user')
    user_adress = db.relationship('Adress', secondary=association_adress_user, back_populations='adress.adress_user')
    date_of_birth = db.Column(db.String(64))
    zodiak_id = db.Column(db.Integer, db.ForeignKey('zodiak.zodiak_id'))
    user_zodiak = db.relationship('Zodiak', back_populates='zodiak.zodiak_user')
    user_hobby = db.relationship('Hobby', secondary=association_hobby_user, back_populates='hobby.hobby_user')
    user_massage = db.relationship('Massage', secondary=association_massage_user, back_populates='massage.massage_user')
    user_forum = db.relationship('Forum', secondary=association_forum_user, back_populates='forum.forum_user')
    user_gallery = db.relationship('Gallery', back_populates='gallery.gallery_user')
    relation_id = db.Column(db.Integer, db.ForeignKey('relation.relation_id'))
    user_relation = db.relationship('Relation', back_populates='relation.relation_user')
    rank_id = db.Column(db.Integer, db.ForeignKey('rank.rank_id'))
    user_rank = db.relationship('Rank', back_populates='rank.rank_user')

class Zodiak(db.Model):
    zodiak_id = db.Column(db.Integer, primary_key=True)
    zodiak_user = db.relationship('User', back_populates='user.user_zodiak')

class Hobby(db.Model):
    hobby_id = db.Column(db.Integer, primary_key=True)
    hobby_user = db.relationship('User', secondary=association_hobby_user, back_populates='user.user_hobby')

class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)
    message_user = db.relationship('User', secondary=association_massage_user, back_populate='user.user_massage')

class Forum(db.Model):
    forum_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)
    forum_user = db.relationship('User', secondary=association_forum_user, back_populates='user.user_forum')

class Gallery(db.Model):
    gallery_id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(1024), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    gallery_user = db.relationship('User', back_populates='user.user_gallery')

class Relation(db.Model):
    relation_id = db.Column(db.Integer, primary_key=True)
    relation_user = db.relationship('User', back_populates='user.user_relation')

class Rank(db.Model):
    rank_id = db.Column(db.Integer, primary_key=True)
    rank_user = db.relationship('User', back_populates='user.user_rank')

def __repr__(self):
    return '<User {}>'.format(self.rank)
'''