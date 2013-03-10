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


response = '''
<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Gather action="/play" method="GET">
            <Say>
                Press 1 for Metal
            </Say>
        </Gather>
    <Say>We didn't receive any input. Goodbye!</Say>
</Response>
'''

lyrics_template = '''
<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say>
        %s
        </Say>
    </Response>
'''


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(response)


class PlayHandler(webapp2.RequestHandler):
    def get(self):
        digit = 1

        with open('lyrics/%d' % digit) as f:
            lyrics = f.read()
        self.response.write(lyrics_template % lyrics)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/play', PlayHandler)
], debug=True)
