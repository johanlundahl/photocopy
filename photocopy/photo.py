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
        return os.path.join(self._dirpath, self._filename)

    @property
    def year_month(self):
        name = self._filename.split('.')[0]
        dt = Photo.parse_name(name)
        return dt.strftime('%Y/%m')
    
    @property
    def filename(self):
        return self._filename

    @property
    def created(self):
        f = open(self.path, 'rb')
        tags = exifread.process_file(f)
        created = tags["EXIF DateTimeOriginal"]
        return created
    
    @property
    def has_created_time(self):
        f = open(self.path, 'rb')
        tags = exifread.process_file(f)
        return "EXIF DateTimeOriginal" in tags.keys()

    @staticmethod
    def is_valid(path, filename):
        name = filename.split('.')[0]
        return os.path.isfile(os.path.join(path, filename)) and \
               Photo.parse_name(name) is not None

    @staticmethod
    def is_photo(path, filename):
        name = filename.split('.')[0]
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
        except:
            return None
