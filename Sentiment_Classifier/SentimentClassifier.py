#work in prog...


# Twitter Sentiment Analysis Script

# This script analyzes sentiment in tweets and calculates positive, negative, and net scores.

# Instructions:
# 1. Ensure 'project_twitter_data.csv' contains tweet text, number of retweets, and replies.
# 2. 'positive_words.txt' should list positive words, one per line.
# 3. 'negative_words.txt' should list negative words, one per line.
# 4. Run the script to analyze each tweet's sentiment and output results to 'resulting_data.csv'.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# Function to strip punctuation from a string
def strip_punctuation(x):
    for i in punctuation_chars:
        x = x.replace(i, '')
    return x

# Function to count positive words in a sentence
def get_pos(sent):
    l_s = sent.lower()
    non_p = strip_punctuation(l_s)
    splitted_ = non_p.split()
    pos_count = 0 
    for w in splitted_:
        if w in positive_words:
            pos_count += 1
    return pos_count

# Function to count negative words in a sentence
def get_neg(sent):
    l_s = sent.lower()
    non_p = strip_punctuation(l_s)
    splitted_ = non_p.split()
    neg_count = 0 
    for w in splitted_:
        if w in negative_words:
            neg_count += 1
    return neg_count

# Read positive words from file
positive_words = []
with open("positive_words.txt") as pos_f:
    positive_words = [line.strip() for line in pos_f if line.strip() and not line.startswith(';')]

# Read negative words from file
negative_words = []
with open("negative_words.txt") as neg_f:
    negative_words = [line.strip() for line in neg_f if line.strip() and not line.startswith(';')]

# Open input and output files
with open("project_twitter_data.csv", "r") as fileop, open("resulting_data.csv", "w") as out:
    data = fileop.readlines()
    out.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
    
    # Process each line of input data
    for line in data[1:]:  # Skip header line
        new_splt = line.strip().split(",")
        tweet_text = new_splt[0]
        num_retweets = new_splt[1]
        num_replies = new_splt[2]
        
        # Calculate positive and negative scores for the tweet text
        pos_score = get_pos(tweet_text)
        neg_score = get_neg(tweet_text)
        
        # Calculate net score
        net_score = pos_score - neg_score
        
        # Prepare output row
        row = "{},{},{},{},{}\n".format(num_retweets, num_replies, pos_score, neg_score, net_score)
        
        # Write row to output file
        out.write(row)

# Print completion message
print("Analysis complete. Check resulting_data.csv for output.")
