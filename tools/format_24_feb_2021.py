import json
import os
import re

filepath = os.path.join(os.path.dirname(__file__), '..', 'jee_mains_24_feb_2021_shift_1', 'jee_mains_24_feb_2021_shift_1.json')

with open(filepath, 'r', encoding='utf-8') as f:
    paper = json.load(f)

updates = {
    "phys_q19": {
        "questionText": "Consider two satellites $S_1$ and $S_2$ with periods of revolution $1\\text{ hr}$ and $8\\text{ hr}$ respectively revolving around a planet in circular orbits. The ratio of angular velocity of satellite $S_1$ to the angular velocity of satellite $S_2$ is :",
        "options": [
            {"id": "1", "text": "$8 : 1$", "isCorrect": True},
            {"id": "2", "text": "$1 : 4$", "isCorrect": False},
            {"id": "3", "text": "$2 : 1$", "isCorrect": False},
            {"id": "4", "text": "$1 : 8$", "isCorrect": False}
        ]
    },
    "chem_q11": {
        "questionText": "What is the major product formed by $\\text{HI}$ on reaction with $\\text{CH}_3-\\text{C}(\\text{CH}_3)=\\text{CH}-\\text{CH}_2-\\text{CH}_3$ ?",
        "options": [
            {"id": "1", "text": "$\\text{CH}_3-\\text{CH}(\\text{CH}_3)-\\text{CH}(\\text{I})-\\text{CH}_2-\\text{CH}_3$", "isCorrect": False},
            {"id": "2", "text": "$\\text{CH}_3-\\text{C}(\\text{CH}_3)_2-\\text{CH}_2-\\text{CH}_2-\\text{I}$", "isCorrect": False},
            {"id": "3", "text": "$\\text{CH}_3-\\text{C}(\\text{I})(\\text{CH}_3)-\\text{CH}_2-\\text{CH}_2-\\text{CH}_3$", "isCorrect": True},
            {"id": "4", "text": "$\\text{CH}_3-\\text{CH}(\\text{CH}_3)-\\text{CH}_2-\\text{CH}(\\text{I})-\\text{CH}_3$", "isCorrect": False}
        ]
    },
    "chem_q12": {
        "questionText": "Which of the following reagent is used for the reaction : $\\text{CH}_3-\\text{CH}_2-\\text{CH}_3 \\to \\text{CH}_3-\\text{CH}_2-\\text{CHO}$ ?",
        "options": [
            {"id": "1", "text": "Manganese acetate", "isCorrect": False},
            {"id": "2", "text": "Copper at high temperature and pressure", "isCorrect": False},
            {"id": "3", "text": "Molybdenum oxide", "isCorrect": True},
            {"id": "4", "text": "Potassium permanganate", "isCorrect": False}
        ]
    },
    "chem_q19": {
        "questionText": "Identify products $A$ and $B$ in the sequence : toluene $\\xrightarrow[273\\text{ K}]{\\text{dil. }\\text{KMnO}_4} A \\xrightarrow{\\text{CrO}_3} B$ :",
        "options": [
            {"id": "1", "text": "$A$ : 1-methylcyclohexa-3,5-diene-1,2-diol, $B$ : ketone", "isCorrect": False},
            {"id": "2", "text": "$A$ : diol, $B$ : dicarboxylic acid", "isCorrect": True},
            {"id": "3", "text": "$A$ : aldehyde, $B$ : acid", "isCorrect": False},
            {"id": "4", "text": "$A$ : alcohol, $B$ : aldehyde", "isCorrect": False}
        ]
    },
    "chem_q22": {
        "questionText": "$4.5\\text{ g}$ of compound $A$ ($\\text{MW} = 90$) was used to make $250\\text{ mL}$ of its aqueous solution. The molarity of the solution in $\\text{M}$ is $x \\times 10^{-1}$. The value of $x$ is _______ (Rounded off to the nearest integer).",
        "explanation": "Molarity $M = \\frac{4.5 / 90}{250 / 1000} = 0.2\\text{ M} = 2 \\times 10^{-1}\\text{ M} \\implies x = 2$.",
        "answer": 2.0
    },
    "math_q2": {
        "questionText": "A man is walking on a straight line. The arithmetic mean of the reciprocals of the intercepts of this line on the coordinate axes is $\\frac{1}{4}$. Three stones $A, B$ and $C$ are placed at the points $(1,1)$, $(2, 2)$ and $(4, 4)$ respectively. Then which of these stones is / are on the path of the man ?",
        "options": [
            {"id": "1", "text": "$A$ only", "isCorrect": False},
            {"id": "2", "text": "$C$ only", "isCorrect": False},
            {"id": "3", "text": "All the three", "isCorrect": False},
            {"id": "4", "text": "$B$ only", "isCorrect": True}
        ],
        "explanation": "Let the line be $\\frac{x}{a} + \\frac{y}{b} = 1$. The arithmetic mean of reciprocals of intercepts is $\\frac{1}{2}\\left(\\frac{1}{a} + \\frac{1}{b}\\right) = \\frac{1}{4} \\implies \\frac{1}{a} + \\frac{1}{b} = \\frac{1}{2} \\implies \\frac{2}{a} + \\frac{2}{b} = 1$. Comparing with $\\frac{x}{a} + \\frac{y}{b} = 1$, the line always passes through $(2, 2)$, which is point $B$."
    },
    "math_q3": {
        "questionText": "The equation of the plane passing through the point $(1, 2, -3)$ and perpendicular to the planes $3x + y - 2z = 5$ and $2x - 5y - z = 7$ is :",
        "options": [
            {"id": "1", "text": "$3x - 10y - 2z + 11 = 0$", "isCorrect": False},
            {"id": "2", "text": "$6x - 5y - 2z - 2 = 0$", "isCorrect": False},
            {"id": "3", "text": "$11x + y + 17z + 38 = 0$", "isCorrect": True},
            {"id": "4", "text": "$6x - 5y + 2z + 10 = 0$", "isCorrect": False}
        ]
    },
    "math_q4": {
        "questionText": "The population $P = P(t)$ at time '$t$' of a certain species follows the differential equation $\\frac{dP}{dt} = 0.5P - 450$. If $P(0) = 850$, then the time at which population becomes zero is :",
        "options": [
            {"id": "1", "text": "$\\log_e 18$", "isCorrect": False},
            {"id": "2", "text": "$\\log_e 9$", "isCorrect": False},
            {"id": "3", "text": "$\\frac{1}{2}\\log_e 18$", "isCorrect": False},
            {"id": "4", "text": "$2\\log_e 18$", "isCorrect": True}
        ]
    },
    "math_q5": {
        "questionText": "The system of linear equations:\n$$\\begin{aligned} 3x - 2y - kz &= 10 \\\\ 2x - 4y - 2z &= 6 \\\\ x + 2y - z &= 5m \\end{aligned}$$\nis inconsistent if :",
        "options": [
            {"id": "1", "text": "$k = 3, m = \\frac{4}{5}$", "isCorrect": False},
            {"id": "2", "text": "$k \\neq 3, m \\in \\mathbb{R}$", "isCorrect": False},
            {"id": "3", "text": "$k \\neq 3, m \\neq \\frac{4}{5}$", "isCorrect": False},
            {"id": "4", "text": "$k = 3, m \\neq \\frac{4}{5}$", "isCorrect": True}
        ]
    },
    "math_q6": {
        "questionText": "If $f : \\mathbb{R} \\to \\mathbb{R}$ is a function defined by $f(x) = [x - 1]\\cos\\left(\\frac{2x - 1}{2}\\pi\\right)$, where $[.]$ denotes the greatest integer function, then $f$ is :",
        "options": [
            {"id": "1", "text": "discontinuous at all integral points", "isCorrect": False},
            {"id": "2", "text": "continuous only at $x = 1$", "isCorrect": False},
            {"id": "3", "text": "continuous for every real $x$", "isCorrect": True},
            {"id": "4", "text": "discontinuous only at $x = 1$", "isCorrect": False}
        ]
    },
    "math_q7": {
        "questionText": "The distance of the point $(1, 1, 9)$ from the point of intersection of the line $\\frac{x-3}{1} = \\frac{y-4}{2} = \\frac{z-5}{2}$ and the plane $x + y + z = 17$ is :",
        "options": [
            {"id": "1", "text": "$2\\sqrt{19}$", "isCorrect": False},
            {"id": "2", "text": "$\\frac{\\sqrt{19}}{2}$", "isCorrect": False},
            {"id": "3", "text": "38", "isCorrect": False},
            {"id": "4", "text": "$\\sqrt{38}$", "isCorrect": True}
        ]
    },
    "math_q8": {
        "questionText": "If the tangent to the curve $y = x^3$ at the point $P(t, t^3)$ meets the curve again at $Q$, then the ordinate of the point which divides $PQ$ internally in the ratio $1 : 2$ is :",
        "options": [
            {"id": "1", "text": "$-2t^3$", "isCorrect": True},
            {"id": "2", "text": "0", "isCorrect": False},
            {"id": "3", "text": "$-t^3$", "isCorrect": False},
            {"id": "4", "text": "$2t^3$", "isCorrect": False}
        ]
    },
    "math_q10": {
        "questionText": "The value of $-{}^{15}\\text{C}_1 + 2\\cdot{}^{15}\\text{C}_2 - 3\\cdot{}^{15}\\text{C}_3 + \\dots - 15\\cdot{}^{15}\\text{C}_{15} + {}^{14}\\text{C}_1 + {}^{14}\\text{C}_3 + \\dots + {}^{14}\\text{C}_{11}$ is :",
        "options": [
            {"id": "1", "text": "$2^{16} - 1$", "isCorrect": False},
            {"id": "2", "text": "$2^{13} - 14$", "isCorrect": True},
            {"id": "3", "text": "$2^{14}$", "isCorrect": False},
            {"id": "4", "text": "$2^{13} - 13$", "isCorrect": False}
        ]
    },
    "math_q15": {
        "questionText": "The area (in sq. units) of the part of the circle $x^2 + y^2 = 36$, which is outside the parabola $y^2 = 9x$, is :",
        "options": [
            {"id": "1", "text": "$24\\pi + 3\\sqrt{3}$", "isCorrect": False},
            {"id": "2", "text": "$12\\pi - 3\\sqrt{3}$", "isCorrect": False},
            {"id": "3", "text": "$24\\pi - 3\\sqrt{3}$", "isCorrect": True},
            {"id": "4", "text": "$12\\pi + 3\\sqrt{3}$", "isCorrect": False}
        ]
    },
    "math_q16": {
        "questionText": "Let $p$ and $q$ be two positive numbers such that $p + q = 2$ and $p^4 + q^4 = 272$. Then $p$ and $q$ are roots of :",
        "options": [
            {"id": "1", "text": "$x^2 - 2x + 2 = 0$", "isCorrect": False},
            {"id": "2", "text": "$x^2 - 2x + 8 = 0$", "isCorrect": False},
            {"id": "3", "text": "$x^2 - 2x + 136 = 0$", "isCorrect": False},
            {"id": "4", "text": "$x^2 - 2x + 16 = 0$", "isCorrect": True}
        ]
    },
    "math_q18": {
        "questionText": "$\\lim_{x \\to 0} \\frac{\\int_0^{x^2} \\sin\\sqrt{t}\\,dt}{x^3}$ is equal to :",
        "options": [
            {"id": "1", "text": "$\\frac{2}{3}$", "isCorrect": True},
            {"id": "2", "text": "$\\frac{3}{2}$", "isCorrect": False},
            {"id": "3", "text": "0", "isCorrect": False},
            {"id": "4", "text": "$\\frac{1}{15}$", "isCorrect": False}
        ]
    },
    "math_q19": {
        "questionText": "If $e^{(\\cos^2 x + \\cos^4 x + \\cos^6 x + \\dots)\\ln 2}$ satisfies the equation $t^2 - 9t + 8 = 0$, then the value of $\\frac{2\\sin x}{\\sin x + \\sqrt{3}\\cos x}$ for $0 < x < \\frac{\\pi}{2}$ is :",
        "options": [
            {"id": "1", "text": "$\\frac{2}{3}$", "isCorrect": False},
            {"id": "2", "text": "$\\frac{3}{2}$", "isCorrect": False},
            {"id": "3", "text": "$\\sqrt{3}$", "isCorrect": False},
            {"id": "4", "text": "$\\frac{1}{2}$", "isCorrect": True}
        ]
    },
    "math_q21": {
        "questionText": "If the least and the largest real values of $\\alpha$, for which the equation $z + \\alpha|z - 1| + 2i = 0$ ($z \\in \\mathbb{C}$ and $i = \\sqrt{-1}$) has a solution, are $p$ and $q$ respectively, then $4(p^2 + q^2)$ is equal to _______."
    },
    "math_q22": {
        "questionText": "If $\\int_{-a}^a (|x| + |x-2|)\\,dx = 22, \\ (a > 2)$ and $[x]$ denotes the greatest integer $\\le x$, then $\\int_{-a}^a (x + [x])\\,dx$ is equal to _______."
    },
    "math_q26": {
        "questionText": "The minimum value of $\\alpha$ for which the equation $\\frac{4}{\\sin x} + \\frac{1}{1 - \\sin x} = \\alpha$ has at least one solution in $(0, \\frac{\\pi}{2})$ is _______."
    },
    "math_q27": {
        "questionText": "$\\lim_{n \\to \\infty} \\tan\\left(\\sum_{r=1}^n \\tan^{-1}\\left(\\frac{1}{1 + r + r^2}\\right)\\right)$ is equal to _______."
    }
}

for s in paper['sections']:
    for sub in s.get('subsections', []):
        for q in sub.get('questions', []):
            qid = q['id']
            if qid in updates:
                for k, v in updates[qid].items():
                    q[k] = v

# Clean up  across all questions in the paper
def clean_char(val):
    if isinstance(val, str):
        val = val.replace('\u2013', '-').replace('\u2014', '-').replace('\xad', '')
        val = val.replace('p = 3.14', r'$\pi = 3.14$')
        val = val.replace('W respectively', r'$\Omega$ respectively')
        val = val.replace('oC', r'$^\circ\text{C}$')
    return val

for s in paper['sections']:
    for sub in s.get('subsections', []):
        for q in sub.get('questions', []):
            q['questionText'] = clean_char(q.get('questionText', ''))
            q['explanation'] = clean_char(q.get('explanation', ''))
            for o in q.get('options', []):
                o['text'] = clean_char(o.get('text', ''))

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(paper, f, indent=2, ensure_ascii=False)
    f.write('\n')

print("Successfully updated jee_mains_24_feb_2021_shift_1.json!")
