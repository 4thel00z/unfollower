from __future__ import print_function

from api.unfollower import Unfollower
from click_monkey_patch import prevent_ascii_env, wrapper_get_terminal_size
from utils.auth import get_authenticated_api
import click

prevent_ascii_env()
wrapper_get_terminal_size()


#
#   Parser handler section
#


@click.group(chain=True)
def main():
    pass


@main.command("twitter")
@click.option("-u", "--unfollow", help="Unfollow all ( or only non-followers with -o option) followers in your list.", default=False, is_flag=True)
@click.option("-o", "--only_non_follower", help="Only usable with -u option. Unfollow only non followers.",
              default=False, is_flag=True)
@click.option("-p", "--print_on_delete", help="Prints the names of deleted users", default=False, is_flag=True)
def twitter_handler(unfollow, only_non_follower, print_on_delete):
    if unfollow:
        api = get_authenticated_api()
        unfollower = Unfollower(api)
        unfollower.destroyAllFriendships(only_non_follower, print_on_delete)

        # TODO: add new subcommands


#
#   Main method section
#


if __name__ == '__main__':
    main()
