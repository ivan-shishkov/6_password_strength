import argparse


def get_password_strength(password):
    pass


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'password',
        help='a password for analysis',
        type=str,
    )

    command_line_arguments = parser.parse_args()

    return command_line_arguments


def main():
    command_line_arguments = parse_command_line_arguments()

    password = command_line_arguments.password


if __name__ == '__main__':
    main()
