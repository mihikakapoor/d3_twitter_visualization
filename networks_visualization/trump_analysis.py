import googlemaps
from random import randint, shuffle
from keys import *
from models import Retweet, Reply, TrumpStatus, Hashtag
import os


# JS to place in the function "getPoints"
# https://developers.google.com/maps/documentation/javascript/examples/layer-heatmap#try-it-yourself
# function getPoints() {
# 	// these are coordinates from location_list_to_coordinate_list
# 	points = [[37.09024, -95.712891], [32.715738, -117.1610838], [32.3546679, -89.3985283], [33.4483771, -112.0740373], [46.1908484, -84.8314496], [34.3916641, -118.542586], [37.6456329, -84.77217019999999], [-23.3044524, -51.1695824], [28.5383355, -81.3792365], [44.3148443, -85.60236429999999], [39.7596061, -121.6219177], [36.0971945, -115.1466648], [36.778261, -119.4179324], [39.9611755, -82.99879419999999]];
#   	listMapPoints = [];
#   	for (var i = 0; i < points.length; i++) {
#   		lat = points[i][0];
#     		lng = points[i][1];
#   		mapPoint = new google.maps.LatLng(lat,lng)
#   		listMapPoints.push(mapPoint);
#  	 }
#   return listMapPoints;
# }

def location_list_to_coordinate_list(location):
	# we only get up to 5,000 calls each day...
	gmaps = googlemaps.Client(key=geocode_api_key)
	with open('hexbin/maga_reply.tsv', 'a') as f:
		if os.stat("hexbin/maga_reply.tsv").st_size == 0:
			f.write('0\t1\tdate\n')
		geocode_results = gmaps.geocode(location[1])

		for gresult in geocode_results:
			lat = gresult['geometry']['location']['lat']
			lng = gresult['geometry']['location']['lng']
			coordinate = [lat, lng]
			f.write(str(lng))
			f.write('\t')
			f.write(str(lat))
			f.write('\t{count}\n'.format(count=location[0]))
			return coordinate

def location_list_to_coordinate_list2(location):
	# we only get up to 5,000 calls each day...
	gmaps = googlemaps.Client(key=geocode_api_key)
	with open('hexbin/sensational2.tsv', 'a') as f:
		if os.stat("hexbin/sensational2.tsv").st_size == 0:
			f.write('0\t1\tdate\n')
		geocode_results = gmaps.geocode(location[1])
		
		for gresult in geocode_results:
			lat = gresult['geometry']['location']['lat']
			lng = gresult['geometry']['location']['lng']
			coordinate = [lat, lng]
			f.write(str(lng))
			f.write('\t')
			f.write(str(lat))
			f.write('\t{count}\n'.format(count=location[2]))
			return coordinate

def location_list_to_coordinate_list3(location, coordinate):
	# we only get up to 5,000 calls each day...
	gmaps = googlemaps.Client(key=geocode_api_key)
	with open('hexbin/itwillchange.tsv', 'a') as f:
		if os.stat("hexbin/itwillchange.tsv").st_size == 0:
			f.write('0\t1\tdate\n')
		coordinate2 = "hello"
		if coordinate is not None:
			f.write(str(coordinate[1]))
			f.write('\t')
			f.write(str(coordinate[0]))
			f.write('\t{count}\n'.format(count=location[0]))
			return coordinate2


def get_reply_locations(trump_status_id):
	locations = []
	count = 0
	for reply in Reply.select().where(Reply.in_reply_to_status_id_str == trump_status_id).order_by(Reply.created_at):
		location = reply.location
		if location:
			locations.append((count, location))
			count += 1
	return locations

def get_retweet_locations(trump_status_id):
	locations = []
	count = 0
	for retweet in Retweet.select().where(Retweet.status_id_of_retweeted_tweet == trump_status_id).order_by(Retweet.created_at):
		location = retweet.location
		if location:
			locations.append((count, location))
			count += 1
	return locations

if __name__ == "__main__":
	# nuclear_tweet_id = '815930688889352192'
	# locations = get_retweet_locations(nuclear_tweet_id)
	# print(len(locations))
	# count = 0
	# while count < 10:
	# 	location = locations[randint(0, len(locations)-1)]
	# 	coordinate = location_list_to_coordinate_list(location)
	# 	if coordinate != None:
	# 		count += 1

	# from sensational import map_inputs
	# count = 0
	# while count < 10:
	# 	location = map_inputs[randint(0, len(map_inputs)-1)]
	# 	coordinate = location_list_to_coordinate_list2(location)
	# 	if coordinate != None:
	# 		count += 1


	# from sensational2 import map_inputs
	# shuffle(map_inputs)
	# for i in range(len(map_inputs)):
	# # for i in range(5):
	# 	location = map_inputs[i]
	# 	coordinate = location_list_to_coordinate_list2(location)
	# 	coordinate2 = location_list_to_coordinate_list3(location, coordinate)
	# 	print(i)

	# tweet_id = '815930688889352192'
	tweet_id = '815930688889352192'
	locations = get_reply_locations(tweet_id)
	shuffle(locations)
	print(len(locations))
	for i in range(len(locations)):
		coordinate = location_list_to_coordinate_list(locations[i])
		print(i)






	# print(coordinates)