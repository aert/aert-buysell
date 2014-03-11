# coding=utf-8
from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object("bee3.config")


@app.route('/', methods=['GET', 'POST'])
def index():
    articles = [
        {"title": u"Porte caisse facom", "price": "30", "desc": u"Strasbourg / Bas-Rhin"},
        {"title": u"Monnaies: Médailles attribuées", "price": "10", "desc": u"Lyon / Rhône"},
        {"title": u"Golf 4 GTI TDI 110 cuir beige distri neuve carnet", "price": "4 000", "desc": u"Shiltigheim / Bas-Rhin"},
        {"title": u"Canaper 2 place +fauteuil on peut ouvrir les bas", "price": "300", "desc": u"Strasbourg / Bas-Rhin"},
        {"title": u"Demain est un autre jour LARRY COLLINS", "price": " 5", "desc": u"Strasbourg / Bas-Rhin"},
        {"title": u"Xbox one + FIFA 14, garantie 3 ans + live 1 an", "price": "500", u"desc": u"Haguenau / Bas-Rhin"},
        {"title": u"Verrines jetables forme tube \"FIFINE\"", "price": "1", "desc": u"Strasbourg / Bas-Rhin"},
        {"title": u"Anciens livres brochés", "price": "", "desc": u"Strasbourg / Bas-Rhin"},
        {"title": u"Moteur 350 rdlc 31k", "price": "800", "desc": u"Strasbourg / Bas-Rhin"},
    ]
    return render_template("frontend/index.html",
                           articles=articles)


