import os
from os import path
import sys
import shutil
import time
from photocopy.photo import Photo
from photocopy.arguments import Arguments
from photocopy.commands import OrganizeManager


def name_photos(photos):
    for index, photo in enumerate(photos):
        if photo.has_created_time:
            # print(f'{photo.filename} {photo.created}')
            progress('Renamed %s photos\r' % (index))
    print(f'Renamed {len(photos)} photos')


def progress(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.2)


def create_folder(dirpath):
    if not path.exists(dirpath):
        os.makedirs(dirpath)


def collect(source_path):
    photos = []
    for dirpath, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            if Photo.is_photo(dirpath, filename):
                progress('collected %s photos\r' % (len(photos)))
                photos.append(Photo(dirpath, filename))
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

    organizer = OrganizeManager(args.target)

    print('Scanning {} for photos'.format(args.source))
    photos = collect(args.source)

    for photo in photos:
        organizer.delegate(photo)
