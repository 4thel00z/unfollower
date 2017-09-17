from __future__ import print_function

import argparse

from api.unfollower import Unfollower
from utils.auth import get_authenticated_api


#
#   Parser handler section
#


def twitter_handler(args):
    api = get_authenticated_api()
    unfollower = Unfollower(api)
    unfollower.destroyAllFriendships(only_non_follower=args.only_non_followers)



#
#   Parser setup section
#

parser = argparse.ArgumentParser()

subParsers = parser.add_subparsers(help='[command] help')

twitterParser = subParsers.add_parser("twitter",
                                      help="invokes the twitter related commands")
twitterParser.add_argument_group()
twitterParser.set_defaults(func=twitter_handler)
twitterParser.add_argument("-n", "--only-non-followers", default=False, action="store_true")

twitterParser.add_argument("-p", "--print-on-delete", help="Prints the names of deleted users", default=False,
                           action="store_true")


#
#   Main method section
#

def main():
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
