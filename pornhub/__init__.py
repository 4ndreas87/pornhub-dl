"""Entry point for pornhub downloader."""
import sys

from pornhub.db import create_db
from pornhub.arguments import parser


def main():
    """Parse args, check if everything is ok and start pornhub."""
    args = parser.parse_args()

    create_db()

    # Check if pueue is available:
    # command_factory('status')({}, root_dir=os.path.expanduser('~'))
    try:
        var_args = vars(args)
        if 'func' in var_args:
            args.func(var_args)
        else:
            print("Unknown command. Use --help.")
            sys.exit(1)
    except KeyboardInterrupt:
        print('Keyboard interrupt. Shutting down')
        sys.exit(0)
