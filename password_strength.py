import sys
from getpass import getpass

from zxcvbn import zxcvbn


def get_score_password_strength(
        password,
        min_score_password_strength=1,
        max_score_password_strength=10):
    password_analysis_result = zxcvbn(password)

    score_password_strength = int(password_analysis_result['guesses_log10'])

    score_password_strength_limited = min(
        max(
            score_password_strength,
            min_score_password_strength,
        ),
        max_score_password_strength,
    )

    return score_password_strength_limited


def print_score_password_strength(score):
    print('{:-<36}'.format(''))
    print('Score of password strength: {:2} of 10'.format(
        score,
    ))
    print('{:-<36}'.format(''))


def main():
    password = getpass(prompt='Enter a password for analysis: ')

    if not password:
        sys.exit('Password is empty')

    print_score_password_strength(
        score=get_score_password_strength(password),
    )


if __name__ == '__main__':
    main()
