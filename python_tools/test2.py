import pandas as pd

data = pd.read_excel('input/full_hid25_re_f1.xlsx', sheetname=0,index_col=0, header=1)
print(data)

writer = pd.ExcelWriter('input/test_write.xlsx', engine='xlsxwriter')
worksheet = writer.sheets['Sheet2']
worksheet.write(data)
writer.save()