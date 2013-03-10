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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(templates.menu % ''.join(
            templates.option % (number, genre) for number, genre in enumerate(genres, start=1)
            ))

class PlayHandler(webapp2.RequestHandler):
    def get(self):
        digit = int(self.request.GET['Digits'])

        if digit == 5:
            self.response.write(templates.rickroll)
            return
        try:
            with open('lyrics/%d' % digit) as f:
                lyrics = ''.join(templates.say % line.strip() for line in f)
        except IOError:
            self.response.write(lyrics_error)
            return
        self.response.write(templates.radio % (genres[digit-1], lyrics,))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/play', PlayHandler)
], debug=True)
