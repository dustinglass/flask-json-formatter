from flask import Flask, request, make_response, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/format')
def format():
    full_text = request.args.get('full_text', '')
    if int(request.args.get('quotes', 0)) == 1:
        quote = '\''
    else:
        quote = '"'
    tabs = int(request.args.get('tabs', 2))
    lines = []
    for n, line in enumerate(full_text.splitlines()):
        kv = ['{}{}{}'.format(quote, i.strip(), quote) 
              for i in line.split(': ', 1)]
        if len(full_text.splitlines()) - n > 1:
            lines.append(': '.join(kv) + ',')
        else:
            lines.append(': '.join(kv))
    return render_template('format.html', **{
        'full_text': full_text,
        'lines': lines,
        'tab': '&nbsp;' * tabs
    })


if __name__ == "__main__":
    app.run(debug=True)