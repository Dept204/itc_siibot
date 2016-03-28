import requests
from lxml import html


class ITCSII:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.url = 'https://sii.itcelaya.edu.mx/sii/index.php?r=cruge/ui/login'

    def set_userdata(self, user, password):
        self.username = user
        self.password = password

    def get_grades(self):
        payload = {'CrugeLogon[username]': self.username, 'CrugeLogon[password]': self.password}
        r = requests.get(self.url)  # Fetch the original website
        # POST payloads
        r = requests.post(self.url, data=payload)
        tree = html.fromstring(r.content)  # Parses the website
        table = tree.xpath('//td/text()')  # Gets data from tables
        # Clean table
        results = ''
        newline = True
        for element in table:
            if len(element) == 4:
                results += '\n'
                results += element + ' '
            elif len(element) >= 2:
                results += element.rstrip().lstrip() + ' '
        return results
