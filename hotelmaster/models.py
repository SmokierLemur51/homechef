from hotelmaster import db




class RoomType(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	roomtype = db.Column(db.String(50), unique=True)