import pandas as pd
df = pd.read_csv(u'test_V2.csv', encoding='gbk')
outfile = df[(df[u'matchType']=='solo')]
outfile.to_csv('test_solo.csv', index=False, encoding='gbk')
