import unittest

import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("I'm having a party", result.data)

    def test_no_rsvp_yet(self):
        result = self.client.get("/")
        self.assertIn("<h2>Please RSVP</h2>", result.data)

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={'name': "Jane", 'email': "jane@jane.com"},
                                  follow_redirects=True)

        self.assertIn("Party Details", result.data)


    def test_rsvp_mel(self):
        result = self.client.post("/rsvp",
                                  data={'name': "Mel", 'email': "mel@ubermelon.com"},
                                  follow_redirects=True)

        self.assertNotIn("Party Details", result.data)



if __name__ == "__main__":
    unittest.main()