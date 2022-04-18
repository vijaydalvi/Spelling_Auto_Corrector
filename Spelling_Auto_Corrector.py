from textblob import TextBlob
words=input("Enter Any Word:-")
print("Worng Words:-",words)
correct=TextBlob(words)
print("Correct Words",correct.correct())