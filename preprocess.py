import pandas as pd

df = pd.read_csv("RAW_recipes.csv")

f = open('dataset/emnlp_news.txt', 'w')
for i in range(5000):
	line = df['steps'][i][2:-2].split("', '")
	line = ' , '.join(line) + '\n'
	f.write(line)

f = open('dataset/testdata/emnlp_news_test.txt', 'w')
for i in range(5000, 7500):
	line = df['steps'][i][2:-2].split("', '")
	line = ' , '.join(line) + '\n'
	f.write(line)