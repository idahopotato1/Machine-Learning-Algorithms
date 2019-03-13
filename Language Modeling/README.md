# Language Modeling
Almost all devices around us today have a built in language understanding and generation module as Apple’s Siri, Amazon’s Alexa, Google Assistant ...etc. These applications use machine learning and natural language processing techniques to achieve that goal. One technique that’s heavily used in all of these applications is called “Language Modeling”. Language Modeling is a technique that machines uses to model human languages

## Application
Implementing a simple language called “N-gram” Language Model (N-gram LM). The “N” in N-gram is the number of contextual words considered during training. Words depend on the context they appear in; N is the length of such context. For example, 3-gram LM is the model which restricts itself to context of length equals 3 words, such that each word depends on the previous 2 words, so more generally an n-gram model assumes each word depend on the previous n-1 words. Similar to the text prediction in your phone, the language model should be able to predict one word at a time, generating running text.

## Usage
python3 LM.py [input_file] [k] [length_sentence] [seed_word]

[input_file]: input file for list of sentences to train the model

[k]: type of n-gram model

[length_sentence]: length of sentence to be generated (by words)

[seed_word]: Starting seed word for model to generate sentence


