import pandas as pd

df = pd.read_csv("RAW_recipes.csv")

f = open('dataset/emnlp_news.txt', 'w')
for i in range(1000):
	line = df['steps'][i][2:-2].split("', '")
	line = ' , '.join(line) + '\n'
	f.write(line)

f = open('dataset/testdata/emnlp_news_text.txt', 'w')
for i in range(1000, 1500):
	line = df['steps'][i][2:-2].split("', '")
	line = ' , '.join(line) + '\n'
	f.write(line)