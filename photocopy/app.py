import os
import sys
import time
from photocopy.photo import Photo
from photocopy.arguments import Arguments
from photocopy.commands import OrganizeManager


def progress(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.2)


def collect(source_path):
    photos = []
    for dirpath, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            if Photo.is_photo(dirpath, filename):
                progress('collected %s photos\r' % (len(photos)))
                photos.append(Photo(dirpath, filename))
    print(f'Collected {len(photos)} photos')
    return photos


if __name__ == '__main__':
    print('------------ Photos ------------')
    args = Arguments.init()

    organizer = OrganizeManager(args.target)

    print('Scanning {} for photos'.format(args.source))
    photos = collect(args.source)

    for index, photo in enumerate(photos):
        organizer.delegate(photo)
        progress(f'Processed {index} of {len(photos)}\r')
    print(f'Processed {len(photos)} of {len(photos)}')
