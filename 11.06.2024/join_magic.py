names = ["Nai", "Yarin", "Bat"]
seperator = ","
print(names)

joined = seperator.join(names)
print("The names joined into a string:", joined)

word1 = "Hello"
word2 = "World"
word3 = ".This is so sick!"

print("Words joined:", " ".join([word1,word2,word3]))

formatted_string = "Hello {1} {0} {2}".format(word2, "duh", "meh")
print(formatted_string)

cost = 999.99999999
formatted_with_percent = "Hello %s. %s. I cost:%.2f" %(word2, "duh", cost)
print(formatted_with_percent)


