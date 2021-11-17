# sentences(0), dictionaries, forvo, images (1)

import webbrowser, time

#-------Global Variables-------

# Links for the searches
links = [
    'https://forvo.com/word/', # forvo
    'https://www.google.com/search?tbm=isch&q=', # google images
    'https://context.reverso.net/translation/english-portuguese/', # reverso-EN
    'https://context.reverso.net/translation/french-english/', # reverso-FR
    'https://context.reverso.net/translation/spanish-english/', #reverto-ES
    'https://dictionary.cambridge.org/pt/dicionario/ingles/', # english cambridge
    'https://www.oxfordlearnersdictionaries.com/definition/english/', # english oxford
    'https://www.wordreference.com/fren/', # bilingual french
    'https://es.thefreedictionary.com/' # monolingual spanish
    #url for normal google searches is "http://www.google.com/search?q="
]

# User input selects the language for the searches
def select_language():
    global language
    all_languages =['en', 'fr', 'es']
    while True:
        language = input("What's the language? ").lower()

        # validates the entries and asks for the words to be searched
        if language in all_languages:            
            global words            
            words = input('What words? ').strip().split(', ')
            print(f'-------Total of words: {len(words)} -------\n')
            search_everything()
        else:
            print('Sorry, language not available')


#makes sure every word is searched
def search_everything():
    for i in range(len(words)):   
        id_pa = general_check_and_others(language, words[i])
        other_links(*id_pa)
        time.sleep(1.5)

        if (i+1)%4 == 0:
            words_left = (len(words)- 1) - i
            if words_left != 0:
                print(f'Number of words left: {words_left}')
                input('Ready for the next batch?')
                print('\n')
        
    select_language()   


#checks if example sentences or images are needed and searches them...
#and calls other_links()
def general_check_and_others(idioma, palavra):
    options1 = {'en': 2, 'fr': 3, 'es': 4}
    symbols = ['0', '1']

    if '_' in palavra:
        palavra = palavra.split('_')
        palavra = ' '.join(palavra)
    
    for number in symbols:
        #both setences and images
        if palavra[-2:] in ['01', '10']:
            palavra = palavra.replace(palavra[-2:], '') #removes the symbols
            webbrowser.open(links[1] + palavra) #images
            time.sleep(0.4)
            webbrowser.open(links[options1[idioma]] + palavra) #sentences
            break
        
        #either sentences or images
        elif palavra[-1] == number:
            palavra = palavra.replace(number, '') #removes the number

            if number == '0':
                webbrowser.open(links[options1[idioma]] + palavra) #sentences
            else:
                webbrowser.open(links[1] + palavra) #images

##    other_links(idioma, palavra)
    time.sleep(0.65)
    return idioma, palavra

# searches the word's audio and definition
def other_links(idioma, palavra):
    options2 = {'en': [6, 5], 'fr': [7], 'es': [8]}

    for option in options2[idioma]:
        webbrowser.open(links[option] + palavra) #dictionaries
        time.sleep(1)
        
    time.sleep(0.83)
    webbrowser.open(links[0] + palavra + f'/#{idioma}') #forvo


#starts the script
if __name__ == '__main__':
    select_language()
