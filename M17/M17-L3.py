#M17-L3
#Задание 2.4 (External resource)


import pandas as pd

def create_medications(names, counts):    
    return pd.Series(index=names, data=counts)

def get_percent(medications, name):
    '''
    All_C - 100%
    namec_C - ?
    namec_C * 100 / AllC
    '''
    #return medications[name]
    #print(sum(medications.values))
    #print(medications[name]*100/sum(medications.values))
    return medications[name]*100/sum(medications.values)


names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]
medications = create_medications(names, counts)
print(get_percent(medications, "chlorhexidine")) 
#37.5