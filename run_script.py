import json
import safaribooks
import argparse
import os
import sys
import requests

def run_app(credentials=None):
	with open("collection.json", 'r') as file:
	    collection = json.load(file)

	bookIds = [elem['api_url'].split("/api/v1/book/")[-1].split("/")[0] for elem in collection[0]['content']]

	for book in bookIds:
	    if book not in set([elem.split("(")[-1].replace(")","") for elem in os.listdir('Books')]):
	        command = "safaribooks --cred {0} {1}".format(credentials, book)
	        print(command)
	        os.system(command)
	    else:
	        print("BookId %s bereits vorhanden.", book)

if __name__ == "__main__":
    arguments = argparse.ArgumentParser(prog="run_script.py",
                                        description="Download and generate an EPUB of your favorite books"
                                                    " from Safari Books Online.",
                                        add_help=False,
                                        allow_abbrev=False)

    arguments.add_argument(
        "--cred", metavar="<EMAIL:PASS>",
        help="Credentials used to perform the auth login on Safari Books Online."
             " Es. ` --cred \"account_mail@mail.com:password01\" `."
    )

    args_parsed = arguments.parse_args()

    run_app(credentials=args_parsed.cred)
