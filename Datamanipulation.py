import math
import GlobalVar as G

'''
G.Actions[0]=[["Set", "KL30",1, "","Set KL30 to 1", ""],["Set","KL15",1, "","Set KL15 to 1", ""],["Wait","",3,"","Wait for 3 secs", ""]]
G.Actions[1]=[["Set", "HVDC",380,"V","Set HVDC to 380",""],["Wait","",3,"","Wait for 3 secs", ""],["Set","MO_EM1_SollModus",1,"","Set Mo_EM1 Sollmodus to 1",""],["Wait","",3,"Wait for 3 secs", ""]]
G.Actions[2]=[["Set","MO_EM1_SollModus",0,"","Set Mo_EM1Sollmodus to 0",""],["Wait","",3,"Wait for 3 secs", ""]]
G.Actions[3]=[["Set","MO_EM1_SollModus",1,"","Set Mo_EM1Sollmodus to 1",""],["Set", "KL15",0,"","Set KL15 to 0", ""],["Set","Rotortemp",50,"DegC","Set rotor temp to 50",""] ,["Wait","",3,"","Wait for 3 secs", ""]]
G.Actions[4]=[["Ramp","SOLLMOMENT",[-40,100,20],"Nm","Ramp Sollmoment from 0 to 100 in 20",1], ["Wait","",2,"","Wait for 2 secs", ""],["Set","MOMENT",3000,"Nm","set moment to 3000",""],["Wait","",2,"","Wait for 2 secs", ""]]          #test case- ramp signal is first finding
G.Actions[5]=[["Set","KL15",0,"","Set KL15 to 0",""],["Wait","",2,"Wait for 2 secs", ""]]
G.Actions[6]=[["Set","Speed",10,"rpm","Set speed to 10",""], ["Set","IGBTtemp",-10,"DegC","Set IGBT temp to 10"],["Set","Vbatt",12,"V","Set Vbatt to 12",""],["Wait","",2,"Wait for 2 secs", ""]]  
G.Actions[7]=[["Ramp","StatorTemp",[20,100,20], "DegC", "Ramp stator temp from 20 to 100 in 20 ",1 ],["Set","coolanttemp",-20,"DegC","Set coolant temp to 20",""],["Set","Speed",30,"rpm","Set speed to 30",""],["Wait","",2,"Wait for 2 secs", ""]]  # resolved: limitation that last action should not be new signal
G.Actions[8]=[["Set","Rotortemp",100,"DegC","Set rotor temp to 100", ""], ["Set","IGBTtemp",20,"DegC","Set IGBT temp to 10"], ["Set","coolanttemp",20,"DegC","Set coolant temp to 20",""],["Wait","",2,"Wait for 2 secs", ""]]     
.Actions[9]=[["Set","Flowrate",10,"L/min","Set Flowrate to 10",""],["Wait","",2,"Wait for 2 secs", ""]]
#G.Actions[10]=[["Set","coolantrate",50,"L/min","Set coolantrate to 50",""],["Wait","",2,"Wait for 2 secs", ""]]
#G.Actions[11]=[["Set","rate",15,"L/min","Set coolantrate to 50",""],["Wait","",2,"Wait for 2 secs", ""]]
#G.Actions[12]=[["Set","coolavxxcvntrate",50,"L/min","Set coolantrate to 50",""],["Wait","",2,"Wait for 2 secs", ""]]
#G.Actions[13]=[["Set","raxvxcvcte",15,"L/min","Set coolantrate to 50",""],["Wait","",2,"Wait for 2 secs", ""]]
'''
#['Ramp', 'HV_Bench_Battery_Voltage.abc', '700,750,10', '', '', 0.2]

'''
G.Actions[0]=[['Set', 'KL15', 1.0, '', '', ''], ['Wait', '', 1.0, '', '', '']]
G.Actions[1]=[['Set', 'KL30', 0.0, '', '', ''], ['Wait', '', 1.0, '', '', '']]
G.Actions[2]=[['Set', 'KL15', 1.0, '', '', ''], ['Wait', '', 1.0, '', '', '']]


G.Actions[0]=[["Set", "KL30",1, "","Set KL30 to 1", ""],["Set","KL15",1, "","Set KL15 to 1", ""],["Wait","",3,"","Wait for 3 secs", ""]]
G.Actions[1]=[["Set", "HVDC",380,"V","Set HVDC to 380",""],["Set","MO_EM1_SollModus",0,"","Set Mo_EM1 Sollmodus to 0",""],["Wait","",6,"Wait for 6 secs", ""]]
G.Actions[2]=[["Set","MO_EM1_SollModus",1,"","Set Mo_EM1Sollmodus to 1",""],["Ramp","SOLLMOMENT",[0,100,20],"Nm","Ramp Sollmoment from 0 to 100 in 20",1],["Wait","",3,"Wait for 3 secs", ""]]
G.Actions[3]=[["Set","MO_EM1_SollModus",0,"","Set Mo_EM1Sollmodus to 0",""],["Set", "KL15",0,"","Set KL15 to 0", ""],["Wait","",3,"","Wait for 3 secs", ""]]
G.Actions[4]=[["Set","SOLLMOMENT",-100,"Nm","set sollmoment to -100",""],["Wait","",1,"","Wait for 1 secs", ""]]
'''

'''Find_Signal_Params function is used to find units, names of G.Signals and indices of G.Signals in G.Actions'''
def Find_Signal_Params():

    for i in range(0,G.No_Actions):                                            # i - changes G.Actions
        for j in range(0,len(G.Actions[i])):                                   # j - changes elements in the corresponding Action
            G.Action_Indices.append([i,j])                                     # G.stores the index of elements in action as a list    G.Action_Indices= [ [0,0],[0,1]], [1,0],[1,1],...]  all G.Actions in single list [1: ]                               
            if G.Actions[i][j][0]== "Set" or G.Actions[i][j][0]== "Ramp"  :      #brackets also effect the result
                not_in_list= G.Actions[i][j][1] not in G.Signal_Names
                if not_in_list== True:                    
                    G.Signal_Names.append(G.Actions[i][j][1])
                    if G.Actions[i][j][3] != "":
                        #print(G.Actions[i][j][3])
                        G.Signal_Units.append("("+ G.Actions[i][j][3]+")")
                    else:
                        G.Signal_Units.append(G.Actions[i][j][3])
            if G.Actions[i][j][0]== "Ramp":
                G.Actions[i][j][2]= G.Actions[i][j][2].split(",")
                G.Actions[i][j][2]=list(map(int,G.Actions[i][j][2]))
            
    G.No_Signals=len(G.Signal_Names)    


def Find_ramp_yticks():

    for i in range(0,G.No_Actions):           # i - changes G.Actions
        for j in range(0,len(G.Actions[i])):  # j - changes elements in Action
            if G.Actions[i][j][0]== "Ramp":
                ytemp=[]
                for m in range(G.Actions[i][j][2][0],G.Actions[i][j][2][1],G.Actions[i][j][2][2]):
                    ytemp.append(m)
                G.Ramp_Signal_yticks[G.Actions[i][j][1]]=ytemp

#Find_ramp_yticks()                          #(G.Ramp_Signal_yticks)---> for ramp rate of 1/s [1,2,3,4,5]


def Action_Waitlist(LW):                       #LW argumeent takes  the nested list which we will convert to simple list

    for i in range(0,len(LW)):
        if type(LW[i]) is list:
            #for k in range(0,len(G.list_Wait[i])):
            Action_Waitlist(LW[i])
        else:
             G.Wait.append(LW[i])
             if i==(len(LW)-1) :
                 break
#print(Wait)                                 eg:- Wait=[3,0.1,.01,0.1,3,2,1,2]



''' Classify_G.Actions function --> G.Actions are classified based on wait times in each action, nested wait list of G.list_Wait is created'''
def Classify_Actions():
    for i in range(0,G.No_Actions):           # i - changes G.Actions
        r=[]
        for j in range(0,len(G.Actions[i])):  # j - changes elements in Action    
          if G.Actions[i][j][0]== "Wait":
            #print(j)
            r.append((G.Actions[i][j][2]))
           
          if G.Actions[i][j][0]=="Ramp":
              t=math.floor((G.Actions[i][j][2][1]-G.Actions[i][j][2][0])/(G.Actions[i][j][2][2]))
              #q=[G.Actions[i][j][5] for m in range(0,t)]
              r.append([G.Actions[i][j][5] for m in range(0,t)])
          if j==(len(G.Actions[i])-1):
                if len(r)==1:
                    G.list_Wait.extend(r)
                else:
                    G.list_Wait.append(r)
    Action_Waitlist(G.list_Wait)
                        

def Find_Signal_Indices():                                                   # function to find signal indices 

    G.Signal_Indices=[ {} for i in range(0,G.No_Signals)]                     #G.stores the all the indices of G.Signals in all G.Actions  Eg:- {"KL15" :[[0,1],[2,2]]}

    G.Signals=[ {} for i in range(0,G.No_Signals)]               # Final Signal Data format required for plotting    Eg: G.Signals[1] = { KL15: [ [3,1], [3,0],[2,0]] }
    for k in range(0,G.No_Signals):
        G.Signals[k][G.Signal_Names[k]]=[]                       #intializing the dictionary with keys as Signal names and values as empty list

    G.store=[ [] for i in range(G.No_Signals)]                
    
    for k in range(0,G.No_Signals):
        G.Signal_Indices[k][G.Signal_Names[k]]=[]                            #intializing the dictionary with keys as Signal names and values as empty list
 
    for i in range(0,G.No_Actions):         # i - changes G.Actions
        for j in range(0,len(G.Actions[i])):  # j - changes elements in Action
            for k in range(0,G.No_Signals):
                
                if(G.Actions[i][j][1] is list((G.Signal_Indices[k].keys()))[0]):
                    G.Signal_Indices[k][G.Actions[i][j][1]].append([i,j])            

   
def Create_Signal_Data(a,b,c):                           # a- first indices of a signal found in a action, b- next indices found in a action  c- Signal number

    for m in range(0,len(G.Action_Indices)):               # len(G.Action_Indices) != len( G.Actions)   ; G.Action_Indices= [ [0,0],[0,1]], [1,0],[1,1],[1,2], [2,0]...]
        if G.Action_Indices[m]== a:
            lower_index=m
        if G.Action_Indices[m]==b:
            upper_index=m
  
    if G.Actions[a[0]][a[1]][0]  == "Set":
        for k in range(lower_index,upper_index+1):      
            if G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][0] == "Wait" :
                G.store[c].append([G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][2],  G.Actions[a[0]][a[1]][2]])

            if G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][0] == "Ramp" and G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][1] != G.Actions[a[0]][a[1]][1] :
                steps= math.floor((G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][2][1]- G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][2][0])//(G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][2][2]))
                #print(steps)  ----> G.stores the no of times signal is ramped 
                for h in range(0,steps):
                    G.store[c].append([G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][5],G.Actions[a[0]][a[1]][2]])
    
    if G.Actions[a[0]][a[1]][0]  == "Ramp" :
        
        lower_value=G.Actions[a[0]][a[1]][2][0]
        upper_value=G.Actions[a[0]][a[1]][2][1]
        ramp_value= G.Actions[a[0]][a[1]][2][2]                                                     # Eg:- ramp rate is 20 units/sec then ramp value is 20 
        rate=G.Actions[a[0]][a[1]][5]                                                               # 5th element represents the step value time

        for m in range(lower_value,upper_value,ramp_value):
            G.store[c].append([rate, m])                                                               # ramp signal data,
                    
        for k in range(lower_index+1,upper_index+1): 
            if G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][0] == "Wait" :
                G.store[c].append([G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][2], upper_value])

            if G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][0] == "Ramp":           # this might need modification look 
                steps= math.floor((G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][2][1]- G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][2][0])//(G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][2][2]))
    
                for h in range(0,steps):
                    G.store[c].append([G.Actions[G.Action_Indices[k][0]][G.Action_Indices[k][1]][5],upper_value])
                 
    G.Signals[c][G.Signal_Names[c]]=G.store[c]
    
'''function to pass the signal indices to create data function and call it'''
def Pass_SignalIndices_Fun():

    for i in range(G.No_Signals):                                           # i--changes action in indices
              for j in range(0,len(list(G.Signal_Indices[i].values())[0] )):  # j - changes elements in indices of action
                  if j== (len(list(G.Signal_Indices[i].values())[0])-1):      # to check if the indices are the last element for the signal
                      Create_Signal_Data(list(G.Signal_Indices[i].values())[0][j], [G.No_Actions-1,len(G.Actions[G.No_Actions-1])-1],i)
                  else:
                      #print(list(G.Signal_Indices[i].values()))
                      Create_Signal_Data(list(G.Signal_Indices[i].values())[0][j], list(G.Signal_Indices[i].values())[0][j+1],i)


def Generate_Data(InputData):      # uncomment this line
    
    G.Actions=[[] for k in range(len(InputData))]
    for i in range(0,len(InputData)):
        G.Actions[i]=InputData[i]
    G.No_Actions= len(G.Actions)   
    G.Data_Init()
    Find_Signal_Params()
    Find_ramp_yticks()
    Classify_Actions()
    Find_Signal_Indices()
    Pass_SignalIndices_Fun()
  

