# The goal of this project was to write a function that translates any given string into "ubby dubby".
# The function ubby_dubby accomplishes this. The main function makes a copy of a file and 
# ubby-dubby-izes the contents
# The file editing maintains newlines and maintains spacing correctly.
# Written 2021-12-09 by AN

vowels = ['a','e','i','o','u','y']

# for the purpose of this language, consider any combo of VVVCCCC that ends just before another V as a syllable
def syllables(input_word):
    ''' Syllables finds and returns a list of syllables in the word given. It uses logic that works for 
        the ubby-dubby language: a "syllable" ends with the last consonant before a vowel, or ends at the
        end of a word'''
    output_list = []
    syllable_builder = ''
    in_consonant = False
    word_being_analyzed = True
    index = 0
    
    while word_being_analyzed:
        
        if (input_word[index].lower() not in vowels or input_word[index].lower() == 'y') and in_consonant == False:
            # ex starting a word with a consonant
            # or in a syllable that has only been vowels so far
            syllable_builder += input_word[index]
            in_consonant = True
            
        elif input_word[index].lower() in vowels and in_consonant == True:
            # starting new syllable
            # save old one and start new syllable
            output_list.append(syllable_builder)
            syllable_builder = input_word[index]
            in_consonant = False
        
        elif input_word[index].lower() not in vowels and in_consonant == True:
            # in a number of consonants in a row within a syllable
            syllable_builder += input_word[index]
            
        else:
            # case where input_word[index] in vowels and in_consonant == False
            # still in vowel-only part of syllable
            syllable_builder += input_word[index]
        
        if index + 1 == len(input_word):
            word_being_analyzed = False
        else:
            index += 1
    
    output_list.append(syllable_builder)
            
    return output_list   
    
def ubby_dubby(input_string):
    ''' Function that translates input_string into ubby-dubby-ized version of input string, and returns
        translated version. Maintains newlines and spacing. If a word starts with "y" it considers that
        a consonant.
        
        More could be done to this function to add a better understanding of some minutiae of the english
        language. Current issues are that it handles a silent "e" at the end of a word as if it is a syllable,
        and syllables that come from multiple vowels in a row such as radio are not handled'''
    
    word_list = input_string.split(' ')
    output_word_list = []
    starts_with_y = False
    
    for word in word_list:
        output_word = ''
        if word[0].lower() == 'y':
            starts_with_y = True
        
        for syllable in syllables(word):
            if syllable[0].lower() in vowels:
                if starts_with_y == True:
                    starts_with_y = False
                else:
                    output_word += 'ubb-'
                
                output_word += syllable
            else:
                output_word += syllable
        
        output_word_list.append(output_word)
        
        # join with space except when the final character of the word is a newline character
        output_string = ''
        for word in output_word_list:
            output_string += word
            if word[-1] != '\n':
                output_string += ' '
            
    return output_string

def run_program():
    ''' Main program. Prompts user for a file to translate, and then outputs a translated file.
        Re-prompts user for input while a valid filename has not been given.'''
    
    acceptable_input = False
    
    while acceptable_input == False:
        try:
            # test that this error-checking works
            name = input("Please enter a filename for us to translate: ")
            f = open(name,'r',newline='')
        except IOError as e:
            print(e.strerror)
        else:
            acceptable_input = True
    
    text = f.read()
    
    # add spaces after new lines so that ubby_dubby function correctly separates this into words
    # instead of keeping last word of previous line and first word of next line together as a word
    mod_text = text.replace('\n\n','\n\n ')
    
    f.close()
    
    # detect filename extension location and make new filename based on this
    period_index = len(name) - name[::-1].find('.') - 1
    new_filename = name[0:period_index] + " in ubby-dubby.txt"
    
    f2 = open(new_filename,'w',encoding='utf-8')
    f2.write(ubby_dubby(mod_text))
    f2.close()
    
    print("Successfully output new file!")
        

if __name__ == "__main__":
    run_program()
    