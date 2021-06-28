# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re


class Parser:
    def get(self, response, page):

        channel = {
            'page': 1,
            'page_patten': None,
            'movies': []
        }

        soup = BeautifulSoup(response, "html.parser")
        tab = soup.find('div', {'class': 'tab-pane', 'id': page})

        movies = re.findall(r'li\sclass="channel".*href="(.*?)".*src="(.*?)".*title="(.*?)"', str(tab))
        for movie in movies:
            # try:
            channel['movies'].append({
                'id': movie[0],
                'label': movie[2],
                'title': movie[2],
                'realtitle': movie[2],
                'thumb': movie[1],
                'type': movie[2]
            })

        return channel
