import os
import sys
import tty
import termios
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
    print_trie(dictionary)
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
    search_word()
    prefix_autocomplete()
    delete_word()
    get_spelling_suggestions()

def get_prefix_input():
    print("\nEnter a prefix to search for, then press Tab to cycle through search results. Press Enter to exit.")
    
    # Initialize variables
    running = True
    prefix = ""
    text_buffer = []
    words = None
    words_index = 0
    
    # Get original terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
    try:
        # Set terminal to raw mode
        tty.setraw(fd)
        
        while running:
            # Read single character
            char = sys.stdin.read(1)
            
            # Handle different key inputs
            if ord(char) == 32:  # Space
                sys.stdout.write(' ')
                sys.stdout.flush()
                prefix = ""
                text_buffer.append(' ')
                
            elif ord(char) == 127:  # Backspace
                if len(text_buffer) > 0:
                    # Move cursor back and clear character
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
                    text_buffer.pop()
                    # Update prefix to last word
                    prefix = ''.join(text_buffer).split()[-1] if text_buffer else ""
                    
            elif ord(char) == 13:  # Enter
                sys.stdout.write('\n')
                sys.stdout.flush()
                running = False
                
            elif ord(char) == 9:  # Tab
                if len(prefix) > 1:
                    previous_word = ''.join(text_buffer).split()[-1]
                    
                    # Get suggestions if needed
                    if words is not None:
                        if previous_word != words[words_index - 1]:
                            words = dictionary.auto_suggest(prefix)  # Assuming this exists
                            words_index = 0
                    else:
                        words = dictionary.auto_suggest(prefix)  # Assuming this exists
                        words_index = 0
                    
                    # Clear previous completion
                    for _ in range(len(previous_word) - len(prefix)):
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                        text_buffer.pop()
                    
                    # Write new completion
                    if words and words_index < len(words):
                        output = words[words_index]
                        completion = output[len(prefix):]
                        sys.stdout.write(completion)
                        sys.stdout.flush()
                        text_buffer.extend(completion)
                        words_index += 1
                        
            elif ord(char) != 9:  # Not Tab
                sys.stdout.write(char)
                sys.stdout.flush()
                prefix += char
                text_buffer.append(char)
                words = None
                words_index = 0
                
    finally:
        # Restore terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return ''.join(text_buffer)

def print_trie(trie):
    print("The dictionary contains the following words:")
    words = trie.get_all_words()
    for word in words:
        print(f"{word}, ", end='')
    print()

if __name__ == "__main__":
    dictionary = initialize_trie(words)
    # search_word()
    # prefix_autocomplete()
    # delete_word()
    # get_spelling_suggestions()