Python 3.6.8 (default, Oct  7 2019, 12:59:55)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.12.0 -- An enhanced Interactive Python. Type '?' for help.
PyDev console: using IPython 7.12.0
Python 3.6.8 (default, Oct  7 2019, 12:59:55)
[GCC 8.3.0] on linux
runfile('/home/oredko/Desktop/cs366/hw7/hw7.py', wdir='/home/oredko/Desktop/cs366/hw7')
Grammar with 71 productions (start state = S)
    S -> NP VP
    S -> NP Aux VP
    NP -> Det Adj N
    NP -> Det Adj Adj N
    NP -> N
    NP -> Pro
    NP -> Det N
    NP -> NP CP
    NP -> NP Conj NP
    NP -> NP PP
    NP -> N N
    VP -> V PP
    VP -> V NP
    VP -> V NP PP
    VP -> V NP NP
    VP -> V AdjP
    VP -> V
    VP -> VP Conj VP
    VP -> V NP CP
    VP -> VP AdvP
    PP -> P NP
    CP -> Comp S
    AdjP -> Adj
    AdjP -> Adv Adj
    AdjP -> AdjP Conj AdjP
    AdvP -> Adv Adv
    Det -> 'the'
    Det -> 'his'
    Det -> 'her'
    N -> 'bully'
    N -> 'kid'
    N -> 'school'
    N -> 'book'
    N -> 'sister'
    N -> 't'
    N -> 'Homer'
    N -> 'Marge'
    N -> 'friends'
    N -> 'work'
    N -> 'bar'
    N -> 'Lisa'
    N -> 'brother'
    N -> 'peanut'
    N -> 'butter'
    V -> 'punched'
    V -> 'gave'
    V -> 'given'
    V -> 'are'
    V -> 'drank'
    V -> 'sang'
    V -> 'told'
    V -> 'liked'
    P -> 'after'
    P -> 'to'
    P -> 'from'
    P -> 'in'
    Adj -> 'big'
    Adj -> 'tiny'
    Adj -> 'nerdy'
    Adj -> 'poor'
    Adj -> 'happy'
    Adv -> 'very'
    Adv -> 'much'
    Pro -> 'he'
    Pro -> 'I'
    Pro -> 'him'
    Pro -> 'she'
    Comp -> 'that'
    Conj -> 'and'
    Conj -> 'but'
    Aux -> 'had'
[S -> NP VP, S -> NP Aux VP, NP -> Det Adj N, NP -> Det Adj Adj N, NP -> N, NP -> Pro, NP -> Det N, NP -> NP CP, NP -> NP Conj NP, NP -> NP PP, NP -> N N, VP -> V PP, VP -> V NP, VP -> V NP PP, VP -> V NP NP, VP -> V AdjP, VP -> V, VP -> VP Conj VP, VP -> V NP CP, VP -> VP AdvP, PP -> P NP, CP -> Comp S, AdjP -> Adj, AdjP -> Adv Adj, AdjP -> AdjP Conj AdjP, AdvP -> Adv Adv, Det -> 'the', Det -> 'his', Det -> 'her', N -> 'bully', N -> 'kid', N -> 'school', N -> 'book', N -> 'sister', N -> 't', N -> 'Homer', N -> 'Marge', N -> 'friends', N -> 'work', N -> 'bar', N -> 'Lisa', N -> 'brother', N -> 'peanut', N -> 'butter', V -> 'punched', V -> 'gave', V -> 'given', V -> 'are', V -> 'drank', V -> 'sang', V -> 'told', V -> 'liked', P -> 'after', P -> 'to', P -> 'from', P -> 'in', Adj -> 'big', Adj -> 'tiny', Adj -> 'nerdy', Adj -> 'poor', Adj -> 'happy', Adv -> 'very', Adv -> 'much', Pro -> 'he', Pro -> 'I', Pro -> 'him', Pro -> 'she', Comp -> 'that', Conj -> 'and', Conj -> 'but', Aux -> 'had']
Lexical item count:  45
VP rule count:  9
V rule count:  8
s6:
(S
  (NP (Det the) (Adj big) (N bully))
  (VP
    (V punched)
    (NP (Det the) (Adj tiny) (Adj nerdy) (N kid))
    (PP (P after) (NP (N school)))))
(S
  (NP (Det the) (Adj big) (N bully))
  (VP
    (V punched)
    (NP
      (NP (Det the) (Adj tiny) (Adj nerdy) (N kid))
      (PP (P after) (NP (N school))))))
s7:
(S
  (NP (Pro he))
  (VP
    (V gave)
    (NP (Det the) (N book))
    (PP (P to) (NP (Det his) (N sister)))))
(S
  (NP (Pro he))
  (VP
    (V gave)
    (NP
      (NP (Det the) (N book))
      (PP (P to) (NP (Det his) (N sister))))))
s8:
(S
  (NP (Pro he))
  (VP
    (V gave)
    (NP
      (NP (Det the) (N book))
      (CP
        (Comp that)
        (S
          (NP (Pro I))
          (Aux had)
          (VP (V given) (NP (Pro him)) (NP (N t))))))
    (PP (P to) (NP (Det his) (N sister)))))
(S
  (NP (Pro he))
  (VP
    (V gave)
    (NP
      (NP
        (NP (Det the) (N book))
        (CP
          (Comp that)
          (S
            (NP (Pro I))
            (Aux had)
            (VP (V given) (NP (Pro him)) (NP (N t))))))
      (PP (P to) (NP (Det his) (N sister))))))
(S
  (NP (Pro he))
  (VP
    (V gave)
    (NP
      (NP (Det the) (N book))
      (CP
        (Comp that)
        (S
          (NP (Pro I))
          (Aux had)
          (VP
            (V given)
            (NP (Pro him))
            (NP (NP (N t)) (PP (P to) (NP (Det his) (N sister))))))))))
(S
  (NP (Pro he))
  (VP
    (V gave)
    (NP
      (NP (Det the) (N book))
      (CP
        (Comp that)
        (S (NP (Pro I)) (Aux had) (VP (V given) (NP (Pro him))))))
    (NP (NP (N t)) (PP (P to) (NP (Det his) (N sister))))))
(S
  (NP (Pro he))
  (VP
    (V gave)
    (NP (Det the) (N book))
    (CP
      (Comp that)
      (S
        (NP (Pro I))
        (Aux had)
        (VP
          (V given)
          (NP (Pro him))
          (NP (NP (N t)) (PP (P to) (NP (Det his) (N sister)))))))))
s9:
(S
  (NP (NP (N Homer)) (Conj and) (NP (N Marge)))
  (VP
    (V are)
    (AdjP (AdjP (Adj poor)) (Conj but) (AdjP (Adv very) (Adj happy)))))
s10:
(S
  (NP
    (NP (NP (N Homer)) (Conj and) (NP (Det his) (N friends)))
    (PP (P from) (NP (N work))))
  (VP
    (VP (V drank))
    (Conj and)
    (VP (V sang) (PP (P in) (NP (Det the) (N bar))))))
(S
  (NP
    (NP (N Homer))
    (Conj and)
    (NP (NP (Det his) (N friends)) (PP (P from) (NP (N work)))))
  (VP
    (VP (V drank))
    (Conj and)
    (VP (V sang) (PP (P in) (NP (Det the) (N bar))))))
s11:
(S
  (NP (N Lisa))
  (VP
    (V told)
    (NP (Det her) (N brother))
    (CP
      (Comp that)
      (S
        (NP (Pro she))
        (VP
          (VP (V liked) (NP (N peanut) (N butter)))
          (AdvP (Adv very) (Adv much)))))))
(S
  (NP (N Lisa))
  (VP
    (V told)
    (NP (Det her) (N brother))
    (CP
      (Comp that)
      (S
        (NP (Pro she))
        (VP
          (VP (V liked) (NP (N peanut)) (NP (N butter)))
          (AdvP (Adv very) (Adv much)))))))
(S
  (NP (N Lisa))
  (VP
    (V told)
    (NP
      (NP (Det her) (N brother))
      (CP
        (Comp that)
        (S
          (NP (Pro she))
          (VP
            (VP (V liked) (NP (N peanut) (N butter)))
            (AdvP (Adv very) (Adv much))))))))
(S
  (NP (N Lisa))
  (VP
    (V told)
    (NP
      (NP (Det her) (N brother))
      (CP
        (Comp that)
        (S
          (NP (Pro she))
          (VP
            (VP (V liked) (NP (N peanut)) (NP (N butter)))
            (AdvP (Adv very) (Adv much))))))))
(S
  (NP (N Lisa))
  (VP
    (VP
      (V told)
      (NP
        (NP (Det her) (N brother))
        (CP (Comp that) (S (NP (Pro she)) (VP (V liked)))))
      (NP (N peanut) (N butter)))
    (AdvP (Adv very) (Adv much))))
(S
  (NP (N Lisa))
  (VP
    (VP
      (V told)
      (NP
        (NP (Det her) (N brother))
        (CP
          (Comp that)
          (S (NP (Pro she)) (VP (V liked) (NP (N peanut))))))
      (NP (N butter)))
    (AdvP (Adv very) (Adv much))))
(S
  (NP (N Lisa))
  (VP
    (VP
      (V told)
      (NP (Det her) (N brother))
      (CP
        (Comp that)
        (S (NP (Pro she)) (VP (V liked) (NP (N peanut) (N butter))))))
    (AdvP (Adv very) (Adv much))))
(S
  (NP (N Lisa))
  (VP
    (VP
      (V told)
      (NP (Det her) (N brother))
      (CP
        (Comp that)
        (S
          (NP (Pro she))
          (VP (V liked) (NP (N peanut)) (NP (N butter))))))
    (AdvP (Adv very) (Adv much))))
(S
  (NP (N Lisa))
  (VP
    (VP
      (V told)
      (NP
        (NP (Det her) (N brother))
        (CP
          (Comp that)
          (S
            (NP (Pro she))
            (VP (V liked) (NP (N peanut) (N butter)))))))
    (AdvP (Adv very) (Adv much))))
(S
  (NP (N Lisa))
  (VP
    (VP
      (V told)
      (NP
        (NP (Det her) (N brother))
        (CP
          (Comp that)
          (S
            (NP (Pro she))
            (VP (V liked) (NP (N peanut)) (NP (N butter)))))))
    (AdvP (Adv very) (Adv much))))
(s10): "Homer and his friends from work drank and sang in the bar"
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
 ...
s12:
(S
  (NP (NP (N Lisa)) (Conj and) (NP (Det her) (N friends)))
  (VP
    (V told)
    (NP
      (NP (N Marge))
      (CP
        (Comp that)
        (S (NP (N Homer)) (VP (V punched) (NP (Det the) (N bully))))))
    (PP (P in) (NP (Det the) (N bar)))))
(S
  (NP (NP (N Lisa)) (Conj and) (NP (Det her) (N friends)))
  (VP
    (V told)
    (NP
      (NP
        (NP (N Marge))
        (CP
          (Comp that)
          (S
            (NP (N Homer))
            (VP (V punched) (NP (Det the) (N bully))))))
      (PP (P in) (NP (Det the) (N bar))))))
(S
  (NP (NP (N Lisa)) (Conj and) (NP (Det her) (N friends)))
  (VP
    (V told)
    (NP
      (NP (N Marge))
      (CP
        (Comp that)
        (S
          (NP (N Homer))
          (VP
            (V punched)
            (NP (Det the) (N bully))
            (PP (P in) (NP (Det the) (N bar)))))))))
(S
  (NP (NP (N Lisa)) (Conj and) (NP (Det her) (N friends)))
  (VP
    (V told)
    (NP
      (NP (N Marge))
      (CP
        (Comp that)
        (S
          (NP (N Homer))
          (VP
            (V punched)
            (NP
              (NP (Det the) (N bully))
              (PP (P in) (NP (Det the) (N bar))))))))))
(S
  (NP (NP (N Lisa)) (Conj and) (NP (Det her) (N friends)))
  (VP
    (V told)
    (NP (N Marge))
    (CP
      (Comp that)
      (S
        (NP (N Homer))
        (VP
          (V punched)
          (NP (Det the) (N bully))
          (PP (P in) (NP (Det the) (N bar))))))))
(S
  (NP (NP (N Lisa)) (Conj and) (NP (Det her) (N friends)))
  (VP
    (V told)
    (NP (N Marge))
    (CP
      (Comp that)
      (S
        (NP (N Homer))
        (VP
          (V punched)
          (NP
            (NP (Det the) (N bully))
            (PP (P in) (NP (Det the) (N bar)))))))))
(S
  (NP (NP (N Lisa)) (Conj and) (NP (Det her) (N friends)))
  (VP
    (V told)
    (NP
      (NP (N Marge))
      (CP (Comp that) (S (NP (N Homer)) (VP (V punched)))))
    (NP (NP (Det the) (N bully)) (PP (P in) (NP (Det the) (N bar))))))
s13:
(S
  (NP (Det the) (Adj big) (N bully))
  (VP
    (VP (V liked) (NP (Det the) (Adj tiny) (Adj nerdy) (N kid)))
    (AdvP (Adv very) (Adv much))))
Grammar with 22 productions (start state = S)
    S -> NP Aux VP
    S -> Aux NP VP
    S -> NP VP
    NP -> N
    NP -> Det NP
    NP -> N N
    NP -> Det N PP
    VP -> V NP NP
    VP -> V NP
    PP -> P NP
    Det -> 'a'
    Det -> 'the'
    N -> 'Marge'
    N -> 'Homer'
    N -> 'ham'
    N -> 'sandwich'
    N -> 'donut'
    N -> 'table'
    V -> 'make'
    V -> 'ate'
    P -> 'on'
    Aux -> 'will'
[S -> NP Aux VP, S -> Aux NP VP, S -> NP VP, NP -> N, NP -> Det NP, NP -> N N, NP -> Det N PP, VP -> V NP NP, VP -> V NP, PP -> P NP, Det -> 'a', Det -> 'the', N -> 'Marge', N -> 'Homer', N -> 'ham', N -> 'sandwich', N -> 'donut', N -> 'table', V -> 'make', V -> 'ate', P -> 'on', Aux -> 'will']
{P -> 'on', S -> NP VP, PP -> P NP, N -> 'Marge', NP -> N, N -> 'ham', VP -> V NP NP, VP -> V NP, NP -> Det N PP, NP -> N N, Det -> 'a', NP -> Det NP, Det -> 'the', N -> 'donut', N -> 'sandwich', N -> 'Homer', S -> Aux NP VP, Aux -> 'will', N -> 'table', V -> 'make', V -> 'ate', S -> NP Aux VP}
Grammar with 83 productions (start state = S)
    S -> NP VP
    S -> NP Aux VP
    NP -> Det Adj N
    NP -> Det Adj Adj N
    NP -> N
    NP -> Pro
    NP -> Det N
    NP -> NP CP
    NP -> NP Conj NP
    NP -> NP PP
    NP -> N N
    VP -> V PP
    VP -> V NP
    VP -> V NP PP
    VP -> V NP NP
    VP -> V AdjP
    VP -> V
    VP -> VP Conj VP
    VP -> V NP CP
    VP -> VP AdvP
    PP -> P NP
    CP -> Comp S
    AdjP -> Adj
    AdjP -> Adv Adj
    AdjP -> AdjP Conj AdjP
    AdvP -> Adv Adv
    Det -> 'the'
    Det -> 'his'
    Det -> 'her'
    N -> 'bully'
    N -> 'kid'
    N -> 'school'
    N -> 'book'
    N -> 'sister'
    N -> 't'
    N -> 'Homer'
    N -> 'Marge'
    N -> 'friends'
    N -> 'work'
    N -> 'bar'
    N -> 'Lisa'
    N -> 'brother'
    N -> 'peanut'
    N -> 'butter'
    V -> 'punched'
    V -> 'gave'
    V -> 'given'
    V -> 'are'
    V -> 'drank'
    V -> 'sang'
    V -> 'told'
    V -> 'liked'
    P -> 'after'
    P -> 'to'
    P -> 'from'
    P -> 'in'
    Adj -> 'big'
    Adj -> 'tiny'
    Adj -> 'nerdy'
    Adj -> 'poor'
    Adj -> 'happy'
    Adv -> 'very'
    Adv -> 'much'
    Pro -> 'he'
    Pro -> 'I'
    Pro -> 'him'
    Pro -> 'she'
    Comp -> 'that'
    Conj -> 'and'
    Conj -> 'but'
    Aux -> 'had'
    S -> Aux NP VP
    NP -> Det NP
    NP -> Det N PP
    Det -> 'a'
    N -> 'ham'
    N -> 'sandwich'
    N -> 'donut'
    N -> 'table'
    V -> 'make'
    V -> 'ate'
    P -> 'on'
    Aux -> 'will'
s1:
(S
  (NP (N Marge))
  (Aux will)
  (VP (V make) (NP (Det a) (NP (N ham) (N sandwich)))))
(S
  (NP (N Marge))
  (Aux will)
  (VP (V make) (NP (Det a) (N ham)) (NP (N sandwich))))
(S
  (NP (N Marge))
  (Aux will)
  (VP (V make) (NP (Det a) (NP (N ham))) (NP (N sandwich))))
s2:
(S
  (Aux will)
  (NP (N Marge))
  (VP (V make) (NP (Det a) (NP (N ham) (N sandwich)))))
(S
  (Aux will)
  (NP (N Marge))
  (VP (V make) (NP (Det a) (N ham)) (NP (N sandwich))))
(S
  (Aux will)
  (NP (N Marge))
  (VP (V make) (NP (Det a) (NP (N ham))) (NP (N sandwich))))
s3:
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP
      (Det the)
      (NP (NP (N donut)) (PP (P on) (NP (Det the) (N table)))))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP
      (Det the)
      (NP (NP (N donut)) (PP (P on) (NP (Det the) (NP (N table))))))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP
      (NP (Det the) (N donut))
      (PP (P on) (NP (Det the) (N table))))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP
      (NP (Det the) (N donut))
      (PP (P on) (NP (Det the) (NP (N table)))))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP
      (NP (Det the) (NP (N donut)))
      (PP (P on) (NP (Det the) (N table))))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP
      (NP (Det the) (NP (N donut)))
      (PP (P on) (NP (Det the) (NP (N table)))))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP (Det the) (N donut) (PP (P on) (NP (Det the) (N table))))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP
      (Det the)
      (N donut)
      (PP (P on) (NP (Det the) (NP (N table)))))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP (Det the) (N donut))
    (PP (P on) (NP (Det the) (N table)))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP (Det the) (N donut))
    (PP (P on) (NP (Det the) (NP (N table))))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP (Det the) (NP (N donut)))
    (PP (P on) (NP (Det the) (N table)))))
(S
  (NP (N Homer))
  (VP
    (V ate)
    (NP (Det the) (NP (N donut)))
    (PP (P on) (NP (Det the) (NP (N table))))))
s14:
(S
  (Aux will)
  (NP (Det the) (Adj big) (N bully))
  (VP
    (V make)
    (NP (Det the) (Adj tiny) (Adj nerdy) (N kid))
    (NP (Det a) (NP (N ham) (N sandwich)))))
I'm satisfied with the result.
Grammar with 83 productions (start state = S)
    S -> NP VP
    S -> NP Aux VP
    NP -> Det Adj N
    NP -> Det Adj Adj N
    NP -> N
    NP -> Pro
    NP -> Det N
    NP -> NP CP
    NP -> NP Conj NP
    NP -> NP PP
    NP -> N N
    VP -> V PP
    VP -> V NP
    VP -> V NP PP
    VP -> V NP NP
    VP -> V AdjP
    VP -> V
    VP -> VP Conj VP
    VP -> V NP CP
    VP -> VP AdvP
    PP -> P NP
    CP -> Comp S
    AdjP -> Adj
    AdjP -> Adv Adj
    AdjP -> AdjP Conj AdjP
    AdvP -> Adv Adv
    Det -> 'the'
    Det -> 'his'
    Det -> 'her'
    N -> 'bully'
    N -> 'kid'
    N -> 'school'
    N -> 'book'
    N -> 'sister'
    N -> 't'
    N -> 'Homer'
    N -> 'Marge'
    N -> 'friends'
    N -> 'work'
    N -> 'bar'
    N -> 'Lisa'
    N -> 'brother'
    N -> 'peanut'
    N -> 'butter'
    V -> 'punched'
    V -> 'gave'
    V -> 'given'
    V -> 'are'
    V -> 'drank'
    V -> 'sang'
    V -> 'told'
    V -> 'liked'
    P -> 'after'
    P -> 'to'
    P -> 'from'
    P -> 'in'
    Adj -> 'big'
    Adj -> 'tiny'
    Adj -> 'nerdy'
    Adj -> 'poor'
    Adj -> 'happy'
    Adv -> 'very'
    Adv -> 'much'
    Pro -> 'he'
    Pro -> 'I'
    Pro -> 'him'
    Pro -> 'she'
    Comp -> 'that'
    Conj -> 'and'
    Conj -> 'but'
    Aux -> 'had'
    S -> Aux NP VP
    NP -> Det NP
    NP -> Det N PP
    Det -> 'a'
    N -> 'ham'
    N -> 'sandwich'
    N -> 'donut'
    N -> 'table'
    V -> 'make'
    V -> 'ate'
    P -> 'on'
    Aux -> 'will'