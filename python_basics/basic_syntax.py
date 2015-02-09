import sys
item1 = "one"
item2 = "two"
# \ put of the continuation of the statements
total = item1 +\
        item2+item1+item2+item1+\
        item2+item1 
total1 =[item1,item2,'added',"additioned"]
#double quotes and single quotes in python program are same
days_mixed_quotes =  ('monday',"tuesday",'wednesday',item1,total1)
string_nobracket = "string without bracket"
#triple quotes max possible only,program doesnt work with python3.4 as brackets 
#-are required
string_withbracket = ("""\nstring with bracket and double quotes""")
string_withbracket_singlequote = ('sring with bracket and single quote')
print string_nobracket
print string_withbracket
print string_withbracket_singlequote
#print string_bracket
#print days_mixed_quotes
#print total
#print total1
word_or = '\nword'
word = 'wo\
r\nd'
sentence_or = "this is a sente\nnce"#cannot simply enter to second line in case of#double or single quotes,but in case of tripe quotes(max no of quotes)we can
sentence = "this is a \
sentence"
paragraph = """this is a\n 
paragraph"""
print word
print word_or
print sentence
print sentence_or
print paragraph
################################################
raw_input("\n\n press any key to exit\n")
#multiple stmts in single line,put semicolon
x = 'foo';sys.stdout.write(x + '\n');print x + '\n'
#header line and suite
if 0:
#suite
 print 'if'
elif -1:#treats as positive value like c
 print 'elif'
elif 10:
 print 'elif 2'
else:
 print'else'

