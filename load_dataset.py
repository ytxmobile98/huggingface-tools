import argparse
from os.path import splitext

from datasets import load_dataset


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, required=True, help='Data file')
    parser.add_argument('--type', type=str, choices=[
        # Reference:
        # https://huggingface.co/docs/datasets/loading#local-and-remote-files
        'csv', 'json', 'parquet', 'arrow', 'webdataset'
    ], help='Data type')

    return parser.parse_args()


def get_data_type(file: str):
    _, ext = splitext(file)
    ext = ext[1:].lower()
    if ext == 'tar':
        return 'webdataset'
    return ext


def main():
    args = parse_args()

    data_type = args.type if args.type else get_data_type(args.file)
    data = load_dataset(data_type, data_files=args.file)
    print(data)


if __name__ == '__main__':
    main()
