import json
from pathlib import Path
BASE = Path(__file__).parent
SYN = {x['term'].lower(): x['normalized'] for x in json.loads((BASE/'data'/'synonyms.json').read_text(encoding='utf-8'))}
MAP = {'lumelükkamine': 'lumelükkamine', 'oilfuel': 'oilfuel', 'terrass': 'terrass', 'sadam': 'sadam', 'ehitus': 'ehitus', 'aknatihend': 'aknatihend'}

def detect(q):
    t=q.lower()
    for term,cat in SYN.items():
        if term in t:
            return cat
    return 'aknatihend'

if __name__ == '__main__':
    import sys
    q = ' ' .join(sys.argv[1:]) if len(sys.argv)>1 else 'sahk'
    print(detect(q))
