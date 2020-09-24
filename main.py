import subplotsWaveform
#import ScrollWaveformPlot

#Sample inputdata dummy data is given, so you can selet any of these to test

#inputdata=[[['Set', 'KL30', 0.0, '', 'Set KL15 to 0', ''], ['Wait', '', 3.0, 's', 'Wait for 3 Sec', ''], ['Set', 'KL15', 1.0, '', 'Set KL15 to 1', ''], ['Wait', '', 3.0, 's', 'Wait for 3 Sec', '']], [['Set', 'KL15', 1.0, '', 'Set KL15 to 1', ''], ['Wait', '', 3.0, 's', 'Wait for 3 Second', ''], ['Set', 'MO_EM2_Sollmodus_Switch', 1.0, '', 'Set MO_EM2_Sollmodus_Switch to 1', ''], ['Wait', '', 0.1, 's', 'Wait for 0.1 sec', ''], ['Set', 'MO_EM2_Sollmodus', 1.0, '', 'Set MO_EM2_Sollmodus to 1', ''], ['Ramp', 'HV_Bench_Battery_Voltage.abc', '700,750,10', '', '', 0.2]], [['Set', 'TME_EM2_IstVolumenstrom', 10.0, '', 'Set TME_EM2_IstVolumenstrom to 10 ', ''], ['Wait', '', 2.0, 's', 'Wait for 2 second', ''], ['Set', 'TME_EM2_IstVolumenstrom', 50.0, '', 'Set TME_EM2_IstVolumenstrom to 50', ''], ['Wait', '', 2.0, 's', 'Wait for 2 second', '']]]
'''
inputdata=[[['Set', 'KL15', 1.0, '', '', ''], ['Wait', '', 1.0, '', '', '']],
[['Set', 'KL30', 0.0, '', '', ''], ['Wait', '', 1.0, '', '', '']],[['Set', 'KL45', 1.0, '', '', ''], ['Wait', '', 1.0, '', '', '']]]
'''

inputdata=[[["Set", "KL30",1, "","Set KL30 to 1", ""],["Set","KL15",1, "","Set KL15 to 1", ""],["Wait","",3,"","Wait for 3 secs", ""]]
,[["Set", "HVDC",380,"V","Set HVDC to 380",""],["Wait","",3,"","Wait for 3 secs", ""],["Set","MO_EM1_SollModus",1,"","Set Mo_EM1 Sollmodus to 1",""],["Wait","",3,"Wait for 3 secs", ""]]
,[["Set","MO_EM1_SollModus",0,"","Set Mo_EM1Sollmodus to 0",""],["Wait","",3,"Wait for 3 secs", ""]]
,[["Set","MO_EM1_SollModus",1,"","Set Mo_EM1Sollmodus to 1",""],["Set", "KL15",0,"","Set KL15 to 0", ""],["Set","Rotortemp",50,"DegC","Set rotor temp to 50",""] ,["Wait","",3,"","Wait for 3 secs", ""]]
,[["Ramp","SOLLMOMENT",'-40,100,20',"Nm","Ramp Sollmoment from 0 to 100 in 20",1], ["Wait","",2,"","Wait for 2 secs", ""],["Set","MOMENT",3000,"Nm","set moment to 3000",""],["Wait","",2,"","Wait for 2 secs", ""]]          #test case- ramp signal is first finding
,[["Set","KL15",0,"","Set KL15 to 0",""],["Wait","",2,"Wait for 2 secs", ""]]
,[["Set","Speed",10,"rpm","Set speed to 10",""], ["Set","IGBTtemp",-10,"DegC","Set IGBT temp to 10"],["Set","Vbatt",12,"V","Set Vbatt to 12",""],["Wait","",2,"Wait for 2 secs", ""]]  
,[["Ramp","StatorTemp",'20,100,20', "DegC", "Ramp stator temp from 20 to 100 in 20 ",1 ],["Set","coolanttemp",-20,"DegC","Set coolant temp to 20",""],["Set","Speed",30,"rpm","Set speed to 30",""],["Wait","",2,"Wait for 2 secs", ""]]  # resolved: limitation that last action should not be new signal
,[["Set","Rotortemp",100,"DegC","Set rotor temp to 100", ""], ["Set","IGBTtemp",20,"DegC","Set IGBT temp to 10"], ["Set","coolanttemp",20,"DegC","Set coolant temp to 20",""],["Wait","",2,"Wait for 2 secs", ""]]     
,[["Set","Flowrate",10,"L/min","Set Flowrate to 10",""],["Wait","",2,"Wait for 2 secs", ""]]]

'''
# inputdata=[[["Ramp","SOLLMOMENT","-40,100,20","Nm","Ramp Sollmoment from 0 to 100 in 20",1], ["Wait","",2,"","Wait for 2 secs", ""],["Set","MOMENT",3000,"Nm","set moment to 3000",""],["Wait","",2,"","Wait for 2 secs", ""]]          #test case- ramp signal is first finding
,[["Set","KL15",0,"","Set KL15 to 0",""],["Wait","",2,"Wait for 2 secs", ""]]
,[["Set","Speed",10,"rpm","Set speed to 10",""], ["Set","IGBTtemp",-10,"DegC","Set IGBT temp to -10"],["Set","Vbatt",12,"V","Set Vbatt to 12",""],["Wait","",2,"Wait for 2 secs", ""]]
,[["Ramp","StatorTemp",'20,100,20', "DegC", "Ramp stator temp from 20 to 100 in 20 ",1 ],["Set","coolanttemp",-20,"DegC","Set coolant temp to 20",""],["Set","Speed",30,"rpm","Set speed to 30",""],["Wait","",2,"Wait for 2 secs", ""]]  # resolved: limitation that last action should not be new signal
,[["Set","Rotortemp",100,"DegC","Set rotor temp to 100", ""], ["Set","IGBTtemp",20,"DegC","Set IGBT temp to 20"], ["Set","coolanttemp",20,"DegC","Set coolant temp to 20",""],["Wait","",2,"Wait for 2 secs", ""]] ]    
'''

'''
inputdata=[[["Set", "KL30",1, "","Set KL30 to 1", ""],["Set","KL15",1, "","Set KL15 to 1", ""],["Wait","",3,"","Wait for 3 secs", ""]]
,[["Set", "HVDC",380,"V","Set HVDC to 380",""],["Wait","",3,"","Wait for 3 secs", ""],["Set","MO_EM1_SollModus",1,"","Set Mo_EM1 Sollmodus to 1",""],["Wait","",3,"Wait for 3 secs", ""]]
,[["Set","MO_EM1_SollModus",0,"","Set Mo_EM1Sollmodus to 0",""],["Wait","",3,"Wait for 3 secs", ""]]
,[["Set","MO_EM1_SollModus",1,"","Set Mo_EM1Sollmodus to 1",""],["Set", "KL15",0,"","Set KL15 to 0", ""],["Set","Rotortemp",50,"DegC","Set rotor temp to 50",""] ,["Wait","",3,"","Wait for 3 secs", ""]]
,[["Ramp","SOLLMOMENT",[-40,100,20],"Nm","Ramp Sollmoment from 0 to 100 in 20",1], ["Wait","",2,"","Wait for 2 secs", ""],["Set","MOMENT",3000,"Nm","set moment to 3000",""],["Wait","",2,"","Wait for 2 secs", ""]]          #test case- ramp signal is first finding
,[["Set","KL15",0,"","Set KL15 to 0",""],["Wait","",2,"Wait for 2 secs", ""]]
,[["Set","Speed",10,"rpm","Set speed to 10",""], ["Set","IGBTtemp",-10,"DegC","Set IGBT temp to 10"],["Set","Vbatt",12,"V","Set Vbatt to 12",""],["Wait","",2,"Wait for 2 secs", ""]]  
,[["Ramp","StatorTemp",[20,100,20], "DegC", "Ramp stator temp from 20 to 100 in 20 ",1 ],["Set","coolanttemp",-20,"DegC","Set coolant temp to 20",""],["Set","Speed",30,"rpm","Set speed to 30",""],["Wait","",2,"Wait for 2 secs", ""]]  # resolved: limitation that last action should not be new signal
,[["Set","Rotortemp",100,"DegC","Set rotor temp to 100", ""], ["Set","IGBTtemp",20,"DegC","Set IGBT temp to 10"], ["Set","coolanttemp",20,"DegC","Set coolant temp to 20",""],["Wait","",2,"Wait for 2 secs", ""]]     
,[["Set","Flowrate",10,"L/min","Set Flowrate to 10",""],["Wait","",2,"Wait for 2 secs", ""]]
,[["Set","coolantrate",50,"L/min","Set coolantrate to 50",""],["Wait","",2,"Wait for 2 secs", ""]]
,[["Set","rate",15,"L/min","Set coolantrate to 50",""],["Wait","",2,"Wait for 2 secs", ""]]
,[["Set","coolavxxcvntrate",50,"L/min","Set coolantrate to 50",""],["Wait","",2,"Wait for 2 secs", ""]]
,[["Set","raxvxcvcte",15,"L/min","Set coolantrate to 50",""],["Wait","",2,"Wait for 2 secs", ""]]]
'''
#['Ramp', 'HV_Bench_Battery_Voltage.abc', '700,750,10', '', '', 0.2]


'''
inputdata=[["Set", "KL30",1, "","Set KL30 to 1", ""],["Set","KL15",1, "","Set KL15 to 1", ""],["Wait","",3,"","Wait for 3 secs", ""]]
[["Set", "HVDC",380,"V","Set HVDC to 380",""],["Set","MO_EM1_SollModus",0,"","Set Mo_EM1 Sollmodus to 0",""],["Wait","",6,"Wait for 6 secs", ""]]
[["Set","MO_EM1_SollModus",1,"","Set Mo_EM1Sollmodus to 1",""],["Ramp","SOLLMOMENT",[0,100,20],"Nm","Ramp Sollmoment from 0 to 100 in 20",1],["Wait","",3,"Wait for 3 secs", ""]]
[["Set","MO_EM1_SollModus",0,"","Set Mo_EM1Sollmodus to 0",""],["Set", "KL15",0,"","Set KL15 to 0", ""],["Wait","",3,"","Wait for 3 secs", ""]]
[["Set","SOLLMOMENT",-100,"Nm","set sollmoment to -100",""],["Wait","",1,"","Wait for 1 secs", ""]]
'''
subplotsWaveform.Plot_Data("trqcntrl","T.1",inputdata) 
#ScrollWaveformplot.Plot_Data("trqcntrl","T.1",inputdata)  # to get the scroll bar in the 1D waveform 
