import argparse as ap
import os

from huggingface_hub import hf_hub_download


def parse_args():
    parser = ap.ArgumentParser()

    parser.add_argument('--repo', type=str, required=True, help='Repo name')
    parser.add_argument('--filename', type=str, required=True,
                        help='Filename to download')
    parser.add_argument('--dir', type=str, required=True,
                        help='Directory name (will be created if not exists)')

    return parser.parse_args()


def main():
    args = parse_args()
    os.makedirs(args.dir, exist_ok=True)
    hf_hub_download(repo_id=args.repo, filename=args.filename,
                    repo_type='dataset', local_dir=args.dir)


if __name__ == '__main__':
    main()
