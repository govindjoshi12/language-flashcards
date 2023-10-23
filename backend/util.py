import json
from opensubtitlescom import srt, responses
from datetime import date, datetime, timedelta

class SubtitleJSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, (srt.Subtitle, responses.Subtitle)):
            return o.__dict__
        elif isinstance(o, (datetime, date)):
            # Can rewrite to fit my needs
            return o.isoformat()
        elif isinstance(o, timedelta):
            return str(o)
        return super().default(o)