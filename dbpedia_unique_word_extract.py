import os
import urllib2
import re
import urllib

def word_check(text,val):
	#print str(text)
	for data in text:	
		text_data = data.strip()
		text_data = text_data.lower()
		#text_data = re.sub(r'\W+', '', text_data)
		if text_data in single_list:
			single_list[text_data].append(val)
		else:
			single_list[text_data] = [val]
			#print text_data

def word_name_check(name,val):
	text_data = name	
	if text_data in word_list:
		#word_list[text_data] += 1
		pass
	else:
		word_list[text_data] = val
		#print text_data

docs = {}
word_list = {}
single_list = {}

## Name of your dbpedia dataset goes here
with open('long_abstracts_en.nt.nt') as fin:
## Output data goes here - This is individual article name
	with open('unique_wiki_names.txt',"w") as fout:
## This is individual words extracted from article names
		with open('unique_words.txt',"w") as fout2:
			id_v = 1
			for line in fin:
				str_line_n = line
				ab = str_line_n.split(' ')
				res_id = ab[0]
				final_name = res_id.replace('<http://dbpedia.org/resource/','').replace('>','').replace('_',' ')
				final_name = final_name.strip()
				final_name = urllib.unquote(final_name)
				final_name.replace("(","").replace(")","").replace(",","")
				"""a_alt_short = str_line_n.split('"')
				pre_remove = a_alt_short[0]
				new_abs = str_line_n.replace(pre_remove,'')
				newer_abs = new_abs.replace('"','')
				abstract = newer_abs.replace('@en .','').replace(',',' ').replace('(','').replace(')','').replace('.',' ').lower()
				tokens = nltk.word_tokenize(abstract)
				text = nltk.Text(tokens)"""
				word_name_check(final_name.lower(),id_v)
				final_key = final_name.split(" ")
				word_check(final_key,id_v)
				id_v = id_v+1
				print str(id_v)+" : "+final_name
				#print "Size: "+str(len(word_list))

			for key,value in word_list.iteritems():
				fout.write(key+":"+str(value)+'\n')
			for key,value in single_list.iteritems():
				fout2.write(key+":"+str(value)+'\n')

	
	
