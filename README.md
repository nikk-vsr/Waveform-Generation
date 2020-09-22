# Waveform-Generation
Generating Waveform from the test input data given in dictionary format in python.

Matplotlib library is used to generate waveoform.

All programs has to be in same folder.

#Sample Input data of a test case. 
#Each element of inputdata represents a action in it.

inputdata=[[['Set', 'KL15', 1.0, '', '', ''], ['Wait', '', 1.0, '', '', '']], \
[['Set', 'KL30', 0.0, '', '', ''], ['Wait', '', 1.0, '', '', '']],\
[['Set', 'KL30', 1.0, '', '', ''], ['Wait', '', 1.0, '', '', '']]]

inputdata[0]= [['Set', 'KL15', 1.0, '', '', ''], ['Wait', '', 1.0, '', '', '']]  --> Action(1)\
inputdata[1]=[['Set', 'KL30', 0.0, '', '', ''], ['Wait', '', 1.0, '', '', '']] --->  Action(2)\
inputdata[2]= [['Set', 'KL45', 1.0, '', '', ''], ['Wait', '', 1.0, '', '', '']]--->  Action(3)

--> input data can be changed in main() function.
--> Run main() function to get the output.

