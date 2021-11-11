class Security_Middleware(object):
    def __init__(self, white_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.WHITE_LIST = white_list

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Security_Middleware, cls).__new__(cls)
        return cls._instance

    def check_valid(self, url, abort):
        if url in self.WHITE_LIST:
            print("Valid Request")
            pass
        else:
            abort()