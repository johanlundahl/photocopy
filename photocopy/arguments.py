from argparse import ArgumentParser


class Arguments(ArgumentParser):

    @classmethod
    def init(cls):
        parser = cls(description=('Organizes photos named according to date '
                     'pattern YYYY-MM-DD* into folder named by year/month.'))
        parser.add_argument('source',
                            help='Folder containg photos to organize.')
        parser.add_argument('target', help='Folder to sort photos into.')
        args = parser.parse_args()
        return args
