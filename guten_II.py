from nltk import ngrams

numbs = [2,3,4,5]

for num in numbs:
  known_words = {}
  with open("gutenberg.txt", encoding='utf-8') as f:
    contents = f.readlines()
    for line in contents:
        line = line.strip()
        xgrams = ngrams(line.split(), num)
        for grams in xgrams:
          # print(grams)
          for line in grams:
            words = line.split()
            for word in words:
              known_words[word] = known_words.get(word, 0) + 1

  known_words = dict(sorted(known_words.items(), key=lambda item: item[1]))
  items = list(reversed(known_words.items()))[:10]
  print(f"N-grams length: {num}")
  print(f"{items} \n")

