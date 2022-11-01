import pendulum

colors = {
    "magenta": '\033[95m',
    "blue": '\033[94m',
    "green": '\033[92m',
    "yellow": '\033[93m',
    "red": '\033[91m',
    "grey": '\033[0m',
    "white": '\033[1m',
    "underline": '\033[4m',
    "bold_red": "\x1b[31;1m",
    "reset": "\x1b[0m"
}


class Logging:
    def __init__(self, prefix: str, should_log: bool):
        self.should_log = should_log
        self.prefix = prefix
        if self.should_log:
            self.debug(f"Logger initialised")

    # Format: [YYYY-MM-DD HH:MM:SS UTC]
    def timestamp(self):
        return str(pendulum.from_timestamp(pendulum.now("Europe/London").timestamp())).replace("T", " ").split(".")[0] + " UTC"

    def info(self, message):
        print(f"{colors['blue']}[INFO]  [{self.timestamp()}] [{self.prefix}]: {message} {colors['reset']}")

    def debug(self, message):
        print(f"{colors['green']}[DEBUG] [{self.timestamp()}] [{self.prefix}]: {message} {colors['reset']}")

    def error(self, message):
        print(f"{colors['red']}[ERROR] [{self.timestamp()}] [{self.prefix}]: {message} {colors['reset']}")
