#ProgAssign_Prob1
import pandas as pd
math_data = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
elec_data = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
geas_data = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
esat_data = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
math = pd.DataFrame(math_data,columns = ['Student','Math'])
electronics = pd.DataFrame(elec_data,columns = ['Student','Electronics'])
geas =  pd.DataFrame(geas_data,columns = ['Student','GEAS'])
esat = pd.DataFrame(esat_data,columns = ['Student','ESAT'])
combi = pd.merge(pd.merge(math,electronics,how = 'left', on = 'Student'),
                 pd.merge(geas,esat,how ='left', on ='Student'))
#Converting from Wide to Long Format
combi_long = pd.melt(combi,id_vars='Student',var_name='Categories',value_name='Grades')
