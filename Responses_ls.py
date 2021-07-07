from datetime import datetime

def sample_responses(input_text):
	user_message = str(input_text).lower()

	# if user_message in ("hello", "hi", "sup"):
	# 	return "Hey! How's it going?"

	# if user_message in ("who are you", "who are you?", "How to buy"):
	if user_message in ("what's the address", "token address", "address"):
		return "kubtc token address: 0x1f884a77ce343d599a139aa03c0305bc5566a84cs"

	# if user_message in ("How to buy", "How to buy?"):
	# 	return "here"	


	#return "I don't understand you."	