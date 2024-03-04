from statistics import mean
from itertools import groupby
from operator import itemgetter

from ai.sentiment_analysis import Sentiment
from ai.sentiaspect_evaluation import SentiAspect, AspectRating

def avg_evaluation_strategy(sentiaspects: list[SentiAspect]) -> AspectRating:
    to_rating = lambda k: { 
        Sentiment.POSITIVE: 1., Sentiment.NEUTRAL: 0., Sentiment.NEGATIVE: -1.
    }[k]

    key = itemgetter(0)
    sentiaspects.sort(key=key) 

    return {
        key: mean(map(to_rating, group))
        for key, group in groupby(sentiaspects, key=key)
    }