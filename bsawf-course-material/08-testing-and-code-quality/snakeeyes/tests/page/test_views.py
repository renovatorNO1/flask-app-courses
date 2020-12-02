from flask import url_for
import re

class TestPage(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_cash_flow_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('page.cash_flow'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """ Terms page should respond with a success 200. """
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_title(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('page.privacy'))
        assert '<title>' in  str(response.data)

    def test_title_full_tag(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('page.privacy'))
        assert 'title' in re.search('<title>.*<\/title>', str(response.data) ).group()
