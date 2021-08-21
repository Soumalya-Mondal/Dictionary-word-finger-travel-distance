import json
import csv
import pandas as pd

def found_distance(a_word):
	distance_word=new_word.get(a_word)
	#print(f'for word {a_word} distance is= {distance_word}')
	return distance_word

def GETKey(val):
	for key, value in word_dict.items():
		if val== value:
			return key


with open('word_distance.txt','r') as df:
	line= df.readlines()

new_word={}
for word in line:
	words=word.replace('|','').replace(' ','').replace('\n','').replace('mm','').split('=')
	new_word[f'{words[0]}']=float(f'{words[1]}')

#print(new_word.get('SO'))
#print(new_word)

with open('dict_word_final-distance.csv','a', newline='') as csvf:
	writer= csv.writer(csvf)

	with open('word_dict.json', 'r') as jf:
		data=json.loads(jf.read())
		for i in data:
			if len(i) > 1:
				#print(i)
				main_final_distance=0
				csv_write_row=[]

				for j in range(0,len(i)-1):
					new_string= i[j]+i[j+1]
					modified_string="'"+new_string+"'"
					final_distance=found_distance(new_string.upper())
					if final_distance==None:
						pass
					else:
						main_final_distance+=final_distance

				#print(f'for word "{i}" total travel distance is= {main_final_distance:.2f}')
				csv_write_row.append(i)
				csv_write_row.append(f'{main_final_distance:.2f}')
				#print(csv_write_row)
				writer.writerow(csv_write_row)
			else:
				continue

word_dict= pd.read_csv('dict_word_final-distance.csv', header=None, index_col=0, squeeze=True).to_dict()
#print(word_dict)

with open('dict_word_final-distance.csv','r') as readf:
	reader= csv.reader(readf)
	word_length=[]

	for row in reader:
		#print(row[1])
		word_length.append(float(row[1]))
	maximum=max(word_length)
	#print(GETKey(maximum))
	minimum= min(word_length)
	
	print(f'for word "{GETKey(maximum)}" the maximum travel distance is= {maximum}')

	print(f'for word "{GETKey(minimum)}" the minimum travel distance is= {minimum}')