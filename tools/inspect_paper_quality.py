import json
import os
import re
import sys

# Ensure UTF-8 output even on Windows console
sys.stdout.reconfigure(encoding='utf-8')

BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(BACKEND_DIR, 'manifest.json'), 'r', encoding='utf-8') as f:
    manifest = json.load(f)

def inspect_paper(paper_id):
    paper_info = next((p for p in manifest['papers'] if p['id'] == paper_id), None)
    if not paper_info:
        print(f"Paper {paper_id} not found in manifest!")
        return
        
    filepath = os.path.join(BACKEND_DIR, paper_info['filename'])
    with open(filepath, 'r', encoding='utf-8') as pf:
        d = json.load(pf)
        
    print(f"=== Paper: {d.get('examTitle', paper_id)} ({paper_info['filename']}) ===")
    
    total_qs = 0
    raw_math_issues = []
    pua_issues = []
    spaces_in_numbers = []
    broken_subscripts = []
    
    for s_idx, s in enumerate(d.get('sections', [])):
        qs = list(s.get('questions', []))
        for sub in s.get('subsections', []):
            qs.extend(sub.get('questions', []))
        for q in qs:
            total_qs += 1
            qid = q.get('id', 'unknown')
            t = q.get('questionText', '')
            
            # Check for PUA characters
            pua = [c for c in t if 0xe000 <= ord(c) <= 0xf8ff]
            if pua:
                pua_issues.append((qid, len(pua), t[:80]))
                
            # Check for unenclosed math commands outside $...$
            no_math = re.sub(r'\$\$[\s\S]*?\$\$', '', t)
            no_math = re.sub(r'\$[\s\S]*?\$', '', no_math)
            outside_cmds = re.findall(r'\\([a-zA-Z]{2,})', no_math)
            math_cmds = [c for c in outside_cmds if c in (
                'alpha', 'beta', 'gamma', 'delta', 'lambda', 'mu', 'theta', 'pi', 'sigma',
                'frac', 'sqrt', 'vec', 'hat', 'sum', 'int', 'infty', 'le', 'ge', 'pm', 'times', 'div', 'in', 'ne'
            )]
            if math_cmds:
                raw_math_issues.append((qid, math_cmds, t[:80]))
                
            # Check for broken chemistry or numbers with space like '0. 1 M' or 'CH 3 COOH'
            if re.search(r'\b0\.\s+\d+', t) or re.search(r'\b[A-Z][a-z]?\s+\d+\b', t):
                spaces_in_numbers.append((qid, t[:80]))
                
    print(f"Total Questions: {total_qs}")
    print(f"Raw math commands outside $: {len(raw_math_issues)}")
    for qid, cmds, snippet in raw_math_issues[:5]:
        print(f"  [{qid}] commands: {cmds} -> {snippet}")
    print(f"PUA / bad glyph issues: {len(pua_issues)}")
    for qid, cnt, snippet in pua_issues[:5]:
        print(f"  [{qid}] {cnt} glyphs -> {snippet}")
    print(f"Spaced chemical formulas / decimals: {len(spaces_in_numbers)}")
    for qid, snippet in spaces_in_numbers[:5]:
        print(f"  [{qid}] -> {snippet}")
    print()

if __name__ == '__main__':
    for p in manifest['papers']:
        inspect_paper(p['id'])
