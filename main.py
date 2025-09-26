import random

quote_list = ["So many books, so little time.", "You only live once, but if you do it right, once is enough.",
              "Always forgive your enemies; nothing annoys them so much.", "A friend is someone who knows all about you and still loves you.", "O sinner, be not discouraged, but have recourse to Mary in all you necessities. Call her to your assistance, for such is the divine Will that she should help in every kind of necessity.", "If you invoke the blessed Virgin when you are tempted, she will come at once to your help, and Satan will leave you."]

print()
print("Firstly, would you like to add your own quote to the list? (Y/N) ")

str = input()
if str.lower() == "y":
    print("Please enter your quote fully:")
    new_quote = input()
    with open("user_input_quotes.txt", "a") as f:
        f.write(new_quote)
        f.write("\n")

with open("user_input_quotes.txt", "r") as file:
    for line in file:
        quote_list.append(line.strip())

print()
print("Here is the randomly chosen quote:")

index = random.randrange(len(quote_list))

prit(quote_list[index])
