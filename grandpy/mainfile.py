from grandpy.classes import Parsing, Googlemap, Mediawiki

def process_question(question):
    
    parsedquery = Parsing(question)
    keyword = parsedquery.returnkeyword()
    datagmap = Googlemap(keyword)
    #try to get address and coordinates"""
    try:
        location = datagmap.http_results()
        diction = {'papyintro': "Bien sûr mon poussin! La voici: ", 'address':location[2],\
            'latitude': location[0], 'longitude': location[1]}
        #try to get a story and link (tuple) from mediawiki with the keyword
        try:
            mediawikistory = Mediawiki(diction['latitude'], diction['longitude']).historytell()
            infowithstory = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? "
            okstory = "Bien sûr mon poussin! La voici: "
            diction = {'papyintro': okstory, 'address':location[2],\
            'latitude': location[0], 'longitude': location[1], 'introstory': infowithstory, 'story': mediawikistory[0], 'link': mediawikistory[1]}
        #return negative answer if no story to tell
        except IndexError:
            notokstory = "Désolé mon petit mais j'ai tout oublié à propos de ce lieu..."
            diction = {'papyintro': notokstory, 'address':location[2],\
            'latitude': location[0], 'longitude': location[1], 'introstory': '', 'story': '', 'link': ''}

    #return negative answer if index out of list or no data""" 
    except IndexError:
        nothingtotell = "Désolé mon petit mais je n'ai pas trouvé ce que tu me demandes =("
        diction = { 'papyintro': nothingtotell, 
                    'address':'',
                    'latitude': '', 
                    'longitude': '', 
                    'introstory': '', 
                    'story': '', 
                    'link': ''}
    jsonfile = {"papyanswer": diction['papyintro'],
            "address": diction['address'], 
            "gps":{'lat': diction['latitude'],
                'lng': diction['longitude']},
            "story": diction['story'] ,
            "url": diction['link']                   
            }
    return jsonfile

