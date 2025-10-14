from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "N2 Auto Reply Bot")
API_ID = 24380477
API_HASH = "dd131f5648d254a669a629e54039940e"
USER_SESSION = environ.get("USER_SESSION", "BQF0BD0ATz3ZPaNQca2-nVx0KCkRHQwOCzQJo14yWe5FMLBKWxoLRhFfxk8nJ4F7LwnKPjbHMnm3K8ZAF0VDbz8MrURbOm0GvUYF-hjcWNbuXKZqZGguEZdoxw8TFYIDk4Y39Jg5AbtfFlc6vwtiiedIQrpzGPDgP6lUDU6ReeX6oRfWrIot6sviciplJjeCrMzX_wVQpbGC1oSq87ebo1BGUmsI4aLQ5IcI4UK1yAFbtfD3n0TRYYCJsMPUMZ9ap57JFyrKcEcY3qM57byKYKx1cf_KyCZu9ECMCRZiLcxgZhWGiYuv-jSxRk_oYWrSukpxjotlh9DNzBKwsULWsLSCW8UCOAAAAAFyRFSnAA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002074744533"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002220525479').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6212048039').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
