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


response = '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Gather action="/play" method="GET">
        <Say>
            Press 1 for Metal
            Press 2 for Hip Hop
            Press 3 for Pop
            Press 4 for Alternative
            Press 5 for R and B
            Press 6 for Country
        </Say>
    </Gather>
<Say>We didn't receive any input. Goodbye!</Say>
</Response>
'''

lyrics_template = '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>
    Playing %s radio.

    %s
    </Say>
</Response>
'''

lyrics_error = '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>
       Oops. Sorry.
    </Say>
</Response>
'''

rickroll = '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play loop="10">https://dl.dropbox.com/u/11675551/rickroll.mp3</Play>
</Response>
'''

genres = ['', 'metal', 'hip hop', 'pop', 'alternative', 'R&B', 'Country']


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(response)


class PlayHandler(webapp2.RequestHandler):
    def get(self):
        digit = int(self.request.GET['Digits'])

        if digit == 5:
            self.response.write(rickroll)
            return
        try:
            with open('lyrics/%d' % digit) as f:
                lyrics = f.read()
        except IOError:
            self.response.write(lyrics_error)
            return

        self.response.write(lyrics_template % (genres[digit], lyrics))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/play', PlayHandler)
], debug=True)
