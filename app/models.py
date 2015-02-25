from app import db

    class User(db.Model):
        __tablename__ = 'users_user'
        userid = db.Column(db.Integer,nullable = False, primary_key=True)
	userName = db.Column(db.String(50), Unique=True)
	img = db.Column(db.LargeBinary)
	profiledate=db.Column(db.DateTime)
        fname = db.Column(db.String(50), unique=True)
        lname = db.Column(db.String(50), unique=True)
        sex=db.Column(db.String(10))
	age = db.Column(db.Integer)
	


	def __init__(self,username, img, profileDate,fname, lname,sex,age):
	   self.username=username 
	   self.img = img
	   self.profileDate=profileDate
	   self.fname = fname
           self.lname = lname
           self.sex = sex
           self.age = age
           

        def __repr__(self):
	    return '<User %r>' %(self.username)
