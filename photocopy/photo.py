from datetime import datetime
import exifread
import os


class Photo:
    filename_pattern = '%Y-%m-%d_%H-%M-%S'

    def __init__(self, dirpath, filename):
        self._dirpath = dirpath
        self._filename = filename

    @property
    def path(self):
        return self._dirpath

    @property
    def full_path(self):
        return os.path.join(self._dirpath, self._filename)

    @property
    def filename(self):
        return self._filename

    @property
    def filename_ordered(self):
        return self.created.strftime(self.filename_pattern)

    @property
    def year_month(self):
        return self.created.strftime('%Y/%m')

    @property
    def created(self):
        f = open(self.full_path, 'rb')
        tags = exifread.process_file(f)
        created = tags["EXIF DateTimeOriginal"]
        return datetime.strptime(created.printable, '%Y:%m:%d %H:%M:%S')

    @property
    def has_created_time(self):
        f = open(self.path, 'rb')
        tags = exifread.process_file(f)
        return "EXIF DateTimeOriginal" in tags.keys()

    @staticmethod
    def is_valid(path, filename):
        name = filename.split('.')[0]
        return os.path.isfile(os.path.join(path, filename)) and \
            (Photo.parse_name(name) is not None)

    @staticmethod
    def is_photo(path, filename):
        # name = filename.split('.')[0]
        return os.path.isfile(os.path.join(path, filename)) and \
               Photo.has_exif(path, filename)

    @staticmethod
    def has_exif(path, filename):
        f = open(os.path.join(path, filename), 'rb')
        tags = exifread.process_file(f)
        return "EXIF DateTimeOriginal" in tags.keys()

    @staticmethod
    def parse_name(filename):
        try:
            return datetime.strptime(filename, Photo.filename_pattern)
        except ValueError:
            return None
