import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect(paper_path):
    with open(paper_path, 'r', encoding='utf-8') as f:
        d = json.load(f)

    print(f"Total Sections: {len(d['sections'])}")
    for s in d['sections']:
        s_name = s['name']
        for sub in s.get('subsections', []):
            sub_name = sub['name']
            qs = sub.get('questions', [])
            print(f"--- Section: {s_name} | {sub_name} ({len(qs)} questions) ---")
            for q in qs:
                qid = q['id']
                t = q.get('questionText', '')
                opts = [o.get('text', '') for o in q.get('options', [])]
                img = q.get('imageName') if q.get('hasImage') else None
                print(f"[{qid}] img={img}")
                print(f"  Q: {t}")
                if opts:
                    print(f"  O: {opts}")

if __name__ == '__main__':
    inspect(sys.argv[1])
