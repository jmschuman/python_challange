import math
import os
import random
import re
import sys

#(a) What is the population variance of the relative letter frequencies in English text?
#variance = 1/N * sum from 1 to N of (x sub i - mu)^2
def encrypt(plaintext, key):
	newText = ""
	cycle = 0
	for i in range(len(plaintext)):
		newText += shiftLetter(plaintext[i], key[cycle % len(key)])
		cycle +=1
	return newText
def diffSQed(x, mean):
	return (x - mean)**2
def probA(letter_freq):
	summ, sumVar = 0, 0
	for key in letter_freq:
		summ += letter_freq[key]
	avg = summ / 26 # len(letter_freq) or 26 letters...

	for key in letter_freq:
		sumVar += diffSQed(letter_freq[key], avg)

	return (1/26) * sumVar

#(b) What is the variance of the relative letter frequencies in the given plaintext?

def probB(pt):
	sumVar, summ = 0, 0
	ptl_freq = {}
	#num occur per letters
	for letter in pt:
		if letter in ptl_freq:
			ptl_freq[letter] += 1
		else:
			ptl_freq[letter] = 1
	#print(ptl_freq)
	#individual prob based on pt len
	#avg for all letters
	for letter in ptl_freq:
		ptl_freq[letter] /= float(len(pt))
		summ += ptl_freq[letter]
	avg = summ / 26.
	#var function
	for letter in ptl_freq:
		sumVar += diffSQed(ptl_freq[letter], avg)
	return (1/26) * sumVar

def probC(pt, key): # xyz 012 012 % len(key)
	shift = 0
	encrypted = encrypt(pt, key)
	return probB(encrypted)

def probC_print():
	print("Problem 1C: ")
	print("Key = yz Var = ", end = "")
	print(probC(plaintext, "yz"))
	print("Key = xyz Var = ", end = "")
	print(probC(plaintext, "xyz"))
	print("Key = wxyz Var = ", end = "")
	print(probC(plaintext, "wxyz"))
	print("Key = vwxyz Var = ", end = "")
	print(probC(plaintext, "vwxyz"))
	print("Key = uvwxyz Var = ", end = "")
	print(probC(plaintext, "uvwxyz"))
	observation = """As the key used for encryption gets longer, the population varience in the cyphertext becomes smaller.
	"""
	print(observation)

################################################################################
def shiftLetter(toBeShifted,shiftBy):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	idx = alphabet.find(toBeShifted)
	idxShift = alphabet.find(shiftBy)
	return alphabet[(idx + idxShift) % 26]

def reset():
    english_Freq = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
    				"g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
    				"m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
    				"s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
    				"y": 0, "z": 0}
    return english_Freq

def probE(cypherText, keyLength):
    popVar = []
    for i in range(keyLength):
		#reset frequencies and variables for each set
        english_Freq = reset()
        mean = 0
        sum_pop_var = 0
        countEle = 0
        for x in range(i, len(cypherText), keyLength):
            english_Freq[cypherText[x]] += 1
            countEle += 1
        for key in english_Freq:
            english_Freq[key] /= countEle #devide by elements in specific set
        for key in english_Freq: #sum pop Var using each  "x sub i" with countEle
            #if english_Freq[key] != 0:
            sum_pop_var += diffSQed(english_Freq[key], 1/26)
        popVar.append(sum_pop_var / 26.)
##variance = 1/N * sum from 1 to N of (x sub i - mu)^2
    return(sum(popVar)/keyLength)


def probDD(plaintext, key):
	encrypted = encrypt(plaintext, key)
	return probE(encrypted, len(key))

def probDPrint():
	print("Problem 1D: ")
	print("Key = yz Var = ", end = "")
	print(probDD(plaintext, "yz"))
	print("Key = xyz Var = ", end = "")
	print(probDD(plaintext, "xyz"))
	print("Key = wxyz Var = ", end = "")
	print(probDD(plaintext, "wxyz"))
	print("Key = vwxyz Var = ", end = "")
	print(probDD(plaintext, "vwxyz"))
	print("Key = uvwxyz Var = ", end = "")
	print(probDD(plaintext, "uvwxyz"))
	observation = """The mean variances observed are more like those found from problem 1B. This is becuase they more closley approximate the original relative letter frequencies of the plaintext by taking them as groups of individual 1 letter keys."""
	print(observation)
def probEPrint(ct):
	print("Problem E: ")
	for i in range(1, 7):
		print( "Attempt at key length " + str(i) + ": ", end = "")
		print(probE(ct, i))

letter_freq = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
				"G": .02015, "H": .06094, "I": .06996, "J": .00153, "K": .00772, "L": .04025,
				"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
				"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
				"Y": .01974, "Z": .00074 }

plaintext = "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"

print("Problem 1A: ", end = "")
print(probA(letter_freq))
print("Problem 1B: ", end = "")
print(probB(plaintext))
probC_print()
probDPrint()
probEPrint(encrypt(plaintext, "uvwxyz"))






"""
def probD_yz(pt, key):
	pt_key1, pt_key2 = [], []
	l = len(key)
	#seperate into y and z pt
	for i in range(0, len(pt)-1,l):
		pt_key1.append(pt[i])
		pt_key2.append(pt[i+1])
	#shift evens and 0 by y
	for i in range(len(pt_key1)):
		pt_key1[i] = shifter(pt_key1[i], key[0])
	#shift odds by z
	for i in range(len(pt_key2)):
		pt_key2[i] = shifter(pt_key2[i] ,key[1])

	one = findVar(pt_key1, len(pt_key1))
	two = findVar(pt_key2, len(pt_key2))
	sumVar1, sumVar2 = 0, 0
	#variance = 1/26 * sum from 1 to 26 of (x sub i - mu)^2
	for key in one:
		sumVar1 += diffSQed(one[key], 1/26)
	for key in two:
		sumVar2 += diffSQed(two[key], 1/26)
	sumVar1 /= 26.
	sumVar2 /= 26.
	print("Key = yz Var= ", end = "")
	print((sumVar1 + sumVar2)/2.)

def probD_xyz(pt, key):
	pt_key1, pt_key2, pt_key3  = [], [], []
	l = len(key)
	#seperate into y and z pt
	for i in range(0, len(pt)-2,l):
		pt_key1.append(pt[i])
		pt_key2.append(pt[i+1])
		pt_key3.append(pt[i+2])
	#shift evens and 0 by y
	for i in range(len(pt_key1)):
		pt_key1[i] = shifter(pt_key1[i], key[0])
	#shift odds by z
	for i in range(len(pt_key2)):
		pt_key2[i] = shifter(pt_key2[i] ,key[1])
	for i in range(len(pt_key3)):
		pt_key3[i] = shifter(pt_key3[i] ,key[2])

	one   = findVar(pt_key1, len(pt_key1))
	two   = findVar(pt_key2, len(pt_key2))
	three = findVar(pt_key3, len(pt_key3))

	sumVar1, sumVar2, sumVar3 = 0, 0, 0

	#variance = 1/26 * sum from 1 to 26 of (x sub i - mu)^2
	for key in one:
		sumVar1 += diffSQed(one[key], 1/26.)
	for key in two:
		sumVar2 += diffSQed(two[key], 1/26.)
	for key in three:
		sumVar3 += diffSQed(three[key], 1/26.)
	sumVar1 /= 26.
	sumVar2 /= 26.
	sumVar3 /= 26.
	print("Key = xyz Var= ", end = "")
	print((sumVar1 + sumVar2+ sumVar3)/3.)

def probD_wxyz(pt, key):
	pt_key1, pt_key2, pt_key3, pt_key4  = [], [], [], []
	l = len(key)
	#seperate into y and z pt
	for i in range(0, len(pt)-3,l):
		pt_key1.append(pt[i])
		pt_key2.append(pt[i+1])
		pt_key3.append(pt[i+2])
		pt_key4.append(pt[i+3])
	#shift evens and 0 by y
	for i in range(len(pt_key1)):
		pt_key1[i] = shifter(pt_key1[i], key[0])
	#shift odds by z
	for i in range(len(pt_key2)):
		pt_key2[i] = shifter(pt_key2[i], key[1])
	for i in range(len(pt_key3)):
		pt_key3[i] = shifter(pt_key3[i], key[2])
	for i in range(len(pt_key4)):
		pt_key4[i] = shifter(pt_key4[i], key[3])

	one   = findVar(pt_key1, len(pt_key1))
	two   = findVar(pt_key2, len(pt_key2))
	three = findVar(pt_key3, len(pt_key3))
	four = findVar(pt_key4, len(pt_key4))

	sumVar1, sumVar2, sumVar3, sumVar4 = 0, 0, 0,0

	#variance = 1/26 * sum from 1 to 26 of (x sub i - mu)^2
	for key in one:
		sumVar1 += diffSQed(one[key], 1/26.)
	for key in two:
		sumVar2 += diffSQed(two[key], 1/26.)
	for key in three:
		sumVar3 += diffSQed(three[key], 1/26.)
	for key in four:
		sumVar4 += diffSQed(four[key], 1/26.)
	sumVar1 /= 26.
	sumVar2 /= 26.
	sumVar3 /= 26.
	sumVar4 /= 26.
	print("Key = wxyz Var= ", end = "")
	print((sumVar1 + sumVar2+ sumVar3 + sumVar4)/4.)

def probD_vwxyz(pt, key):
	pt_key1, pt_key2, pt_key3, pt_key4, pt_key5  = [], [], [], [], []
	l = len(key)
	#seperate into y and z pt
	for i in range(0, len(pt)-4,l):
		pt_key1.append(pt[i])
		pt_key2.append(pt[i+1])
		pt_key3.append(pt[i+2])
		pt_key4.append(pt[i+3])
		pt_key5.append(pt[i+4])
	#shift evens and 0 by y
	for i in range(len(pt_key1)):
		pt_key1[i] = shifter(pt_key1[i], key[0])
	#shift odds by z
	for i in range(len(pt_key2)):
		pt_key2[i] = shifter(pt_key2[i], key[1])
	for i in range(len(pt_key3)):
		pt_key3[i] = shifter(pt_key3[i], key[2])
	for i in range(len(pt_key4)):
		pt_key4[i] = shifter(pt_key4[i], key[3])
	for i in range(len(pt_key5)):
		pt_key5[i] = shifter(pt_key5[i], key[4])

	one   = findVar(pt_key1, len(pt_key1))
	two   = findVar(pt_key2, len(pt_key2))
	three = findVar(pt_key3, len(pt_key3))
	four = findVar(pt_key4, len(pt_key4))
	five = findVar(pt_key5, len(pt_key5))

	sumVar1, sumVar2, sumVar3, sumVar4, sumVar5 = 0, 0, 0, 0, 0

	#variance = 1/26 * sum from 1 to 26 of (x sub i - mu)^2
	for key in one:
		sumVar1 += diffSQed(one[key], 1/26.)
	for key in two:
		sumVar2 += diffSQed(two[key], 1/26.)
	for key in three:
		sumVar3 += diffSQed(three[key], 1/26.)
	for key in four:
		sumVar4 += diffSQed(four[key], 1/26.)
	for key in five:
		sumVar5 += diffSQed(five[key], 1/26.)
	sumVar1 /= 26.
	sumVar2 /= 26.
	sumVar3 /= 26.
	sumVar4 /= 26.
	sumVar5 /= 26.
	print("Key = vwxyz Var= ", end = "")
	print((sumVar1 + sumVar2+ sumVar3 + sumVar4 + sumVar5)/5.)
def probD_uvwxyz(pt, key):
	pt_key1, pt_key2, pt_key3, pt_key4, pt_key5, pt_key6  = [], [], [], [], [], []

	l = len(key)
	#seperate into y and z pt
	for i in range(0, len(pt)-5,l):
		pt_key1.append(pt[i])
		pt_key2.append(pt[i+1])
		pt_key3.append(pt[i+2])
		pt_key4.append(pt[i+3])
		pt_key5.append(pt[i+4])
		pt_key6.append(pt[i+5])
	#shift evens and 0 by y
	for i in range(len(pt_key1)):
		pt_key1[i] = shifter(pt_key1[i], key[0])
	#shift odds by z
	for i in range(len(pt_key2)):
		pt_key2[i] = shifter(pt_key2[i], key[1])
	for i in range(len(pt_key3)):
		pt_key3[i] = shifter(pt_key3[i], key[2])
	for i in range(len(pt_key4)):
		pt_key4[i] = shifter(pt_key4[i], key[3])
	for i in range(len(pt_key5)):
		pt_key5[i] = shifter(pt_key5[i], key[4])
	for i in range(len(pt_key6)):
		pt_key6[i] = shifter(pt_key6[i], key[5])

	one   = findVar(pt_key1, len(pt_key1))
	two   = findVar(pt_key2, len(pt_key2))
	three = findVar(pt_key3, len(pt_key3))
	four  = findVar(pt_key4, len(pt_key4))
	five  = findVar(pt_key5, len(pt_key5))
	six   = findVar(pt_key6, len(pt_key6))

	sumVar1, sumVar2, sumVar3, sumVar4, sumVar5, sumVar6 = 0, 0, 0, 0, 0, 0

	#variance = 1/26 * sum from 1 to 26 of (x sub i - mu)^2
	for keyy in one:
		sumVar1 += diffSQed(one[keyy], 1/26.)
	for key in two:
		sumVar2 += diffSQed(two[keyy], 1/26.)
	for keyy in three:
		sumVar3 += diffSQed(three[keyy], 1/26.)
	for keyy in four:
		sumVar4 += diffSQed(four[keyy], 1/26.)
	for keyy in five:
		sumVar5 += diffSQed(five[keyy], 1/26.)
	for keyy in six:
		sumVar6 += diffSQed(six[keyy], 1/26.)
	sumVar1 /= 26.
	sumVar2 /= 26.
	sumVar3 /= 26.
	sumVar4 /= 26.
	sumVar5 /= 26.
	sumVar6 /= 26.
	print("Key = uvwxyz Var= ", end = "")
	print((sumVar1 + sumVar2+ sumVar3 + sumVar4 + sumVar5 + sumVar6)/6.)

"""
