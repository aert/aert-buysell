# coding=utf-8
from flask import Flask, render_template
from hamlish_jinja import HamlishExtension


app = Flask(__name__)
app.config.from_object("bee3.config")
app.jinja_env.add_extension(HamlishExtension)
app.jinja_env.hamlish_file_extensions = ('.haml', )
app.jinja_env.hamlish_enable_div_shortcut = True


@app.route('/', methods=['GET', 'POST'])
def index():
    articles = [
        {"title": u"Porte caisse facom", "price": "30", "desc": u"Strasbourg"},
        {"title": u"Monnaies: Médailles attribuées", "price": "10", "desc": u"Lyon"},
        {"title": u"Golf 4 GTI TDI 110 cuir beige distri neuve carnet", "price": "4 000", "desc": u"Shiltigheim"},
        {"title": u"Canaper 2 place +fauteuil on peut ouvrir les bas", "price": "300", "desc": u"Strasbourg"},
        {"title": u"Demain est un autre jour LARRY COLLINS", "price": " 5", "desc": u"Strasbourg"},
        {"title": u"Xbox one + FIFA 14, garantie 3 ans + live 1 an", "price": "500", u"desc": u"Haguenau"},
        {"title": u"Verrines jetables forme tube \"FIFINE\"", "price": "1", "desc": u"Strasbourg"},
        {"title": u"Anciens livres brochés", "price": "", "desc": u"Strasbourg"},
        {"title": u"Montre disque vinyl", "price": "30", "desc": u"Kingersheim"},
        {"title": u"Moteur 350 rdlc 31k", "price": "800", "desc": u"Strasbourg"},
        {"title": u"Robe gala - mariage originale moderne dentelle", "price": "130", "desc": u"68720"},
        {"title": u"Table ronde et chaises en fer forgé", "price": "50", "desc": u"Mutzig"},
        {"title": u"Livre DORA", "price": "15", "desc": u"Kingersheim"},
        {"title": u"COUSSINS et TABLEAUX (Christelle)", "price": "5", "desc": u"Ungersheim"},
        {"title": u"Machine à café tassimo", "price": "40", "desc": u"Strasbourg"},
        {"title": u"Sac randonnée", "price": "40", "desc": u"Schweighouse-sur-Moder"},
    ]
    return render_template("frontend/index.haml",
                           articles=articles)


@app.route('/article')
def article():
    desc = """
    <p><br/>
    Auto verkeerd in goede staat. Zit netjes in de lak, bekleding is op een klein gat na helemaal intact.
    <br/>
    Auto heeft altijd netjes bij ons binnen gestaan. De auto heeft een elektrisch bedienbaar dak en er zit airco op. en staat op mooie bbs velgen met nog zo goed als nieuwe Bridgestone banden.
    <br/><br/>
    Kortom een volledig rijk uitgevoerde Golf Cabrio uit het bouwjaar 2000 voor een scherpe prijs.
    </p>
    """

    item = {"title": u"Golf 4 GTI TDI 110 cuir beige distri neuve carnet",
            "price": "4000", "city": u"Strasbourg",
            "desc": desc}
    return render_template("frontend/articles_detail.haml",
                           item=item)


@app.route('/article-new')
def article_add():
    return render_template("frontend/articles_add.haml")