    from flask.ext.wtf import Form
    from wtforms import TextField, IntegerField, DateField
    from wtforms.validators import Required, Optional, FileField, file_required,

  class ProfileForm(Form):
      #profile_photo =FileField('Profile Image')
	userID =IntegerField('ID:', [Required()])
	firstName = TextField('First Name:', [Required()])
	lastName = TextdField('Last Name:', [Required()])
	sex = SelectField('Sex', choices=[('M','Male'),('F''Female')] default = 'M', [Required()])
	age = IntegerField('Age:', [Required()])
