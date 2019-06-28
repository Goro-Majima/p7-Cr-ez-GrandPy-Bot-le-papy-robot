from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

# @app.route('/')
# def ajax(query):

    # query = input("entre ton lieu: ")
    # parsedquery = Parsing(query)
    # keyword = parsedquery.returnkeyword()
    # datagmap = Googlemap(keyword)
    # #try to get address and coordinates"""
    # try:
    #     location = datagmap.http_results()
    #     diction = {'papyintro': "Bien sûr mon poussin! La voici: ", 'address':location[2],\
    #         'latitude': location[0], 'longitude': location[1]}
    #     infowithoutstory = diction['papyintro'] + diction['address']
        
    #     #try to get a story an,d link (tuple) from mediawiki with the keyword
    #     try:
    #         mediawikistory = Mediawiki(diction['latitude'], diction['longitude']).historytell()
    #         diction = {'papyintro': 'Voici le lieu que tu cherches:', 'address':location[0],\
    #         'latitude': location[1], 'longitude': location[2], 'story': mediawikistory}
    #         infowithstory = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?" + diction['story'][0]# diction['story'] is a tuple
    #         link = "Si tu veux en savoir plus clique sur ce lien: " + diction['story'][1]
    #         print(infowithoutstory)
    #         print(infowithstory)
    #         print("")
    #         print("Si tu veux en savoir plus clique sur ce lien: " + diction['story'][1])
    #     #return negative answer if no story to tell
    #     except IndexError:
    #         print("Désolé mon petit mais j'ai tout oublié à propos de ce lieu...")
    # #return negative answer if index out of list or no data""" 
    # except IndexError:
    #     print("Désolé mon petit mais je n'ai pas trouvé ce que tu me demandes =(")

if __name__ == "__main__":
    app.run(debug=True, port=5000)