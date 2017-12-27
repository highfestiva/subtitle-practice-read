#!/usr/bin/env python3

import os
import random
import sys
import time


verbs = 'hoppar skuttar blir gråter springer lufsar sabbar förstör gräver skottar fiskar jagar slår skjuter markerar bajsar kissar går'.split()
nouns = 'kaniner bord pjäser byar hus madrasser folksamlingar vargen skjulet trädet gräsmattan fåraherden slaktaren jultomten datorn dagböcker kepsar'.split()
prefixed_nouns = 'en_stol ett_hus en_madrass ett_tåg'.split()
prepositions = 'över under mellan framför bredvid i på till åt ur mot genom efter utan'.split()
pronouns = 'jag du vi ni han hon de'.split()
adjectives = 'gula fula gamla nya sneda tråkiga hemska rika sorgsna döda'.split()
adverbs = 'glatt snabbt långsamt efterblivet snett kort'.split()

forms_s = 'nvpn Pvpn Nvpn PvpN nvpN NvpN nvApan PvApan panvP panvN'.split()
lookup = dict(n=nouns, p=prepositions, v=verbs, P=pronouns, N=prefixed_nouns, a=adjectives, A=adverbs)
forms = [[lookup[e] for e in sentence] for sentence in forms_s]

delay_letter = float(sys.argv[1])
delay_between_sentences = float(sys.argv[2])
h,w = os.popen('stty size', 'r').read().split()
h,w = int(h),int(w)

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def sentencify(classes):
	words = [random.choice(cl) for cl in classes]
	s = ' '.join(words).replace('_', ' ')
	s = s[0].upper() + s[1:] + '. '
	return s

while True:
	clear()
	for _ in range(h-3):
		print()
	classes = random.choice(forms)
	s = sentencify(classes)
	while random.random() > 0.7:
		classes = random.choice(forms)
		s += sentencify(classes)
	print('       ', s)
	time.sleep(delay_letter*len(s))
	clear()
	time.sleep(delay_between_sentences)
