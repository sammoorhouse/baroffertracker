import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from messages.localOffers import Offer as OfferMessage
from messages.localOffers import Venue as VenueMessage
from messages.localOffers import LocalOffersRequest, LocalOffersResponse

@endpoints.api(name='baroffertracker',version='v1',
	description='Bar Offer Tracker API')
class BarOfferTrackerApi(remote.Service):
	
	@endpoints.method(LocalOffersRequest,
					  LocalOffersResponse,
					  name='BarOfferTracker.getLocalOffers')
	def getLocalOffers(self, request):
		location = request.location
		
		venue = VenueMessage(name="Sam's bar", address="sample venue address")
		offer = OfferMessage(description='two for one stella', venue = venue)
		return LocalOffersResponse(offers = [offer])

	@endpoints.method(AcceptOfferRequest,
					AcceptOfferResponse,
					name='BarOfferTracker.acceptOffer')
	def acceptOffer(self, request):
		offerKey = request.offerKey
		
	@endpoints.method(AcceptedOffersRequest,
						  AcceptedOffersResponse,
						  name='BarOfferTracker.getAcceptedOffers')
	def getAcceptedOffers(self, request):
				  
application = endpoints.api_server([BarOfferTrackerApi])