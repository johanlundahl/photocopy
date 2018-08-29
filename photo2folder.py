import os
import shutil
import argparse
import datetime

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
        dt = datetime.strptime(name, self.filename_pattern)
        return dt.strftime('%Y/%M')
    
    @property
    def filename(self):
        return self._filename
    
    @property
    def is_valid(self):
        # TODO: check that file name follows pattern YYYY-MM-DD_HH-mm-ss
        return os.path.isfile(self.path)
        
def create_folder(path):
	if not os.path.exists(path):
		os.makedirs(path)

def get_photos(source_path):
    photos = {}
    for dirpath, dirnames, filenames in os.walk(sourcePath):
        for filename in filenames:
            photos[filename] = Path(dirpath, filename)
    return photos
    
def organize(photos, target_path):
    for photo in photos:
        if photo.is_valid():            
            create_folder(photo.year_month())
            print(photo.path(), '->', os.path.join(photo.year_month(), photo.filename()))
            shutil.move(photo.path(), os.path.join(photo.year_month(), photo.filename()))
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organizes photos named according to date pattern YYYY-MM-DD* into folder named by year/month.')
    parser.add_argument('source', help='Folder containg photos to organize.')
    parser.add_argument('target', help='Folder to sort photos into.')
    args = parser.parse_args()
    
    photos = get_photos(args.source)
    organize(photos, args.target)
