def the_total_number_of_characters():
    sentence = raw_input("Please enter the sentence")
    sentence_plus = len(sentence) - 280
    sentence_plus2 = 280 -len(sentence)
    if len(sentence) > 280:
        return "The number of characters for this sentence " + str(
            len(sentence)) + " character \nYou can not share this sentence on Twitter \nTo share this sentence, delete " + str(sentence_plus) + " characters"
    if len(sentence) <= 280:
        return "The number of characters for this sentence " + str(len(sentence)) + " Letter \nYou can share this sentence on Twitter \nYou can add " + str(sentence_plus2) + " characters"


print the_total_number_of_characters()