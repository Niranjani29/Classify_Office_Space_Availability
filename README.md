# Classify_Office_Space_Availability
Classify whether a given chunk of text describes a commercial establishment that offers office space for rent
I have implemented the simple but effective machine learning technique, naïve Bayes classification, and applying it to a binary text classification task. This task will describe the details of a implementation of a naïve Bayes classifier with the categories 0 and 1.

ra_data_classifier:- 
The actual CSV Data. It contains 3 columns- hid, chunk, has_space.

Training Data and Testing Data: - 
To calculate the accuracy, we need to test the data.
For testing the data, we do not have access data. 
So, I divided the data into training and testing in 70% and 30% respectively. 
Why 70-30%, It is always advisable to keep one third data for training. 
I could have experimented more, but I did not want to put in a lot of time into this.

Text_classification :-
This is the python classifier.
I have created two dictionaries. One, this includes all the words and their occurrences for the rows of class ‘0’ and second, same for class ‘1’ (Dictionaries are: ‘commercial_0’ and ’commercial_1’)
I total words are counted based upon the number of entries in the dictionaries as below. But a set can been created to avoid the duplicate entries.
total_words= set(total_words)

For each word in both the dictionaries, the probability is calculated depending on the total number of words in the respective dictionary as follows:
commercial_0_prob[eachword] = (commercial_0[eachword] + 1.0)/ (words_count_0 + len(total_words))
where, commercial_0_prob[eachword] = dictionary to store the probabilities of each word of class ‘0’
	commercial_0[eachword]	= dictionary of each word with its occurrences of class ‘0’
	words_count_0			= length of dictionary “commercial_0
	len(total_words)		= length of total number of words in both the dictionaries.
Testing data is invoked. 
The probability of each word is calculated in a row and for eachword, the probability is compared between the probability dictionaries of class ‘0’ and class’1’.
An output list is created with the predicted 0’s and 1’s.
This list is then compared with the test list to get the accuracy with the help of accuracy_score() from sklearn.metrics.

Output:
The accuracy came out to be 36.66%. This is a bad accuracy. But given that it had only 100 records, it was training deficit. I still tried to improve.
I have added ‘add-one’ smoothing.
The idea behind Laplacian smoothing, or add-one smoothing, is shifting some probability from seen words to unseen words. In other words, assigning unseen words/phrases some probability of occurring.
I have also considered all the values alphabets, digits, punctuations whereas in task three, I have removed all numbers and the punctuations which has helped my accuracy by 4.0%. I have used the function isalpha() to separate out the string type from numbers.

