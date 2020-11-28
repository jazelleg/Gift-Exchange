import random

gifters = input("Please enter the names of everyone involved, with the names seperated by a comma:\n")

gift_giver = gifters.split(",")

gift_rec = gift_giver.copy()

num_gifters = len(gift_rec)

for name in gift_giver:
      selector = random.randint(0, num_gifters - 1)
      gift_rec_select = gift_rec[selector]
      gift_giver_select = name
      if gift_rec_select == gift_giver_select:
        print("You can't gift yourself!")
      else:
        print(f"{gift_giver_select} will give a gift to {gift_rec_select}")

        gift_rec.remove(gift_rec_select)
        num_gifters = len(gift_rec)
