from olpcgames import activity
from gettext import gettext as _


class Activity(activity.PyGameActivity):

    """Your Sugar activity"""
    game_name = 'main:main'
    game_title = _('Hit the balls')
    game_size = None
