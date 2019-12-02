#ProgAssign_Prob2
import pandas as pd
data = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2',],
        'Dimension':['Length','Width','Height','Length','Width','Height'],
        'Value':[6,4,2,5,3,4]}
messy = pd.DataFrame(data,columns=['Box','Dimension','Value'])
tidy = pd.pivot_table(messy,index='Box',columns='Dimension',values='Value').reset_index()
tidy['Volume']=tidy.Length*tidy.Width*tidy.Height
