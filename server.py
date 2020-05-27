from flask import Flask, Response

app = Flask(__name__)

wav_file = './data_from/sample.wav'

@app.route("/wav")
def streamwav():
    def generate():
        with open(wav_file, "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

"""
@app.route("/ogg")
def streamogg():
    def generate():
        with open("signals/song.ogg", "rb") as fogg:
            data = fogg.read(1024)
            while data:
                yield data
                data = fogg.read(1024)
    return Response(generate(), mimetype="audio/ogg")
"""

if __name__ == "__main__":
    app.run(port=8877, debug=True)
