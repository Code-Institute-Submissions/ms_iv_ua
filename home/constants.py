"""Definitions for entire project go here"""

# Tab Ids
TABS = {
    'issues':1,
    'features':2,
}

# Filter codes that also act as the status of issues and features.
# Note: putting some space between issues and features as we may need
# to add more filters and in the code at some point I am doing:
# if blah < features_all
FILTERS = {
    'issues_all':0,
    'issues_reported':1,
    'issues_ongoing':2,
    'issues_closed':3,
    'issues_mine':4,
    'features_all':10,
    'features_requested':11,
    'features_accepted':12, # UA has accepted feature and awaits payment from requester
    'features_working':13, # Requester has paid
    'features_declined':14,
    'features_finished':15,
    'features_mine':16,
}

# An alternative to captcha. Dictionary of questions. One will be chosen at random
# when a user registers.
NO_BOTS = {
    '1 and 1 and 1':'3',
    '1 and 2 and 1':'4',
    '1 and 1 and 2':'4',
    '2 and 2 and 2':'6',
    '2 and 2 and 1':'5',
    '2 and 1 and 1':'4',
    '3 and 3 and 3':'9',
    '3 and 2 and 1':'6',
    '3 and 3 and 2':'8',
    '1 and 1 and 3':'5',
    '2 and 3 and 2':'7',
    '5 and 2 and 1':'8',
    '1 and 0 and 0':'1',
    '0 and 0 and 0':'0',
    '5 and 4 and 0':'9',
    '4 and 1 and 1':'6',
}

# Currency and values
DEFAULT_CURRENCY = 'GBP'
MIN_BID = 10
MAX_BID = 5000
