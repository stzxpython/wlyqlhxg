import pandas as pd
#df_5 = pd.read_excel('DRESSTK_2016__C8645011F84_(1).xls')
#df_6 = pd.read_excel('DRESSTK_2016__614ABC84CE2_(2).xls')
#
#
#df = pd.concat([df_5,df_6],axis = 0)
#
#
#lis = ['2017-01-26','2017-02-28','2017-03-31','2017-04-28','2017-05-31','2017-06-30','2017-07-31','2017-08-31','2017-09-29','2017-10-31','2017-11-30','2017-12-29']
#
#
#df_0 = pd.DataFrame([],columns = df.columns)
#for i in lis:
#    df_ = df[df['日期_Date'] == i]
#    df_0 = pd.concat([df_0,df_],axis = 0)
#
#df_0.to_excel('yz.xls')



df = pd.read_excel('yz.xls')


def xxx(x):
    if x[5:7] == '01':
        return 1
    elif x[5:7] == '02':
        return 2
    elif x[5:7] == '03':
        return 3
    elif x[5:7] == '04':
        return 4
    elif x[5:7] == '05':
        return 5
    elif x[5:7] == '06':
        return 6
    elif x[5:7] == '07':
        return 7
    elif x[5:7] == '08':
        return 8
    elif x[5:7] == '09':
        return 9
    elif x[5:7] == '10':
        return 10
    elif x[5:7] == '11':
        return 11
    elif x[5:7] == '12':
        return 12
df['日期_Date'] = df['日期_Date'].astype('str')
df['日期_Date'] = df['日期_Date'].apply(lambda x: xxx(x))
df.to_excel('yz_1.xls')