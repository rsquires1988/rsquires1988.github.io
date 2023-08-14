AUTHOR = 'Ryan Squires'
SITEURL = 'https://rousebrowse.com'
SITENAME = 'Blog'
SITETITLE = 'Rouse Browse'
SITESUBTITLE = 'What is this new devvery?'
SITEDESCRIPTION = "'It's not safe out here. It's wondrous, with treasures to satiate desires both subtle and gross. But it's not for the timid.'"
SITELOGO = SITEURL + "/images/profile.jpeg"
FAVICON = SITEURL + "/images/favicon.ico"

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
THEME = "/home/vscode/pelican-themes/Flex"

PATH = 'content'
OUTPUT_PATH = 'output'
DELETE_OUTPUT_DIRECTORY = True

# BROWSER_COLOR = "#5e644f"
ROBOTS = "index, follow"

COPYRIGHT_YEAR = 2023

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll #
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'))

# Social widget
SOCIAL = (('github', 'https://github.com/rsquires1988'),
          ('linkedin', 'https://www.linkedin.com/in/ryan-squires-0a15841b0/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME',]# 'extra/custom.css']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}# 'extra/custom.css': {'path': 'static/custom.css'}}

MAIN_MENU = True

THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'zenburn'

LOAD_CONTENT_CACHE = False
IMAGE_PROCESS_FORCE = True
IMAGE_PROCESS = {
    "thumb": {
        "type": "image",
        "ops": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
    },
    "article-image": {
        "type": "image",
        "ops": ["scale_in 300 300 True"],
    },
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 800 600 True"]),
            ("2x", ["scale_in 1600 1200 True"]),
            ("4x", ["scale_in 3200 2400 True"]),
        ],
        "default": "1x",
    },
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}