# # string concatentation (how to put strings together)
# # suppose we want to create a string that says "subscribe to ____"
# youtuber = "random youtuber" #some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
famousPerson = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because\
 I love to {verb1}. Stay hydrated and {verb2} like you are {famousPerson}!"

print(madlib)