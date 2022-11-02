import random

quotes_data = []
quote_list = [
    "Be kind whenever possible. It is always possible.",
    "Music - it's motivational and just makes you relax.",
    "Many are called but few get up.",
    "The way to get started is to quit talking and begin doing.",
    "If you can dream it, you can do it.",
    "Know or listen to those who know.",
    "The wise does at once what the fool does at last.",
    "You can't cross the sea merely by standing and staring at the water.",
    "How do you know you're going to do something, untill you do it?",
    "Beginning today, treat everyone you meet as if they were going to be dead by midnight. Extend to them all the care, kindness and understanding you can muster, and do it with no thought of any reward. Your life will never be the same again.",
    "Always do your best. What you plant now, you will harvest later.",
    "Failure will never overtake me if my determination to succeed is strong enough.",
    "We should not give up and we should not allow the problem to defeat us.",
    "You just can't beat the person who never gives up.",
    "You have to learn the rules of the game. And then you have to play better than anyone else.",
    "The past cannot be changed. The future is yet in your power.",
    "Deserve your dream.",
    "Decide what you want, decide what you are willing to exchange for it. Establish your priorities and go to work.",
    "Aim for the moon. If you miss, you may hit a star.",
    "You must take action now that will move you towards your goals. Develop a sense of urgency in your life.",
    "If you fell down yesterday, stand up today.",
    "Do not weep; do not wax indignant. Understand.",
    "To be a good loser is to learn how to win.",
    "Don't watch the clock; do what it does. Keep going.",
    "When you fail you learn from the mistakes you made and it motivates you to work even harder.",
    "I learned that we can do anything, but we can't do everything... at least not at the same time. So think of your priorities not in terms of what activities you do, but when you do them. Timing is everything.",
    "Even if you fall on your face, you're still moving forward.",
    "Go for it now. The future is promised to no one.",
    "You can't wait for inspiration. You have to go after it with a club.",
    "Be miserable. Or motivate yourself. Whatever has to be done, it's always your choice.",
    "We make the world we live in and shape our own environment.",
    "A will finds a way.",
    "A goal is a dream with a deadline.",
    "There is progress whether ye are going forward or backward! The thing is to move!",
    "Do the one thing you think you cannot do. Fail at it. Try again. Do better the second time. The only people who never tumble are those who never mount the high wire. This is your moment. Own it.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "Do the difficult things while they are easy and do the great things while they are small. A journey of a thousand miles must begin with a single step.",
    "Be gentle to all and stern with yourself.",
    "Perseverance is not a long race; it is many short races one after the other.",
    "If you want to conquer fear, don't sit home and think about it. Go out and get busy."
]

def initQuotes():
    item_id = 0
    for item in quote_list:
        quotes_data.append({"id": item_id, "quote": item, "helped": 0, "useless": 0})
        item_id += 1
    for i in range(10):
        id = getRandomQuote()['id']
        addQuoteHelp(id)
    for i in range(5):
        id = getRandomQuote()['id']
        addQuoteUseless(id)

def getQuotes():
    return(quotes_data)

def getQuote(id):
    return(quotes_data[id])

def getRandomQuote():
    return(random.choice(quotes_data))

def favoriteQuote():
    best = 0
    bestID = -1
    for quote in getQuotes():
        if quote['helped'] > best:
            best = quote['helped']
            bestID = quote['id']
    return quotes_data[bestID]

def jeeredQuote():
    worst = 0
    worstID = -1
    for quote in getQuotes():
        if quote['useless'] > best:
            best = quote['useless']
            bestID = quote['id']
    return quotes_data[worstID]

def addQuoteHelp(id):
    quotes_data[id]['helped'] = quotes_data[id]['helped'] + 1
    return quotes_data[id]['helped']

def addQuoteUseless(id):
    quotes_data[id]['useless'] = quotes_data[id]['useless'] + 1
    return quotes_data[id]['useless']

def printQuote(quote):
    print(quote['id'], quote['quote'], "\n", "helped:", quote['helped'], "\n", "useless:", quote['useless'], "\n")

def countQuotes():
    return len(quotes_data)

if __name__ == "__main__": 
    initQuotes() 
    
    # Most likes and most jeered
    best = favoriteQuote()
    print("Most liked", best['helped'])
    printQuote(best)
    worst = jeeredQuote()
    print("Most jeered", worst['useless'])
    printQuote(worst)
    
    # Random joke
    print("Random quote")
    printQuote(getRandomQuote())
    
    # Count of Jokes
    print("Quotes Count: " + str(countQuotes()))