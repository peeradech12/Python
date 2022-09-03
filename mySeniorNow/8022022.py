import re 
#print(re.match('abc','abcdef'))
#word_regex = '\w+'
#print(re.match(word_regex,'hi there'))
#print(re.split('\s+','Split on spaces.'))
my_string = "Let's write RegEx! Won't that be fun? I sure think so. Can you find 4 sentences? Or perhaps, all 19 words?"
sentence_endings =r"[.?!]"
#print(re.split(sentence_endings,my_string))
capitallized_words = r"[A-Z]\w+"
#print(re.findall(capitallized_words,my_string))
spaces = r"\s+"
#print(re.split(spaces,my_string))
digits = r"\d"
#print(re.findall(digits,my_string))
