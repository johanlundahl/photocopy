import abc
import os
from os import path
import shutil


class OrganizeManager:

    def __init__(self, target_path):
        self.move = MovePhoto()
        self.create = CreateDestination(self.move, target_path)
        self.rename = RenamePhoto(self.create)
        self.validate = ValidatePhoto(self.rename)

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
        # Photo.is_photo()
        # is file
        # has exif
        print('Validating photo...')


class RenamePhoto(Handler):

    def __init__(self, next_handler=None, target_path=None):
        self._target_path = target_path
        super().__init__()

    def process(self, photo):
        renamed = path.join(photo.path, photo.filename_ordered)
        shutil.move(photo.full_path, renamed)


class CreateDestination(Handler):

    def __init__(self, next_handler=None, target_path=None):
        self._target_path = target_path
        super().__init__()

    def process(self, photo):
        destination = path.join(self._target_path, photo.year_month)
        if not path.exists(destination):
            os.makedirs(destination)


class MovePhoto(Handler):

    def process(self, object):
        print('Moving photo...')
        pass
