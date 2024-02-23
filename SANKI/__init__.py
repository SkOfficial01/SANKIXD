from SANKI.core.bot import Sanki
from SANKI.core.dir import dirr
from SANKI.core.git import git
from SANKI.core.userbot import Userbot
from SANKI.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Dil()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
