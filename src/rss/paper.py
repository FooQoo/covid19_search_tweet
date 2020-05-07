import requests
from requests.exceptions import Timeout, HTTPError
import traceback


class PaperAPI:

    def fetch_paper(self, url):

        try:
            r = requests.get(url)
            r.raise_for_status()

            return r.text

        except Timeout:
            print(traceback.print_exc())
        except HTTPError:
            print(traceback.print_exc())

        return ""
