import os
import shutil
import argparse
from datetime import datetime

# Copy photos to <sourcePath>
# Run <sourcePath> through ExifRenamer
# Run this script

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
        return os.path.isfile(os.path.join(path, filename)) and Photo.parse_name(name) is not None

    @staticmethod
    def parse_name(filename):
        try:
            return datetime.strptime(filename, Photo.filename_pattern)
        except:
            return None

def create_folder(dirpath):
	if not os.path.exists(dirpath):
		os.makedirs(dirpath)

def get_photos(source_path):
    photos = {}
    for dirpath, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            print(Photo.is_valid(dirpath, filename), filename)
            if Photo.is_valid(dirpath, filename):
                photos[filename] = Photo(dirpath, filename)
    return photos
    
def organize(photos, target_path):
    for filename, photo in photos.iteritems():
        target_path = os.path.realpath(target_path)
        folder = os.path.join(target_path, photo.year_month)
        create_folder(folder)
        print('{} -> {}'.format(photo.path, os.path.join(folder, photo.filename)))
        shutil.move(photo.path, os.path.join(folder, photo.filename))
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organizes photos named according to date pattern YYYY-MM-DD* into folder named by year/month.')
    parser.add_argument('source', help='Folder containg photos to organize.')
    parser.add_argument('target', help='Folder to sort photos into.')
    args = parser.parse_args()
    
    print('Scanning {} for photos'.format(args.source))
    photos = get_photos(args.source)

    print('Organizing {} photos'.format(len(photos)))
    organize(photos, args.target)
