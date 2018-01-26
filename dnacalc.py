#! /usr/bin/env python
#There is no slash after env as this is a program and not a folder

#This program takes a DNA sequence (without checking)
#and shows its length and the nucleotide composition

DNASeq = 'ATGAAC' 	#the DNASeq definition
DNASeq = raw_input ("Enter a DNA sequence: ") 	#Using this command will make the program forget any original values and will wait for user input (which can be pasted or typed) before running.
DNASeq = DNASeq.upper() 	#convert to uppercase for .count() function
DNASeq = DNASeq.replace(" "," ") 	#remove spaces

print 'Sequence:', DNASeq 	#The program will print information about the sequence

SeqLength = float(len(DNASeq)) 	#This result is evaluated first and then used as the input to function float

print 'Sequence Length', SeqLength 	#The sequence length will be printed

#The below commands create four new integer variables and each contain the count of how many times the corresponding nucleotide is found within a sequence string
NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')

#Old way to output the Numbers (now removed)
# print "A:", NumberA/SeqLength
# print "C:", NumberC/SeqLength
# print "G:", NumberG/SeqLength
# print "T:", NumberT/SeqLength

#Calculate percentage and output to 1 decimal and the %% after will display a % after the results instead of only an number
print "A: %.1f" % (100 * NumberA / SeqLength)
print "C: %.1f" % (100 * NumberC / SeqLength)
print "G: %.1f" % (100 * NumberG / SeqLength)
print "T: %.1f" % (100 * NumberT / SeqLength)

#notinscript: print "There are %d A bases." % (NumberA) 	this command can be used to determin how integers are interpreted 
#notinscript: print "A occurs in %d bases out of %d." % (NumberA, SeqLength) 	this command will tell you how many times the integer appears from the total number
#notinscript: print "A occurs in %.2f bases out of %d." % (NumberA/SeqLength, SeqLength).	this command expresses decimal precision and will display the desired information to the commanded number of decimal places


