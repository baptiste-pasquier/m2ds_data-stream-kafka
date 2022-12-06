from colorama import Back, Fore, Style

KEYWORD = "COVID"
MAX_RESULTS = 100
TIME_SLEEP = 1

TOPICS_COLOR = {
    "raw-tweets": Back.BLACK + Fore.WHITE + Style.BRIGHT,
    "en-tweets": Back.BLUE + Fore.WHITE + Style.BRIGHT,
    "fr-tweets": Back.MAGENTA + Fore.WHITE + Style.BRIGHT,
    "positive-tweets": Back.GREEN + Fore.BLACK,
    "negative-tweets": Back.RED + Fore.WHITE + Style.BRIGHT,
}
