'''
Ten plik wczytuje plik dziennika i generuje plik CSV z tymi samymi danymi.
'''
import csv
import argparse
from price_log import PriceLog


def log_to_csv(input_file, output_file, location):
    logs = [PriceLog.parse(location, line) for line in input_file]

    # Zapisywanie pliku w formacie csv.
    writer = csv.writer(output_file)
    writer.writerow(PriceLog.header())
    writer.writerows(l.row() for l in logs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input', type=argparse.FileType('r'),
                        help='Plik wejściowy')
    parser.add_argument(dest='output', type=argparse.FileType('w'),
                        help='Plik wyjściowy')
    parser.add_argument('-l', dest='location', type=str,
                        help='Lokalizacja; domyślnie US', default='US')

    args = parser.parse_args()
    log_to_csv(args.input, args.output, args.location)
