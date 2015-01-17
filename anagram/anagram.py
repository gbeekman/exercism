def detect_anagrams(case_word, test_words):

	ana_list = test_words

	for i in range(len(test_words)):
		case_list = list(case_word)
		if len(case_word)!=len(test_words[i]):
			ana_list.pop([i])

		else:
			test_list = list(test_words[i])
			for x in test_list:
				if x in case_list:
					case_list.remove(x)
				else:
					ana_list.pop([i])
					break

	return ana_list


