# Reddit Clone

ACCOUNT

Signup with email:
- takes an unique email, password and an unique username 
- creates a new user in the db and stores the password in a hash format
- sends out access and refresh token(JWT) as response

Signup with Social(gmail):
- allows anyone to create a new account using their gmail account
- generates a random username internally for this user 

Login:
- takes username and password as input
- if they match an entry in the users model, then send access and refresh token(JWT) as response

Login with Social(gmail):
- allows logging in with a gmail account
- create a new user if user not present already i.e., generate a random username

Forgot username:
- login needs username and password in reddit
- if username is forgotten, we can use this feature to send out an email to the registered email id with the matching username
- takes an email id as input, sends an email to the same if it matches with an entry in users model, else sends an error response

Forgot password:
- this can be used to reset a password when a password is forgotten, to send out an email with the reset link 
- takes username and email as input, checks if it matches an entry in the users model, if it does, then sends an email with a password reset link,
  else throws error
- the password link itself will have a limited lifespan and once used cannot be used again

List all users:
- creates a master list of sorts for the user model i.e., lists all the users signed up
- gives a paginated response

List followed users:
- lists all the users that is followed by the logged in user
- gives a paginated response

List following users:
- lists all the users that the logged in user is following
- gives a paginated response

List subreddits joined by user:
- lists all the subreddits the logged in user has joined 
- gives a paginated response 



SUBREDDIT

Create a subreddit:
- allows an user to create a subreddit
- takes an unique name, a description and an image for the subreddit 
- creates a new subreddit

Edit the subreddit:
- allows an user to edit the description or image of a subreddit
- takes any of these two or both as input and edits the entry in the db

List subreddits:
- show a list of subreddits 
- this can be used by the user to join any subreddit
- gives a paginated response 

View(posts):
- allows an user to view all the posts associated with a subreddit
- API response is a paginated list of posts - image, description, upvotes and downvotes

View(users):
- allows an user to view all the users that are in a particular community(subreddit)
- API response is a paginated list of users - username and profile photo

Join subreddit:
- allows an user to join/leave a subreddit based on if they are already in it or not

Delete subreddit:
- allows the user that created the subreddit to delete the delete it
- performs a soft delete



POSTS

Create a post:
- allows an user to post something on reddit
- takes an optional link/image and a description 
- creates a new subreddit

Edit the post:
- allows an user to edit the description of the post
- takes the input and edits the entry in the db

View posts(without comments):
- show a paginated list of posts, can act as a feed for an user
- can apply filters to change the posts shown in the feed

View post(with comments):
- show a detailed view of a post along with the comments associated with it
- response contains all the post attributes - description, image/link(optional), upvotes, downvotes and first layer of comments

Delete post:
- allows the user that created the post to delete the delete it
- performs a soft delete


COMMENTS:

Create a comment:
- allows an user to add a comment
- if the comment is directly on a post indicate it as first layer
-

Edit a comment:
- allows an user that made the comment to edit it.
- takes the input and edits the entry in the db

View thread:
- allows an user to view a thread of comments on a post
-




GENERAL

Search:
- allows an user to search for a particular subreddit or user
- shows any response that matches the search keyword

Upvote/downvote:
- allows a logged in user to upvote or downvote a post/comment
- saves voted by user_id against an entry in the model

Fllow/unfollow:
- aloows a logged in user to follow/unfollow users
- saves follower_id and followed_by_id in the model



