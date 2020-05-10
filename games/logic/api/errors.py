class CalleeError(Exception):
    pass

class ModelParameterError(CalleeError):
    pass

class MissingModelParameter(ModelParameterError):
    def __init__(self, key):
        if key is None:
            raise TypeError("Bad key arg cannot be null")
        else:
            msg = "Missing parameter '%s'" % str(key)
            super(MissingModelParameter, self).__init__(msg)

class ExcessModelParameter(ModelParameterError):
    def __init__(self, key):
        if key is None:
            raise TypeError("Bad key arg cannot be null")
        else:
            msg = "Extra key '%s' in params" % str(key)
            super(ExcessModelParameter, self).__init__(msg)

class CalleeKeyError(CalleeError):
    pass
