import os
from os import path
import sys
import shutil
import time
from photo import Photo
from arguments import Arguments

# Copy photos to <sourcePath>
# Run <sourcePath> through ExifRenamer
# Run this script


def progress(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()
    #time.sleep(0.2)


def create_folder(dirpath):
	if not path.exists(dirpath):
		os.makedirs(dirpath)


def collect(source_path):
    photos = {}
    for dirpath, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            if Photo.is_valid(dirpath, filename):
                progress('collected %s photos\r' % (len(photos)))
                photos[filename] = Photo(dirpath, filename)
    print(f'Collected {len(photos)} photos')
    return photos


def organize(photos, target_path):
    for index, val in enumerate(photos):
        photo = photos[val]
        target_path = path.realpath(target_path)
        folder = path.join(target_path, photo.year_month)
        create_folder(folder)
        shutil.move(photo.path, path.join(folder, photo.filename))

        percent = round(index/len(photos)*100)
        progress(f'Organized {percent}%, {index} photos\r')
    print(f'Organized {len(photos)} photos')


if __name__ == '__main__':
    print('------------ Photos ------------')
    args = Arguments.init()

    print('Scanning {} for photos'.format(args.source))
    photos = collect(args.source)
    organize(photos, args.target)
