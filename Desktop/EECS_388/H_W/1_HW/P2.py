import math
import os
import random
import re
import sys


cypherText = """TUSQIQEGBFQTDHTUSZIXENQGXKGAAFHKMRXRRBJBGSFUWVEHPLVBWPZXHBIUBGETNZOBGIDHBHLZMNNBGBGIIEVRZRISSCOTNAEQVLUZRDVBGMDHTUSOWUITUOWBGIHBFVMRSFGVHZZRGRFVJNVESCUBGIIEFLLDVSJOVANKRROWBGETGVHGVIRRKLTKMNTHRNZGERJHVSLEGSUZNVOSHKMCSOEWIBGIIEADASIRFVHIQXSJSUMRXENRBIRXHRMZIKOEQPHAHHEGVHUAYTNFRLSLEUCUADSFECKIMVESIVMCXHRKDGZRDUSVBNSDFKHISMNTOQLSVEZPOQMKIAOIMZVTUOWEZWGEWHDNYSGCVMDXHRBOMFSLNGOIHHHVGKIMHSBBKQRIYRGDVCWAAUVWLIWBFGASLAGKHVSWOSHLVSLETZRWLYNGWOPDWUSTHZDHHVAVMKJTBPHTDHAAROMFSLNGSIRWEQWQIMHTUSUMRXOBRJQLPIGVHLVERSZHNSELYOOWMIHVGNVDISFVRWJENQVHEZWWECWPVMTUVLURILSVHZDMSNHKQMKUAVHIQHOSVHAZMDNBHTEAIYZJWTRDRFJZNYNQOQLZHWNFILZVEACWEHXHGVDBGIPYIQODHIAPXBHXSRSPMCXOUWPBGETUSGZZKGRRKQRJERHOQJILROGWUIRGVHBGVEFVRTCENQOWWMGENPOQMHNRGVKZQEHDRVGMMRJHVTTOAULUKMGYELVRWOAKKWGEDJOOSDHUAOIZZMDVBPIMCDRSSXKECRGRNSLEJCUTCERNURZMLAQPUWTKHGHRZBLEFTUWLHUAVDZQSWNBGVNAHRKHVSEHROGJDERVBJWMIAYCIBZRDRZOICENJWWPZROGVHZVINGOWBGIRROUIMHGVAOQRXUZPOQMKBRVLVCWTECYMSSOISUBZOEUWPPDGOHZGADINBHKQMKBHHWPDHIZTOILIOSHKMSSRPVHAAYTVTWPDGOZDDVXLAYHHLSLEESVMDQEQOQMMHLRGVEGMSCSUWEZOVQHAZPLNPRCSLIZOPCQQUECIENVDFWQVNXOAUXMSLAGVHPZHEISUPDERQPHNNVEACWPHRGNGVIHPEQHKMBSMCOQGMSRJWWPRXOBRWPDMRCOVAZKENBGGDXSGSDLHPYSSDZFVEJCQBGIDJOUNZWHRKHVSSNZCVBNJAYZEMBEUFSKMJREJBRESLAGHKMQICBIOLAINBHXZMMNTPDKJELYHKMOETUGEMGM"""

# "tus", "HKM" repeats 5 times

english_Freq = {"A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
				"G": .02015, "H": .06094, "I": .06996, "J": .00153, "K": .00772, "L": .04025,
				"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
				"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
				"Y": .01974, "Z": .00074}

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decypher(ct, key):
    newText = ""
    cycle = 0
    for i in range(len(ct)):
        newText += shifter(ct[i], key[cycle % len(key)])
        cycle +=1
    return newText


def shifter(toBeShifted, shiftBy):
    idx = alphabet.find(toBeShifted)
    idxShift = alphabet.find(shiftBy)
    return alphabet[(idx + (26 - idxShift)) % 26]
def diffSQed(x, mean):
	return (x - mean)**2

def reset():
    english_Freq = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0,
    				"G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0,
    				"M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0,
    				"S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
    				"Y": 0, "Z": 0}
    return english_Freq

def findKeyLength(cypherText, keyLength):
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
        for key in english_Freq: #sum pop Var using each  "x sub i" with 1/26
            #if english_Freq[key] != 0:
            sum_pop_var += diffSQed(english_Freq[key], 1/26)
        popVar.append(sum_pop_var / 26.)
##variance = 1/N * sum from 1 to N of (x sub i - mu)^2
    return(sum(popVar)/keyLength)
#key is a factor of cypherText
lengthOfKey = -1
curMax = -1
for i in range(1, 10):
    print(str(i) + ": ", end = "")
    a = findKeyLength(cypherText.rstrip("\n"), i)
    print(a)
    if(a > curMax):
	    lengthOfKey = i
	    curMax = a
print(lengthOfKey)

step_1 = "Step_1: Found key length to be " + str(lengthOfKey) + " using technique from Prob_E"
print(step_1)
print("Break text into " + str(lengthOfKey) + " individual sets as a collection of k independent Caesar ciphers")

def splitCT(cypherText, kl):
    setOfFreqencies= []
    for i in range(kl):
		#reset frequencies and variables for each set
        setFreq = reset()
        mean = 0
        sum_pop_var = 0
        countEle = 0
        for x in range(i, len(cypherText), kl):
            setFreq[cypherText[x]] += 1
            countEle += 1
        for key in setFreq:
            setFreq[key] /= countEle
        print("Set Freq for "+ str(i) + ":")
        print(setFreq)
        print("Compare to Standard English")
        print(english_Freq)
        setOfFreqencies.append(setFreq)
    #print(setOfFreqencies)


# A     = A is first letter in key resembled englush freq ie no shift
# M + 1 = N is second letter found by finding 000 as xyz
# N + 1 = O is third letter found by  0 0 0 approximation shift to z
# B + 1 = D is fourth by finding xyzabcde resemblence
# H + 1 = I is fifith letter found by value resembling e and shifting to it
# Y + 1 = Z is sixth letter 0 .1 0 resembling xyz
# D + 1 = E is seventh leter

iFoundYou = "ANODIZE"
splitCT(cypherText, lengthOfKey)
print(decypher(cypherText, iFoundYou))
