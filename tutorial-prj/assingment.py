def common_character(name_staring):
	# Initially start with cleansing the string and removing white space character
	new_str = name_staring.replace(' ','')
	counter_str_in= 0
	word_letter =''
	for eachword in new_str:
		count_word= 0
		count_word = new_str.count(eachword)
		if counter_str_in < count_word:
			counter_str_in = count_word
			word_letter = eachword
		elif counter_str_in == count_word:
			 counter_str_in = count_word
			 word_letter =  eachword
	return word_letter.lower()

sting = ('Why do I love python sOOOOO much')
x = common_character(sting)
print(x)