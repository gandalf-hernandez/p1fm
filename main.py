#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import templates

genres = ('Metal', 'Pop', 'Hip Hop', 'Alternative', 'R and B', 'Country',)

class MainMenuHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(templates.en['main_menu'])

class GenreMenuHandler(webapp2.RequestHandler):
    def get(self):
        template = templates.es if self.request.GET['Digits'] == '2' else templates.en
        self.response.write(template['genre_menu'] % ''.join(
            template['option'] % (number, genre) for number, genre in enumerate(genres, start=1)
            ))

class RadioHandler(webapp2.RequestHandler):
    def get(self):
        template = templates.es if self.request.GET['language'] == 'es' else templates.en
        digit = int(self.request.GET['Digits'])

        if digit == 4:
            self.response.write(template['rickroll'])
            return
        try:
            with open('lyrics/%d' % digit) as f:
                track = template['track'] % (
                        f.next().strip(),
                        ''.join(template['say'] % line.strip() for line in f),)
        except IOError:
            self.response.write(template['error_try_later'])
            return
        self.response.write(template['radio'] % (genres[digit-1], track,))

app = webapp2.WSGIApplication([
    ('/', MainMenuHandler),
    ('/genre_menu', GenreMenuHandler),
    ('/radio', RadioHandler)
], debug=True)
