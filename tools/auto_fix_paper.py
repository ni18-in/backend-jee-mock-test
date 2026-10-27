import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MATH_COMMANDS = [
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'varepsilon', 'zeta', 'eta', 'theta',
    'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'pi', 'rho', 'sigma', 'tau', 'phi', 'chi', 'psi', 'omega',
    'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Phi', 'Psi', 'Omega',
    'frac', 'sqrt', 'vec', 'hat', 'bar', 'dot', 'sum', 'int', 'prod', 'lim', 'infty',
    'le', 'ge', 'leq', 'geq', 'pm', 'mp', 'times', 'div', 'cdot', 'in', 'notin', 'ne', 'neq',
    'approx', 'equiv', 'subset', 'supset', 'subseteq', 'supseteq', 'cap', 'cup', 'land', 'lor',
    'sim', 'because', 'therefore', 'circ', 'degree'
]

PUA_REPLACEMENTS = {
    '\uf07e': '~',
    '\uf051': r'$\because$',
    '\uf0ec': '<',
    '\uf0ed': '=',
    '\uf0ee': '>',
    '\uf0ef': r'$\le$',
    '\uf0b0': '°',
    '\uf07b': '{',
    '\uf07d': '}',
    '\uf020': ' ',
    '\uf02b': '+',
    '\uf02d': '-',
    '\uf0b1': r'$\pm$',
    '\uf0d7': r'$\times$',
    '\uf028': '(',
    '\uf029': ')',
    '\uf05b': '[',
    '\uf05d': ']',
    '\uf02c': ',',
    '\uf02e': '.',
    '\uf02f': '/',
    '\uf03a': ':',
    '\uf03b': ';',
    '\uf03d': '=',
    '\uf03c': '<',
    '\uf03e': '>',
    '\uf03f': '?',
    '\uf040': '@',
}

def clean_and_enclose(text):
    if not text:
        return text

    # 1. Clean PUA glyphs
    for pua_char, repl in PUA_REPLACEMENTS.items():
        text = text.replace(pua_char, repl)
    # Strip any remaining unmapped PUA
    text = re.sub(r'[\ue000-\uf8ff]', '', text)

    # 2. Extract existing LaTeX blocks so we don't mess with them
    blocks = []
    def save_block(m):
        blocks.append(m.group(0))
        return f"\u2060MATHBLOCK{len(blocks)-1}\u2060"

    text = re.sub(r'\$\$[\s\S]*?\$\$', save_block, text)
    text = re.sub(r'\$[\s\S]*?\$', save_block, text)

    def wrap_and_protect(m):
        blocks.append(f"${m.group(0)}$")
        return f"\u2060MATHBLOCK{len(blocks)-1}\u2060"

    # 3. Auto-wrap complex LaTeX macros: e.g. \sqrt{...}, \frac{...}{...}, \vec{...}, \hat{...}
    text = re.sub(
        r'\\(sqrt|frac|vec|hat|bar|dot|tilde|text|mathrm|mathbf)(\{[^{}]*\})+',
        wrap_and_protect,
        text
    )

    # 4. Auto-wrap degree expressions: e.g. 60^\circ or 60\circ
    def wrap_degree(m):
        blocks.append(f"${m.group(1)}^\\circ$")
        return f"\u2060MATHBLOCK{len(blocks)-1}\u2060"

    text = re.sub(
        r'\b(\d+)\s*\^?\s*\\circ\b',
        wrap_degree,
        text
    )

    # Remove macro names that take arguments from MATH_COMMANDS so they are not split
    standalone_cmds = [c for c in MATH_COMMANDS if c not in ('sqrt', 'frac', 'vec', 'hat', 'bar', 'dot', 'tilde', 'text', 'mathrm', 'mathbf')]
    pattern = r'\\(' + '|'.join(standalone_cmds) + r')\b'
    text = re.sub(
        pattern,
        wrap_and_protect,
        text
    )

    # 7. Restore protected blocks
    for idx, b in enumerate(blocks):
        text = text.replace(f"\u2060MATHBLOCK{idx}\u2060", b)

    return text

def clean_paper(filename):
    filepath = os.path.join(BACKEND_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    count = 0
    for s in data.get('sections', []):
        for sub in s.get('subsections', []):
            for q in sub.get('questions', []):
                old_q = q.get('questionText', '')
                new_q = clean_and_enclose(old_q)
                if new_q != old_q:
                    q['questionText'] = new_q
                    count += 1

                for opt in q.get('options', []):
                    old_opt = opt.get('text', '')
                    new_opt = clean_and_enclose(old_opt)
                    if new_opt != old_opt:
                        opt['text'] = new_opt
                        count += 1

                old_exp = q.get('explanation', '')
                new_exp = clean_and_enclose(old_exp)
                if new_exp != old_exp:
                    q['explanation'] = new_exp
                    count += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')

    print(f"Updated {filename}: {count} fields formatted.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        clean_paper(sys.argv[1])
    else:
        print("Usage: python auto_fix_paper.py <filename>")
