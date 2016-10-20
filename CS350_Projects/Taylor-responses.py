"""Taylor Herrera"""
#Version Python 3 


import random


class talker:
	def __init__(self,n, v):
		self.name = n
		self.vocab = v
		
	def get_name(self):
		return self.name
		

	def get_vocab(self):
		return self.vocab
	
	
	
def main():
	t_responses = ["EXCUSE ME! NO!"]*11
	t_responses[hash("r1")%10] = "If they overturned it, it will go back to the states."
	t_responses[hash("r2")%10] = "I think I should respond to that."
	t_responses[hash("r3")%10] = "Nobody knows about it, nobody talks about it."
	t_responses[hash("r4")%10] = "You're the puppet!"
	t_responses[hash("r5")%10] = "Yeah, I doubt it. I doubt it."
	t_responses[hash("r6")%10] = "Yes, that's fine."
	t_responses[hash("r7")%10] = "Wrong."
	t_responses[hash("r8")%10] = "This is just another lie."
	t_responses[hash("r9")%10] = "And that will be as bad as NAFTA."
	t_responses[hash("r10")%10] = "Well, let me just say -- let me just say."
	t_responses[hash("r11")%10] = "I built a massive company, a great company, some of the greatest assets anywhere in the world, worth many, many billions of dollars."
	
	
	t_len = len(t_responses)	
	
	h_responses = ["Well, it is an open discussion."]*11
	h_responses[hash("r1")%10] = "Well, you know..."
	h_responses[hash("r2")%10] = "... it just shows you're not up to doing the job."
	h_responses[hash("r3")%10] = "He has consistently denied what is..."
	h_responses[hash("r4")%10] = "I pay for everything I'm proposing. "
	h_responses[hash("r5")%10] = "I started off with -- my dad was a small-business man."
	h_responses[hash("r6")%10] = "You should meet with some of the women that I have met with, women I have known over the course of my life."
	h_responses[hash("r7")%10] = "I think it's an idea that would rip our country apart."
	h_responses[hash("r8")%10] = "I voted for border security,."
	h_responses[hash("r9")%10] = "There are some limited places where that was appropriate"
	h_responses[hash("r10")%10] = "I want to get everybody out of the shadows"
	h_responses[hash("r11")%10] = "Well, if you went on to read the rest of the sentence, I was talking about energy."
	
	h_len = len(h_responses)	
	
	
	
	
	while 1:

		choice = input("Who would you like to talk first? (Hillary or Trump) **case sensitive**: ")
		
		if choice == "Trump":
			ask = input("What would you like to ask? ")
			trump = talker("Trump", t_responses[random.randint(0,t_len)])
			print("\nThe speaker is: ",trump.get_name(),"\n")
			print(trump.get_name(),"says: ",trump.get_vocab(),"\n")

		
		if choice == "Hillary":
			ask = input("What would you like to ask? ")
			hillary = talker("Hillary", h_responses[random.randint(0,h_len)])
			print("\nThe speaker is: ",hillary.get_name(),"\n")
			print(hillary.get_name(),"says: ",hillary.get_vocab(),"\n")
		

	
	
	
	

if __name__ == "__main__":
	main()


