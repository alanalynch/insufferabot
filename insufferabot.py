import markovify
from twitter_scraper import get_tweets

def combine_tweets():
    # for some reason 4, 5, and 7 aren't working rn
    tweets = '\n'.join([t['text'] for t in get_tweets('ericgarland', pages=15)])
    tweets2 = '\n'.join([t['text'] for t in get_tweets('jordanbpeterson', pages=15)])
    tweets3 = '\n'.join([t['text'] for t in get_tweets('nytdavidbrooks', pages=15)])
    #tweets4 = '\n'.join([t['text'] for t in get_tweets('louisemensch', pages=5)])
    #tweets5 = '\n'.join([t['text'] for t in get_tweets('drjillstein', pages=5)])
    tweets6 = '\n'.join([t['text'] for t in get_tweets('keitholbermann', pages=5)])
    #tweets7 = '\n'.join([t['text'] for t in get_tweets('billmaher', pages=3)])
    tweets8 = '\n'.join([t['text'] for t in get_tweets('paulkrugman', pages=5)])
    combined = tweets + '\n' + tweets2 + '\n' + tweets3 + '\n' + tweets6 + '\n' + tweets8

    return combined

if __name__=='__main__':
    text_model = markovify.NewlineText(combine_tweets())

    while True:
        print(text_model.make_short_sentence(140))
        response = input('Want another? ')
        if response == 'y':
            continue
