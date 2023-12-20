# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.


class text_conv:
    def __init__(self,text):
        self.text = text

    def frequency(self, word):
        return print(f'{word}')
            

text1 = text_conv('A good book would sometimes cost as much as a good house')

print(text1.frequency('good'))


# f = open('secrets.txt','w+')

# f = open('secrets.txt','a+')
# f.write('\nThis is text being appended to test.txt')
# f.write('\nAnd another line here.')
# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.