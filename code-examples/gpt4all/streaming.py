from gpt4all import GPT4All

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# create an empty  string for our reply
response = ""

# choose a word to catch
word_to_catch = "pirate"

for word in model.generate("What are some good improv exercises?", streaming=True):
    # get out of the loop here if we've found the word we don't want
    if word_to_catch in word:
        break

    # add the word to our response if it doesn't match the word to catch
    response += word
    print(word)

print(response)