import pandas as pd
df = pd.read_csv(u'test_V2.csv', encoding='gbk')
outfile = df[(df[u'matchType']=='solo')]
outfile.to_csv('solo_test.csv', index=False, encoding='gbk')
