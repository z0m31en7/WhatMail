import argparse
from tabulate import tabulate
from colorama import Fore, Style

print("\n")
print("▒█░░▒█ █░░█ █▀▀█ ▀▀█▀▀ ▒█▀▄▀█ █▀▀█ ░▀░ █░░ ▀█ ")
print("▒█▒█▒█ █▀▀█ █▄▄█ ░░█░░ ▒█▒█▒█ █▄▄█ ▀█▀ █░░ █▀ ")
print("▒█▄▀▄█ ▀░░▀ ▀░░▀ ░░▀░░ ▒█░░▒█ ▀░░▀ ▀▀▀ ▀▀▀ ▄░")
print("\n")
print("        A tool for email header forensics")
print("            By: Pranjal Goel (z0m31en7)\n")

def parse_header(header_file):
    header_data = {}

    with open(header_file, 'r') as file:
        lines = file.readlines()

        current_field = None
        current_value = ''

        for line in lines:
            if ':' in line:
                if current_field:
                    header_data[current_field] = current_value.strip()

                current_field, current_value = line.split(':', 1)
                current_field = current_field.strip()
                current_value = current_value.strip()
            elif current_field:
                current_value += ' ' + line.strip()

        if current_field:
            header_data[current_field] = current_value.strip()

    return header_data

def display_header_info(header_data):
    output = ''

    output += f"{Fore.RED}Message Information:\n"
    output += "---------------------\n"
    output += Style.RESET_ALL

    # Commonly recognized email header fields
    fields = ['To', 'From', 'Subject', 'Date', 'Delivered-To']

    table_data = []
    for field in fields:
        if field in header_data:
            table_data.append([field, header_data[field]])

    output += tabulate(table_data, headers=[f"{Fore.BLUE}Field", f"{Fore.BLUE}Value"], tablefmt="fancy_grid")
    output += f"\n{Style.RESET_ALL}"

    output += f"{Fore.RED}\nAdditional Fields:\n"
    output += "------------------\n"
    output += Style.RESET_ALL

    # Additional useful fields
    additional_fields = {
        'Message-ID': 'Message ID',
        'Return-Path': 'Return Path',
        'Reply-To': 'Reply-To',
        'X-Headers': 'X-Headers',
        'Received': 'Received',
        'MIME-Version': 'MIME Version',
        'Content-Type': 'Content Type',
        'Received-SPF': 'Received-SPF',
        'DKIM-Signature': 'DKIM Signature',
        'Authentication-Results': 'Authentication Results',
        'X-Mailer': 'X-Mailer',
        'DMARC-Results': 'DMARC Results'
    }

    table_data = []
    for field, label in additional_fields.items():
        if field in header_data:
            table_data.append([label, header_data[field]])

    output += tabulate(table_data, headers=[f"{Fore.BLUE}Field", f"{Fore.BLUE}Value"], tablefmt="fancy_grid")
    output += f"\n{Style.RESET_ALL}"

    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='WhatMail')
    parser.add_argument('-hf', '--header_file', type=str, help='Path to the email header file')
    parser.add_argument('-O', '--output_file', type=str, help='Path to the output file')
    args = parser.parse_args()

    if args.header_file:
        header_data = parse_header(args.header_file)
        output = display_header_info(header_data)

        if args.output_file:
            with open(args.output_file, 'w') as file:
                file.write(output)
        else:
            print(output)
    else:
        parser.print_help()