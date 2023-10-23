from flask import request, jsonify, send_file
from flask_cors import cross_origin
import json

from opensubtitlescom import OpenSubtitles
from util import SubtitleJSONEncoder

from app import app

subtitles = OpenSubtitles(app.config["OPENSUB_KEY"], "Language Flashcards 1.0")
subtitles.login(app.config["OPENSUB_USER"], app.config["OPENSUB_PASS"])

@app.route("/")
def hello():
    return "Hello!"

# @app.route("/api/test")
# def test1():
#     response = subtitles.search(query="breaking bad", episode_number=1, season_number=1, languages="en")
#     response_dict = response.to_dict()
#     srt = subtitles.download_and_parse(response.data[0])
#     return json.dumps(srt, cls=SubtitleJSONEncoder)