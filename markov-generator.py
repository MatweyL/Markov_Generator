from fileinput import filename
import random
import sys


def get_input_settings():
    filename = ""
    number_of_links = 0
    number_of_words = 0
    try:
        filename = sys.argv[1]
        number_of_links = int(sys.argv[2])
        number_of_words = int(sys.argv[3])
    except IndexError:
        print("lack of args")
    return [filename, number_of_links, number_of_words]

def get_corpus(filename):
    text = ""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().split()
    except IOError:
        print("No such corpus file")
    return text

def get_related_words(corpus, start_index, related_words_number):
    words = " ".join(corpus[start_index:start_index + related_words_number])
    return words

def make_markov_dict(corpus, related_words_number = 1):
    markov_dict = {}
    for i in range(len(corpus) - 2*related_words_number + 1):#make word pairs
        words_key = get_related_words(corpus, i, related_words_number)
        words_value = get_related_words(corpus, i + related_words_number, related_words_number)
        if words_key in markov_dict:
            markov_dict[words_key].append(words_value)
        else:
            markov_dict[words_key] = [words_value]
    return markov_dict

def generate_text(markov_dict, words_number):
    generated_text = ""
    upper_words_list = []
    for key in markov_dict.keys():
        if key.istitle():
            upper_words_list.append(key)
    current_word = upper_words_list[int(random.random()*len(upper_words_list))]
    generated_text = current_word + " "
    new_word = ""
    i = 0
    while not(i >= words_number and current_word[-1] == '.'):
        new_word = markov_dict[current_word][int(random.random()*len(markov_dict[current_word]))]
        generated_text += new_word + " "
        current_word = new_word
        i += 1
    return generated_text

def main():
    settings = get_input_settings()
    filename = settings[0]
    number_of_links = settings[1]
    number_of_words = settings[2]
    corpus = get_corpus(filename)#get source text for generating
    if (corpus != ""):
        markov_dict = make_markov_dict(corpus, number_of_links)
        generated_text = generate_text(markov_dict, number_of_words)
        print(generated_text)

if __name__ == "__main__":
    main()
