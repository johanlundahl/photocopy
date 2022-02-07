import abc


class OrganizeManager:

    def __init__(self):
        self.move = MovePhoto()
        self.rename = RenamePhoto(self.move)
        self.create = CreateDestination(self.rename)
        self.validate = ValidatePhoto(self.create)

    def delegate(self, photo):
        self.validate.handle(photo)


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, next_handler=None):
        self._next_handler = next_handler
        self._proceed = True

    def handle(self, object):
        self.process(object)
        if self.proceed and self.has_next:
            self._next_handler.handle(object)

    @property
    def has_next(self):
        return self._next_handler is not None

    @property
    def proceed(self):
        return self._proceed

    @abc.abstractmethod
    def process(self, object):
        pass


class ValidatePhoto(Handler):

    def process(self, photo):
        Photo.is_photo()
        # is file
        # has exif
        print('Validating photo...')


class CreateDestination(Handler):

    def process(self, object):
        print('Creating destination...')
        #if not path.exists(dirpath):
            #os.makedirs(dirpath)
        pass


class RenamePhoto(Handler):

    def process(self, object):
        print('Renaming photo...')
        pass


class MovePhoto(Handler):

    def process(self, object):
        print('Moving photo...')
        pass
