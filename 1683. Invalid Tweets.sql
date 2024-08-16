SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) - LENGTH(REPLACE(content, ' ', '')) + 1 > 2;
