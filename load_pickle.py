from argparse import ArgumentParser
import pickle


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('--filename', type=str, required=True,
                        help='filename to load')

    return parser.parse_args()


def load_pickle(filename: str):
    with open(filename, 'rb') as f:
        return pickle.load(f)


def main():
    args = parse_args()

    data = load_pickle(args.filename)
    print(data)


if __name__ == '__main__':
    main()
