df_10w=pd.read_csv('/Users/chenpengyao/Desktop/HKUST/BDT/MSBD_5001_Foundation_of_DA/Group_Project/yelp_dataset/combination_10w_1.csv')
df_10w=pd.concat([df_10w.iloc[:,0:5],df_10w.iloc[:,-2:]],axis=1)

def score(df):
	def f(a,topic):
		for word in subtopics[topic]:
			if word in a:
				return '1'
			break
	score_list = []
	for topic in subtopics.keys():
		df[topic]=df['text'].apply(f,args=(topic,))
		print('Once Topic')
		df_1 = df[df[topic] == '1']
		score_list.append((topic,round(df_1['stars_y'].mean(),2)))
	#score_list.append(np.percentile(df_1['stars_y'], [25, 50, 75])[2])
	return df,score_list


df,score_list=score(df_10w)

#score_list=score_subtopices(df_10w)
#score_list_y=score_subtopices(df_10w)

#选中一个作为测试：
#5,2384,4482
#print(df_10w['business_id'][5])
df_test=df_10w[df_10w['business_id']==df_10w['business_id'][4482]] #作测试集
df_test,score_test=score(df_test)
print(score_test)
#print(df_test[df_test['environment']=='1']['stars_y'].mean())
#print(df_10w['stars_x'].mean())

#score_test=score_subtopices(df_test)
#Final standard score in restaurant
score_restaurant=[3.7, 3.53, 3.64, 3.55, 3.81, 3.71, 3.64, 4.1]
print(score_list)
print(score_test)
score_testlist=[]
for i in score_test:
	score_testlist.append(i[1])
print(score_testlist)

