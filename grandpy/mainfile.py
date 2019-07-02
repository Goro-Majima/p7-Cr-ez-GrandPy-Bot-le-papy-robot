from grandpy.classes import Parsing, Googlemap, Mediawiki, Answer
from random import randrange

def process_question(question):
    
    parsedquery = Parsing(question)
    keyword = parsedquery.returnkeyword()
    datagmap = Googlemap(keyword)
    #try to get address and coordinates"""
    try:
        location = datagmap.http_results()
        papytext = Answer.addressfound()
        diction = {'papyintro': papytext, 'address':location[2],\
            'latitude': location[0], 'longitude': location[1]}
        #try to get a story and link (tuple) from mediawiki with the keyword
        try:
            mediawikistory = Mediawiki(diction['latitude'], diction['longitude']).historytell()
            infowithstory = Answer.storyfound()
            diction = {'papyintro': papytext, 'address':location[2],\
            'latitude': location[0], 'longitude': location[1], 'introstory': infowithstory, 'story': mediawikistory[0], 'link': mediawikistory[1]}
        #return negative answer if no story to tell
        except IndexError:
            notokstory = Answer.nomediawiki()
            diction = {'papyintro': notokstory, 
                'address':location[2],\
                'latitude': location[0], 
                'longitude': location[1], 
                'introstory': '', 
                'story': '', 
                'link': ''
                }

    #return negative answer if index out of list or no data""" 
    except IndexError:
        nothingtotell = Answer.nothingfound()
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
            "introstory": diction['introstory'],
            "story": diction['story'] ,
            "url": diction['link']                   
            }
    return jsonfile

