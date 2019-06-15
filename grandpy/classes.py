import re
from grandpy.stopwords import *


class Parsing:
    """Parse user sentence into a keyword for an accurate research"""
    def __init__(self,question):
        self.question = question
        self.splittedquestion = []

    def returnkeyword(self):
        self.question = self.question.lower()
        self.question = self.question.replace("'",' ')
        self.question = self.question.split()
        for word in self.question:
            if word not in STOPWORDS:
                self.splittedquestion.append(word)
        self.splittedquestion = ' '.join(self.splittedquestion)
        return self.splittedquestion
# class Parser:
#     """ Class definition to parse the sentence from the webpage input. """

#     def __init__(self, sentence):
#         """ Initializer / Instance Attributes """
#         self.sentence = sentence

#     def parsing(self):
#         """ Parser """
#         # To put every words of the sentence in lowercase.
#         self.sentence = self.sentence.lower()
#         # To remove .!,; and ? from the sentence and transform it into a list of words.
#         self.sentence = re.sub(r"[.!,;?\']", " ", self.sentence).split()
#         # To remove the stopwords and .!,;' and ? from the sentence.
#         self.sentence = [x for x in self.sentence if x not in STOPWORDS]
#         # To convert the list to string.
#         self.sentence = ' '.join(self.sentence)
#         return self.sentence
