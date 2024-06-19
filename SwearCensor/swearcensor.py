#!/usr/bin/python3

import re, sys

def censor_statement(statement):
    swear_words = re.compile(r'\b(fuck(?:er|ing|s|ed)?|shit(?:ty|s)?|bitch(?:es|ing)?|cunt(?:s)?|ass(?:hole|es)?|mother(?:fucker|fucking|s)?|goddamn(?:ed)?|pussy|boner(?:s)?|bastard(?:s)?|cocksucker(?:s)?|whore(?:s)?|pussies|cock(?:s)?)\b', re.IGNORECASE)

    censored_statement = swear_words.sub(lambda match: match.group(1)[0] + '*' * (len(match.group(1)) - 1), statement)
    return censored_statement


def main():
    input_filename = input('Enter the name of a text file to censor:\n')
    output_filename = 'censored' + input_filename

    with open(input_filename, 'r') as input_file:
        statements = input_file.readlines()

    with open(output_filename, 'a') as output_file:
        for statement in statements:
            censored_statement = censor_statement(statement)
            output_file.write(censored_statement)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('\nHave a Great Day!')

