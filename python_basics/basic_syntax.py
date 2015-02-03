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
string_withbracket = ("""string with bracket and double quotes""")
string_withbracket_singlequote = ('sring with bracket and single quote')
print string_nobracket
print string_withbracket
print string_withbracket_singlequote
#print string_bracket
#print days_mixed_quotes
#print total
#print total1
