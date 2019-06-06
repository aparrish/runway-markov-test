import runway
from runway.data_types import text, number

import gzip

from markovify import Text

@runway.setup
def setup():
    msg = '[SETUP]'
    with gzip.open('./novel-model-markovify.json.gz') as fh:
        return Text.from_json(fh.read())

@runway.command(name='generate',
                inputs={'max_len': number(default=80, min=10, max=1000)},
                outputs={'output': text()})
def generate(model, args):
    print('[GENERATE] Ran with max_len value "{}"'.format(args['max_len']))
    output = model.make_short_sentence(args['max_len'])
    return {'output': output}

if __name__ == '__main__':
    runway.run(host='0.0.0.0', port=8000)

