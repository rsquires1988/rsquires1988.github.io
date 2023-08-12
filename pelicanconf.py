AUTHOR = 'Ryan Squires'
SITENAME = 'Rouse Browse'
SITEURL = 'https://rsquires1988.github.io'
OUTPUT_PATH = '/'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

THEME = "/home/vscode/pelican-themes/sneakyidea"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll #
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'))

# Social widget
SOCIAL = (('GitHub', 'https://rsquires1988.github.com'),
          ('LinkedIn', 'https://www.linkedin.com/in/ryan-squires-0a15841b0/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
