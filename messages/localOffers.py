import endpoints
from protorpc import messages

class Venue(messages.Message):
	name = messages.StringField(1)
	address = messages.StringField(2)

class Offer(messages.Message):
	venue = messages.MessageField(Venue, 1)
	description = messages.StringField(2)

class LocalOffersRequest(messages.Message):
	location = messages.StringField(1, required=True)

class LocalOffersResponse(messages.Message):
	offers = messages.MessageField(Offer, 1, repeated=True)

