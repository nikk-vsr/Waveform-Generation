global Actions
global No_Actions
'''
Actions= [0 for i in range(3)]
Actions[0]=[['Set', 'KL30', 0.0, '', 'Set KL15 to 0', ''], ['Wait', '', 3.0, 's', 'Wait for 3 Sec', ''], ['Set', 'KL15', 1.0, '', 'Set KL15 to 1', ''], ['Wait', '', 3.0, 's', 'Wait for 3 Sec', '']]
Actions[1]=[['Set', 'KL15', 1.0, '', 'Set KL15 to 1', ''], ['Wait', '', 3.0, 's', 'Wait for 3 Second', ''], ['Set', 'MO_EM2_Sollmodus_Switch', 1.0, '', 'Set MO_EM2_Sollmodus_Switch to 1', ''], ['Wait', '', 0.1, 's', 'Wait for 0.1 sec', ''], ['Set', 'MO_EM2_Sollmodus', 1.0, '', 'Set MO_EM2_Sollmodus to 1', ''], ['Ramp', 'HV_Bench_Battery_Voltage.abc', '700,750,10', '', '', 0.2]]
Actions[2]=[['Set', 'TME_EM2_IstVolumenstrom', 10.0, '', 'Set TME_EM2_IstVolumenstrom to 10 ', ''], ['Wait', '', 2.0, 's', 'Wait for 2 second', ''], ['Set', 'TME_EM2_IstVolumenstrom', 50.0, '', 'Set TME_EM2_IstVolumenstrom to 50', ''], ['Wait', '', 2.0, 's', 'Wait for 2 second', '']]
No_Actions=len(Actions)
'''
def Data_Init():
    global Action_Indices,list_Wait,Signal_Names,Signal_Units,Ramp_Signal_yticks,No_Signals,Wait,Signal_Indices,Signals,store
    Action_Indices=[]                           #stores the indices of each element in actions
    list_Wait=[]                                #Stores the wait time with each action as a element   
    Signal_Names=[]                             # Contains the list of Signal names present in the test case
    Signal_Units=[]                             # Stores the signal units corresponding to signal name in the test case
    Ramp_Signal_yticks={} 
    No_Signals=0
    Wait=[] 
    Signal_Indices=[]
    Signals=[]
    store=[]
    Actions=[]
    No_Actions=0
    
def Plot_Init():
    global Signal_Values,Signals_Segments,Xticks_Wait,Signal_Wait,Rev_CumSum,Concetanated_Segments
    global SignalAction,SignalPendingWait,LC,Colors_List,Color_Index,Grid_Row,Grid_Col
    Signal_Values=[]
    Signals_Segments=[]
    Xticks_Wait=[]
    Signal_Wait=[]
    Rev_CumSum=[]
    Concetanated_Segments=[]
    SignalAction=[]
    SignalPendingWait=[]
    LC=[]
    Colors_List=[]
    Color_Index=[]
    Grid_Row=0
    Grid_Col=0

