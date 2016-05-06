
class InvalidDataSetIOError(Exception):
    """The base class for all DataSetIO related custom exceptions
    """


class ResourceMismatchError(InvalidDataSetIOError):

    def __init__(self, responses):
        super(ResourceMismatchError, self).__init__()
        self.responses = responses

    def __str__(self):
        return "Resources responded differently: " + ', '.join(
            map(str, self.responses))


