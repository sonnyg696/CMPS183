# -*- coding: utf-8 -*-


db.define_table('restaurant',
                Field('name'),
                Field('city'),
                Field('zipcode'),
                Field('address'),
                Field('website'),
                Field('phone', widget=SQLFORM.widgets.text.widget),
                Field('hours', 'string', widget=SQLFORM.widgets.text.widget),
                Field('specials', 'string', widget=SQLFORM.widgets.text.widget),
                )

db.restaurant.phone.requires = IS_MATCH('^1?((-)\d{3}-?|\(\d{3}\))\d{3}-?\d{4}$', error_message="Not a valid phone number")
db.restaurant.zipcode.requires = IS_MATCH('^[0-9]{5}(-[0-9]{4})?$', error_message="Not a valid US Zipcode")
db.restaurant.id.readable = False
db.restaurant.hours.widget = lambda f,v: SQLFORM.widgets.string.widget(f, v, _placeholder='Tuesday-Thursday, 5:30pm-10:00pm')
db.restaurant.specials.widget = lambda f,v: SQLFORM.widgets.string.widget(f, v, _placeholder='$1 Margarita Pitchers')
db.restaurant.phone.widget = lambda f,v: SQLFORM.widgets.string.widget(f, v, _placeholder='(000)000-0000')
