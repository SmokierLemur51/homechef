from flask import render_template

from hotelmaster import app, db
from hotelmaster.forms import public_forms


@app.route("/")
def public_index():
	title = "Public index"
	return render_template("public/index_public.html", title=title)


@app.route("/amenities")
def public_amenities():
	title = "Amenities"
	return render_template("public/amenities_public.html", title=title)


@app.route("/about")
def public_about():
	title = "About"
	return render_template("public/about_public.html", title=title)


@app.route("/contact")
def public_contact():
	title = "Contact"
	return render_template("public/contact_public.html", title=title)
