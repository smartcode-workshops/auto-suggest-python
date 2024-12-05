import sys
from trie import Trie

words = [
    "as", "astronaut", "asteroid", "are", "around",
    "cat", "cars", "cares", "careful", "carefully",
    "for", "follows", "forgot", "from", "front",
    "mellow", "mean", "money", "monday", "monster",
    "place", "plan", "planet", "planets", "plans",
    "the", "their", "they", "there", "towards"
]

dictionary = None

def initialize_trie(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

def search_word():
    while True:
        print("Enter a word to search for, or press Enter to exit.")
        input_word = input()
        if input_word == "":
            break
        '''
        if input_word is not None and dictionary.search(input_word):
            print(f'Found "{input_word}" in dictionary')
        else:
        '''
        print(f'Did not find "{input_word}" in dictionary')

def prefix_autocomplete():
    print_trie(dictionary)
    get_prefix_input()

def delete_word():
    print_trie(dictionary)
    while True:
        print("\nEnter a word to delete, or press Enter to exit.")
        input_word = input()
        if input_word == "":
            break
        '''
        if input_word is not None and dictionary.search(input_word):
            dictionary.delete(input_word)
            print(f'Deleted "{input_word}" from dictionary\n')
            print_trie(dictionary)
        
        else:
        '''
        print(f'Did not find "{input_word}" in dictionary')

def get_spelling_suggestions():
    print_trie(dictionary)
    print("\nEnter a word to get spelling suggestions for, or press Enter to exit.")
    input_word = input()
    if input_word is not None:
        similar_words = dictionary.get_spelling_suggestions(input_word)
        print(f'Spelling suggestions for "{input_word}":')
        if len(similar_words) == 0:
            print("No suggestions found.")
        else:
            for word in similar_words:
                print(word)

def run_all_exercises():
    print_trie(dictionary)
    #search_word()
    #prefix_autocomplete()
    #delete_word()
    #get_spelling_suggestions()

def get_prefix_input():
    print("\nEnter a prefix to search for, then press Tab to " +
          "cycle through search results. Press Enter to exit.")

    running = True
    prefix = ""
    sb = []
    words = None
    words_index = 0

    while running:
        input_key = sys.stdin.read(1)

        if input_key == ' ':
            print(' ', end='', flush=True)
            prefix = ""
            sb.append(' ')
            continue
        elif input_key == '\b' and len(sb) > 0:
            print('\b \b', end='', flush=True)
            sb.pop()
            prefix = ''.join(sb).split(' ')[-1]
        elif input_key == '\n':
            print()
            running = False
            continue
        elif input_key == '\t' and len(prefix) > 1:
            previous_word = ''.join(sb).split(' ')[-1]

            if words is not None:
                if previous_word != words[words_index - 1]:
                    words = dictionary.auto_suggest(prefix)
                    words_index = 0
            else:
                words = dictionary.auto_suggest(prefix)
                words_index = 0

            for i in range(len(prefix), len(previous_word)):
                print('\b \b', end='', flush=True)
                sb.pop()

            if len(words) > 0 and words_index < len(words):
                output = words[words_index]
                words_index += 1
                print(output[len(prefix):], end='', flush=True)
                sb.extend(output[len(prefix):])
            continue
        elif input_key != '\t':
            print(input_key, end='', flush=True)
            prefix += input_key
            sb.append(input_key)
            words = None
            words_index = 0

def print_trie(trie):
    print("The dictionary contains the following words:")
    words = trie.get_all_words()
    for word in words:
        print(f"{word}, ", end='')
    print()

if __name__ == "__main__":
    dictionary = initialize_trie(words)
    run_all_exercises()