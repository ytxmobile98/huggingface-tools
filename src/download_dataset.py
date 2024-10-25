from argparse import ArgumentParser
import os
from os.path import abspath, dirname, join

from huggingface_hub import hf_hub_download, snapshot_download

DEFAULT_DIR = join(dirname(abspath(__file__)), 'data')


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('--repo', type=str, required=True, help='repo name')
    parser.add_argument('--filename', type=str, required=False,
                        help='filename to download;'
                        ' if not specified, download the entire repo')
    parser.add_argument('--dir', type=str, required=False, default=DEFAULT_DIR,
                        help='directory name (will be created if not exists)')

    return parser.parse_args()


def main():
    args = parse_args()

    os.makedirs(args.dir, exist_ok=True)

    download_single_file = bool(args.filename)
    if download_single_file:
        hf_hub_download(repo_id=args.repo, filename=args.filename,
                        repo_type='dataset', local_dir=args.dir)
    else:
        snapshot_download(repo_id=args.repo, repo_type='dataset',
                          local_dir=args.dir)


if __name__ == '__main__':
    main()
