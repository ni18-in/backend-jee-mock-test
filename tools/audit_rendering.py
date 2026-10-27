import os
import json
import re

BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(BACKEND_DIR, "manifest.json")

def check_latex_syntax(field_name, text, q_id, paper_id):
    issues = []
    if not text:
        return issues
        
    # Check double dollar and single dollar
    dd_matches = list(re.finditer(r'(?<!\\)\$\$', text))
    if len(dd_matches) % 2 != 0:
        issues.append(f"Unbalanced $$ in {field_name}")
        
    temp_text = re.sub(r'(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$', '', text)
    sd_matches = list(re.finditer(r'(?<!\\)\$', temp_text))
    if len(sd_matches) % 2 != 0:
        issues.append(f"Unbalanced $ in {field_name}")

    # Extract all math blocks: $$...$$ and $...$
    math_blocks = re.findall(r'(\$\$[\s\S]*?\$\$|\$[\s\S]*?\$)', text)
    for mb in math_blocks:
        is_block = mb.startswith('$$')
        inner = mb[2:-2] if is_block else mb[1:-1]
        inner_trimmed = inner.strip()
        
        # Check for unescaped percent sign (in KaTeX % is a comment that truncates remainder)
        if re.search(r'(?<!\\)%', inner):
            issues.append(f"Unescaped % inside LaTeX formula ({mb[:40]}...) in {field_name} - truncates formula in KaTeX!")

        # Check for brace balance {}
        open_braces = len(re.findall(r'(?<!\\)\{', inner))
        close_braces = len(re.findall(r'(?<!\\)\}', inner))
        if open_braces != close_braces:
            issues.append(f"Unbalanced braces in LaTeX: '{mb[:50]}...' ({open_braces} '{{' vs {close_braces} '}}') in {field_name}")

        # Check for \begin{env} without \end{env}
        begins = re.findall(r'\\begin\{([a-zA-Z*]+)\}', inner)
        ends = re.findall(r'\\end\{([a-zA-Z*]+)\}', inner)
        if begins != ends:
            issues.append(f"Mismatched \\begin{begins} vs \\end{ends} in LaTeX: '{mb[:50]}' in {field_name}")

        # Check for unsupported packages/commands in KaTeX/flutter_math_fork
        if r'\ce{' in inner:
            issues.append(f"Unsupported \\ce{{}} chem command in KaTeX in {field_name}: '{mb[:50]}'")
        if r'\tabular' in inner:
            issues.append(f"Unsupported \\tabular command in KaTeX in {field_name}: '{mb[:50]}'")

    # Also check if text has unescaped raw control chars like form-feed \x0c or backspace \x08
    if '\x0c' in text:
        issues.append(f"Raw form-feed (\\x0c) in {field_name} (likely unescaped \\f...)")
    if '\x08' in text:
        issues.append(f"Raw backspace (\\x08) in {field_name} (likely unescaped \\b...)")

    return issues

def audit():
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    all_paper_issues = {}
    total_questions = 0

    for p in manifest['papers']:
        p_id = p['id']
        p_filename = p['filename']
        p_path = os.path.join(BACKEND_DIR, p_filename)
        p_dir = os.path.dirname(p_path)

        if not os.path.exists(p_path):
            all_paper_issues[p_id] = [f"File not found: {p_filename}"]
            continue

        with open(p_path, 'r', encoding='utf-8') as pf:
            try:
                data = json.load(pf)
            except Exception as e:
                all_paper_issues[p_id] = [f"JSON parse error: {e}"]
                continue

        p_issues = []
        sections = data.get('sections', [])
        for s_idx, sec in enumerate(sections):
            subsections = sec.get('subsections', [])
            questions = sec.get('questions', [])
            all_qs = list(questions)
            for sub in subsections:
                all_qs.extend(sub.get('questions', []))

            for q_idx, q in enumerate(all_qs):
                total_questions += 1
                q_id = q.get('id', f'sec{s_idx}_q{q_idx}')

                # Check question text
                q_text = q.get('questionText', '')
                p_issues.extend([f"[{q_id}] {iss}" for iss in check_latex_syntax('questionText', q_text, q_id, p_id)])

                # Check options
                for opt in q.get('options', []):
                    opt_id = opt.get('id', '?')
                    opt_text = opt.get('text', '')
                    p_issues.extend([f"[{q_id} opt {opt_id}] {iss}" for iss in check_latex_syntax(f"option_{opt_id}", opt_text, q_id, p_id)])

                # Check explanation
                expl = q.get('explanation', '')
                p_issues.extend([f"[{q_id}] {iss}" for iss in check_latex_syntax('explanation', expl, q_id, p_id)])

                # Check matching items
                for mi in q.get('matchingItems', []):
                    for side in ['leftItems', 'rightItems']:
                        for item in mi.get(side, []):
                            i_text = item.get('text', '')
                            p_issues.extend([f"[{q_id} matching] {iss}" for iss in check_latex_syntax('matchingItem', i_text, q_id, p_id)])

                # Check images
                if q.get('hasImage'):
                    img_name = q.get('imageName')
                    if not img_name:
                        p_issues.append(f"[{q_id}] hasImage is true but imageName is missing/empty")
                    else:
                        img_path = os.path.join(p_dir, img_name)
                        if not os.path.exists(img_path):
                            p_issues.append(f"[{q_id}] Missing image file: {img_name}")

                # Check option images
                for opt in q.get('options', []):
                    if opt.get('hasImage'):
                        opt_img = opt.get('imageName')
                        if opt_img:
                            img_path = os.path.join(p_dir, opt_img)
                            if not os.path.exists(img_path):
                                p_issues.append(f"[{q_id} opt {opt.get('id')}] Missing option image: {opt_img}")

        if p_issues:
            all_paper_issues[p_id] = p_issues

    print(f"Audited {len(manifest['papers'])} papers ({total_questions} questions total).")
    print(f"Papers with issues: {len(all_paper_issues)}")
    for pid, issues in all_paper_issues.items():
        print(f"\n--- Paper: {pid} ({len(issues)} issues) ---")
        for iss in issues[:15]:
            print(f"  • {iss}")
        if len(issues) > 15:
            print(f"  ... and {len(issues) - 15} more issues")

if __name__ == '__main__':
    audit()
