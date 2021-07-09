# Olga Redko

import nltk
import pickle

# PART A:
grammar1 = nltk.CFG.fromstring("""
        S -> NP VP | NP Aux VP 
        NP -> Det Adj N | Det Adj Adj N | N | Pro | Det N | NP CP | NP Conj NP | NP PP | N N 
        VP -> V PP | V NP | V NP PP | V NP NP | V AdjP | V | VP Conj VP | V NP CP | VP AdvP 
        PP -> P NP 
        CP -> Comp S 
        AdjP -> Adj | Adv Adj | AdjP Conj AdjP
        AdvP -> Adv Adv 
        Det -> 'the' | 'his' | 'her' 
        N -> 'bully' | 'kid' | 'school' | 'book' | 'sister' | 't' | 'Homer' | 'Marge' | 'friends' | 'work' | 'bar' | 'Lisa' | 'brother' | 'peanut' | 'butter' 
        V -> 'punched' | 'gave' | 'given' | 'are' | 'drank' | 'sang' | 'told' | 'liked' 
        P -> 'after' | 'to' | 'from' | 'in'  
        Adj -> 'big' | 'tiny' | 'nerdy' | 'poor' | 'happy' 
        Adv -> 'very' | 'much' 
        Pro -> 'he' | 'I' | 'him' | 'she' 
        Comp -> 'that' 
        Conj -> 'and' | 'but' 
        Aux -> 'had' 
    """)
# 2.
# a. start state = S
# b. Grammar with 71 productions (so, there are 71 CF rules)
# c. There are 45 lexical items
# d. There are 9 VP rules
# e. There are 8 V rules

print(grammar1)

print(grammar1.productions())

lexical_count = 0
VP_rule_count = 0
V_rule_count = 0

for r in grammar1.productions():
    if r.is_lexical():
        lexical_count += 1
    if r.lhs().symbol() == 'VP':
        VP_rule_count += 1
    if r.lhs().symbol() == 'V':
        V_rule_count += 1

print('Lexical item count: ', lexical_count)
print('VP rule count: ', VP_rule_count)
print('V rule count: ', V_rule_count)

# 3. Building a chart parser
parser = nltk.ChartParser(grammar1)

# 4. Parsing sentences s6-s11
s6 = 'the big bully punched the tiny nerdy kid after school'.split()
s7 = 'he gave the book to his sister'.split()
s8 = 'he gave the book that I had given him t to his sister'.split()
s9 = 'Homer and Marge are poor but very happy'.split()
s10 = 'Homer and his friends from work drank and sang in the bar'.split()
s11 = 'Lisa told her brother that she liked peanut butter very much'.split()

print('s6: ')
for t6 in parser.parse(s6):
    print(t6)
print('s7: ')
for t7 in parser.parse(s7):
    print(t7)
print('s8: ')
for t8 in parser.parse(s8):
    print(t8)
print('s9: ')
for t9 in parser.parse(s9):
    print(t9)
print('s10: ')
for t10 in parser.parse(s10):
    print(t10)
print('s11: ')
for t11 in parser.parse(s11):
    print(t11)

# PART B:

# 1.
print('''(s10): "Homer and his friends from work drank and sang in the bar"
 is ambiguous because it could be interpreted as
 "[Homer and his friends] from work..."
(S
  (NP
    (NP (NP (N Homer)) (Conj and) (NP (Det his) (N friends)))
    (PP (P from) (NP (N work))))
 ...
 or
 "Homer and [his friends from work]..."
 (S
   (NP
     (NP (N Homer))
     (Conj and)
     (NP (NP (Det his) (N friends)) (PP (P from) (NP (N work)))))
 ...''')

# 2.
s12 = 'Lisa and her friends told Marge that Homer punched the bully in the bar'.split()

print('s12: ')
for t12 in parser.parse(s12):
    print(t12)

# 3.
s13 = 'the big bully liked the tiny nerdy kid very much'.split()
print('s13: ')
for t13 in parser.parse(s13):
    print(t13)

# 4.
s1 = 'Marge will make a ham sandwich'.split()
s2 = 'will Marge make a ham sandwich'.split()
s3 = 'Homer ate the donut on the table'.split()

# a.
grammar2 = nltk.CFG.fromstring("""
        S -> NP Aux VP | Aux NP VP | NP VP
        NP -> N | Det NP | N N | Det N PP
        VP -> V NP NP | V NP 
        PP -> P NP
        Det -> 'a' | 'the'
        N -> 'Marge' | 'Homer' | 'ham' | 'sandwich' | 'donut' | 'table'
        V -> 'make' | 'ate' 
        P -> 'on'
        Aux -> 'will' 
    """)

print(grammar2)

print(grammar2.productions())
print(set(grammar2.productions()))

# b.
grammar3 = nltk.CFG.fromstring("""
        S -> Aux NP VP
        NP -> Det NP | Det N PP
        Det -> 'a'
        N -> 'ham' | 'sandwich' | 'donut' | 'table'
        V -> 'make' | 'ate' 
        P -> 'on'
        Aux -> 'will' 
    """)

more_rules = grammar3.productions()

# c.
grammar1.productions().extend(more_rules)

# d.
grammar1 = nltk.grammar.CFG(grammar1.start(), grammar1.productions())
print(grammar1)

# e.
parser = nltk.ChartParser(grammar1)

print('s1: ')
for t1 in parser.parse(s1):
    print(t1)

print('s2: ')
for t2 in parser.parse(s2):
    print(t2)

print('s3: ')
for t3 in parser.parse(s3):
    print(t3)

# 5.
s14 = 'will the big bully make the tiny nerdy kid a ham sandwich'.split()

print('s14: ')
for t14 in parser.parse(s14):
    print(t14)

print("I'm satisfied with the result.")

# 6.
pickle.dump(grammar1, open("ex7_grammar.pkl", "wb"))
grammar1 = pickle.load(open("ex7_grammar.pkl", "rb"))
print(grammar1)