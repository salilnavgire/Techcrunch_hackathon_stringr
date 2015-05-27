We used SoundCloud API to get user_id for each artist and their tracks. The final score for each artist is calculated based on avg sentiment of eachtracks, number of followers and the number of tracks uploaded. The json dump for each artist is being regularily indexed in Elasticsearch. Final script creates a REST api using Flask library and then uses ngrok to create a secure tunnel to that localhost. Message script sends a message to the user if he gets a match.

User dictionary is stored in Elasticsearch as follows
users:userid{
	username:
	full_name:
	countrty:
	city:
	track_count:
	playlist_count:
	followers_count:
	public_favorite_count:
	tags_list:
	genres_max:
	top_stream_urls:
	num_favorites:
	avg_sentiment:
	score:
}

Most of my work is in Ipython Notebooks, but i'll clean this repo and add scripts as and when I get free time.
