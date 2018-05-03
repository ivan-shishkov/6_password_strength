import sys

from zxcvbn import zxcvbn


def get_score_password_strength(
        password,
        min_score_password_strength=1,
        max_score_password_strength=10):
    password_analysis_result = zxcvbn(password)

    score_password_strength = int(password_analysis_result['guesses_log10'])

    if score_password_strength < min_score_password_strength:
        score_password_strength = min_score_password_strength

    if score_password_strength > max_score_password_strength:
        score_password_strength = max_score_password_strength

    return score_password_strength


def print_script_info():
    print('{:-<36}'.format(''))
    print('{:^36}'.format('Password Strength Calculator'))
    print('{:-<36}'.format(''))


def print_score_password_strength(score):
    print('{:-<36}'.format(''))
    print('Score of password strength: {:2} of 10'.format(
        score,
    ))
    print('{:-<36}'.format(''))


def main():
    print_script_info()

    password = input('Enter a password for analysis: ')

    if not password:
        sys.exit('Password is empty')

    print_score_password_strength(
        score=get_score_password_strength(password),
    )


if __name__ == '__main__':
    main()
