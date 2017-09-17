class Unfollower():
    """This class is intended to provide APIs to unfollow all friends ( who unfollowed you ) """

    def __init__(self, api):
        self.api = api

    def _get_friends(self):
        return self.api.GetFriends()

    def destroyAllFriendships(self, only_non_follower=False,friends=None, ):

        if friends is None:
            friends = self.api.GetFriends()

        if len(friends) == 0:
            print("You aren't following anyone already. You are a true leader.")
            return

        for friend in friends:
            print("Destroying friendship with user: " + friend.id)
            self.api.DestroyFriendship(user_id=friend.id)
        print("You have successfully unfollowed all losers.")
