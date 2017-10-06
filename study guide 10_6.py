"""1. Write a function that takes in a list of letters and 
returns the unique letters from that list in a set."""

def unique_letters (L):
    result = set()
    for i in L:
        result.add(i)

    return result 

print unique_letters(['a', 'b', 'c', 'c', 'd', 'e', 'e', 'e', 'a'])


"""2. Write a function that takes in any word and checks if it is the name of a
character in Harry Potter. The function should return a Boolean."""

HARRY_POTTER_CHARACTERS = ['Hermione Granger', 'Harry Potter', 'Ron Weasley', 
'Neville Longbottom', 'Professor Snape', 'Professor Dumbledore', 'Sirius Black']

def validate_harry_potter_character (word):
    return word in HARRY_POTTER_CHARACTERS

print validate_harry_potter_character('Hermione Granger')
print validate_harry_potter_character('Rabbit Angstrom')


"""3. Write a function that congratulates someone with varying levels of 
ferocity."""

def congratulate (name, num_exclamation):
    print "Congratulations,", name, ('!'*num_exclamation)

congratulate('Ginny', 25)

"""4. Write a function that inputs an integer and prints out every number from 0
to that integer, but not including the integer itself."""

def int_printer (n):
    for num in range(n):
        print num

int_printer(6)

"""5. Movie review exercise."""

def analyze_sentiment(review):
    """Takes a movie review and returns overall neg/pos sentiment as a float.
    """

    positive_words = {'great', 'funny', 'uplifting', 'hilarious', 'cool'}
    negative_words = {'sad', 'stupid', 'disgusting', 'horrible', 'boring'}

    review_tokens = set(review.split(' '))

    num_positive = len(positive_words & review_tokens) # num of overlapping with positive
    num_negative = -len(negative_words & review_tokens) # num of overlapping with negative

    pos_ratio = float(num_positive)/len(positive_words)
    neg_ratio = float(num_negative)/len(negative_words)

    return pos_ratio + neg_ratio



def generate_review_message (movie_review):
