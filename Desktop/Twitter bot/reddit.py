import praw

reddit = praw.Reddit(client_id = 'lraxb47ZSIGEAw',
					 client_secret = '4a14MpFNTdPrCwc4yMsAEHnxJqM',
					 username = 'jmschu3',
					 password = '3A119df372',
					 user_agent = 'cryptoBot')


subreddit = reddit.subreddit('Stellar')

hot_keyword = subreddit.top(limit=2000)
 
count = 0
for submission in hot_keyword:
	if not submission.stickied:
		count += 1
		if(submission.title.find("partner", 0, len(submission.title)) > 1):
			print(submission.title)
			# print('Title: {}, ups: {}'.format(submission.title, submission.ups))
	print(count)