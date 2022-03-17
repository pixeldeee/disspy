import api.client


class DisBotEventType:
    on_message = "messagecreate"
    on_ready = "ready"


class DisErr:
    def __init__(self, code, message):
        self.code = code
        self.message = message


class Errors:
    DisBotInitErr = DisErr("b001", "Invalid prefix of bot")

    @staticmethod
    def raiseerr(obj: DisErr):
        raise RuntimeError(f"{obj.code} - {obj.message}")