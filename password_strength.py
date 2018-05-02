import argparse

from zxcvbn import zxcvbn


def get_password_strength(password):
    password_analysis_result = zxcvbn(password)

    score_password_strength = int(password_analysis_result['guesses_log10'])

    if score_password_strength < 1:
        score_password_strength = 1

    if score_password_strength > 10:
        score_password_strength = 10

    return score_password_strength


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'password',
        help='a password for analysis',
        type=str,
    )

    command_line_arguments = parser.parse_args()

    return command_line_arguments


def print_score_password_strength(score):
    print('{:-<36}'.format(''))
    print('Score of password strength: {:2} of 10'.format(
        score,
    ))
    print('{:-<36}'.format(''))


def main():
    command_line_arguments = parse_command_line_arguments()

    password = command_line_arguments.password

    print_score_password_strength(
        score=get_password_strength(password),
    )


if __name__ == '__main__':
    main()
