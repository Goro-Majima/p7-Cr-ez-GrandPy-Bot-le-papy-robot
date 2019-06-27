from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

# @app.route('/')
# def ajax():

#     query = input("Entre ton lieu: ")
#     parsedquery = Parsing(query)
#     keyword = parsedquery.returnkeyword()
#     datagmap = Googlemap(keyword)
#     #try to get address and coordinates"""
#     try:
#         location = datagmap.http_results()
#         diction = {'papyintro': 'Voici le lieu que tu cherches: ', 'address':location[0],\
#             'latitude': location[1], 'longitude': location[2]}
#         infowithoutstory = diction['papyintro'] + diction['address'] + ", ses coordonnées gps: ", \
#         diction['latitude'], diction['longitude']
#         #try to get a story an,d link (tuple) from mediawiki with the keyword
#         try:
#             mediawikistory = Mediawiki(diction['latitude'], diction['longitude']).historytell()
#             diction = {'papyintro': 'Voici le lieu que tu cherches:', 'address':location[0],\
#             'latitude': location[1], 'longitude': location[2], 'story': mediawikistory}
#             infowithstory = "J'ai une belle histoire à raconter sur ce lieu: " + diction['story'][0]# diction['story'] is a tuple
#             print(infowithstory)
#             print("")
#             print("Si tu veux en savoir plus clique sur ce lien: " + diction['story'][1])
#         #return negative answer if no story to tell
#         except KeyError:
#             print("Désolé mon petit mais je ne me souviens plus de l'histoire de ce lieu mais j'ai ses coordonnées" + infowithoutstory)
#     #return negative answer if index out of list or no data""" 
#     except IndexError:
#         print("Désolé mon petit mais je n'ai pas trouvé ce que tu me demandes =(")

if __name__ == "__main__":
    app.run(debug=True, port=5000)