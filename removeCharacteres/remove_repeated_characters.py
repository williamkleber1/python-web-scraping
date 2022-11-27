import re

def remove_repeat(old_word: str): 
    """using regex to remove consecutive duplicate characters"""
    repeat_pattern = re.compile(r'(.)\1+') 
    match_substitution = r'\1' 
    new_word = repeat_pattern.sub(match_substitution,old_word)
    return new_word



# Defining main function
def main():
    words = []
    while True:
        try:
            words.append( str(input()))
            
        except EOFError:
            new_words = []
            for word in words:
                new_words.append(remove_repeat(word))
            print("Result:",new_words)
            break



# __name__
if __name__=="__main__":
	main()
