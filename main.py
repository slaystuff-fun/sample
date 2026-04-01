from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Layspeaksa Eneratorga</title>
    <style>
        body {
            font-family: sans-serif;
            max-width: 640px;
            margin: 60px auto;
            padding: 0 24px;
            background: #fff;
            color: #111;
        }
        h1 { font-size: 2em; margin-bottom: 4px; }
        p { color: #555; margin-top: 0; }
        textarea {
            width: 100%;
            height: 130px;
            font-size: 1em;
            padding: 10px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
            resize: vertical;
        }
        button {
            margin-top: 10px;
            padding: 10px 28px;
            font-size: 1em;
            background: #111;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover { background: #333; }
        #output {
            margin-top: 20px;
            padding: 14px;
            background: #f5f5f5;
            border-radius: 4px;
            min-height: 60px;
            font-size: 1em;
            white-space: pre-wrap;
            word-break: break-word;
        }
        #output:empty::before {
            content: 'Outputway illwa appearway errhay...';
            color: #aaa;
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>Layspeaksa Eneratorga</h1>
    <p>Ypeta omesay exttay andway esspray ethay uttonbay otay anslatetray itway intoway Layspeaksa.</p>

    <textarea id="input" placeholder="Enter text here..."></textarea>
    <br>
    <button type="button" onclick="translate()">Eneratega!</button>

    <div id="output"></div>

    <script>
        const VOWELS = new Set('aeiouAEIOU');

        function pigLatinWord(word) {
            const match = word.match(/^([^a-zA-Z]*)([a-zA-Z]+)([^a-zA-Z]*)$/);
            if (!match) return word;
            const [, pre, core, post] = match;

            if (VOWELS.has(core[0])) {
                return pre + core + 'way' + post;
            }

            let i = 0;
            while (i < core.length && !VOWELS.has(core[i])) i++;

            if (i === core.length) {
                return pre + core + 'ay' + post;
            }

            const cluster = core.slice(0, i).toLowerCase();
            const rest = core.slice(i);
            return pre + rest + cluster + 'ay' + post;
        }

        function translate() {
            const input = document.getElementById('input').value.trim();
            if (!input) return;
            const result = input.replace(/\\S+/g, pigLatinWord);
            document.getElementById('output').textContent = result;
        }

        document.getElementById('input').addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) translate();
        });
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
