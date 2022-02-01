from datetime import datetime
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
    
    @staticmethod
    def is_valid(path, filename):
        name = filename.split('.')[0]
        return os.path.isfile(os.path.join(path, filename)) and \
               Photo.parse_name(name) is not None

    @staticmethod
    def parse_name(filename):
        try:
            return datetime.strptime(filename, Photo.filename_pattern)
        except:
            return None
