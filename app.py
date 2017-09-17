from __future__ import print_function

import argparse

from api.unfollower import Unfollower
from utils.auth import get_authenticated_api




parser = argparse.ArgumentParser()

subParsers = parser.add_subparsers(help='[command] help')


twitterParser = subParsers.add_parser("twitter",
                                      help="invokes the twitter related commands")

twitterParser.add_argument_group()

twitterParser.add_argument("-n", "--only-non-followers", default=False, action="store_true")


twitterParser.add_argument("-p", "--print-on-delete", help="Prints the names of deleted users",default=False, action="store_true")



def main():
    api = get_authenticated_api()
    unfollower = Unfollower(api)
    unfollower.destroyAllFriendships()


if __name__ == '__main__':
    main()
