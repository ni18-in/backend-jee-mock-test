import json
import os

filepath = os.path.join(os.path.dirname(__file__), '..', 'jee_mains_04_apr_2025_shift_2', 'jee_mains_04_apr_2025_shift_2.json')

with open(filepath, 'r', encoding='utf-8') as f:
    paper = json.load(f)

updates = {
    "q2": {
        "questionText": "There are '$n$' number of identical electric bulbs, each is designed to draw a power $p$ independently from the mains supply. They are now joined in series across the main supply. The total power drawn by the combination is :",
        "options": [
            {"id": "1", "text": "$np$", "isCorrect": False},
            {"id": "2", "text": "$\\frac{p}{n^2}$", "isCorrect": False},
            {"id": "3", "text": "$p$", "isCorrect": False},
            {"id": "4", "text": "$\\frac{p}{n}$", "isCorrect": True}
        ]
    },
    "q7": {
        "questionText": "A metallic ring is uniformly charged as shown in figure. $AC$ and $BD$ are two mutually perpendicular diameters. Electric field due to arc $AB$ at $O$ has magnitude $E$. What would be the magnitude of electric field at $O$ due to arc $ABC$ ?",
        "options": [
            {"id": "1", "text": "$2E$", "isCorrect": False},
            {"id": "2", "text": "$\\sqrt{2}E$", "isCorrect": True},
            {"id": "3", "text": "$E/2$", "isCorrect": False},
            {"id": "4", "text": "Zero", "isCorrect": False}
        ]
    },
    "q9": {
        "questionText": "The escape velocity of a body from the surface of the earth is $v_e = \\sqrt{\\frac{2GM}{R}}$. If the radius of the earth is doubled keeping its mass constant, then the new escape velocity will be :",
        "options": [
            {"id": "1", "text": "$v_e$", "isCorrect": False},
            {"id": "2", "text": "$\\frac{v_e}{2}$", "isCorrect": False},
            {"id": "3", "text": "$\\sqrt{\\frac{3GM}{R}}$", "isCorrect": False},
            {"id": "4", "text": "$\\frac{v_e}{\\sqrt{2}}$", "isCorrect": True}
        ]
    },
    "q12": {
        "questionText": "A particle executes simple harmonic motion of amplitude $A$. At what distance from the mean position is its kinetic energy equal to its potential energy?",
        "options": [
            {"id": "1", "text": "$\\frac{A}{\\sqrt{2}}$", "isCorrect": True},
            {"id": "2", "text": "$\\frac{A}{2}$", "isCorrect": False},
            {"id": "3", "text": "$\\frac{A}{4}$", "isCorrect": False},
            {"id": "4", "text": "$\\frac{\\sqrt{3}A}{2}$", "isCorrect": False}
        ]
    },
    "q51": {
        "questionText": "Let $a > 0$. If the function $f(x) = 6x^3 - 45ax^2 + 108a^2x + 1$ attains its local maximum and minimum values at the points $x_1$ and $x_2$ respectively such that $x_1 x_2 = 54$, then $a + x_1 + x_2$ is equal to :",
        "options": [
            {"id": "1", "text": "15", "isCorrect": False},
            {"id": "2", "text": "18", "isCorrect": False},
            {"id": "3", "text": "24", "isCorrect": False},
            {"id": "4", "text": "13", "isCorrect": True}
        ]
    },
    "q52": {
        "questionText": "Let $f$ be a differentiable function on $\\mathbb{R}$ such that $f(2) = 1, f'(2) = 4$. Let $\\lim_{x \\to 0} (f(2+x))^{3/x} = e^\\alpha$. Then the number of times the curve $y = 4x^3 - 4x^2 - 4(\\alpha - 7)x - \\alpha$ meets the $x$-axis is :",
        "options": [
            {"id": "1", "text": "2", "isCorrect": False},
            {"id": "2", "text": "1", "isCorrect": True},
            {"id": "3", "text": "0", "isCorrect": False},
            {"id": "4", "text": "3", "isCorrect": False}
        ]
    },
    "q53": {
        "questionText": "The sum of the infinite series $\\cot^{-1}\\left(\\frac{7}{4}\\right) + \\cot^{-1}\\left(\\frac{19}{4}\\right) + \\cot^{-1}\\left(\\frac{39}{4}\\right) + \\cot^{-1}\\left(\\frac{67}{4}\\right) + \\dots$ is :",
        "options": [
            {"id": "1", "text": "$\\frac{\\pi}{2} + \\tan^{-1}\\left(\\frac{1}{2}\\right)$", "isCorrect": False},
            {"id": "2", "text": "$\\frac{\\pi}{2} - \\cot^{-1}\\left(\\frac{1}{2}\\right)$", "isCorrect": False},
            {"id": "3", "text": "$\\frac{\\pi}{2} + \\cot^{-1}\\left(\\frac{1}{2}\\right)$", "isCorrect": False},
            {"id": "4", "text": "$\\frac{\\pi}{2} - \\tan^{-1}\\left(\\frac{1}{2}\\right)$", "isCorrect": True}
        ]
    },
    "q56": {
        "questionText": "Let the values of $p$, for which the shortest distance between the lines $\\frac{x+1}{3} = \\frac{y}{4} = \\frac{z}{5}$ and $\\vec{r} = (p\\hat{i} + 2\\hat{j} + \\hat{k}) + \\lambda(2\\hat{i} + 3\\hat{j} + 4\\hat{k})$ is $\\frac{1}{\\sqrt{6}}$, be $a, b \\ (a < b)$. Then the length of the latus rectum of the ellipse $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ is :",
        "options": [
            {"id": "1", "text": "9", "isCorrect": False},
            {"id": "2", "text": "$\\frac{3}{2}$", "isCorrect": True},
            {"id": "3", "text": "2", "isCorrect": False},
            {"id": "4", "text": "6", "isCorrect": False}
        ]
    },
    "q57": {
        "questionText": "The axis of a parabola is the line $y = x$ and its vertex and focus are in the first quadrant at distances $\\sqrt{2}$ and $2\\sqrt{2}$ units from the origin, respectively. If the point $(1, k)$ lies on the parabola, then a possible value of $k$ is :",
        "options": [
            {"id": "1", "text": "4", "isCorrect": False},
            {"id": "2", "text": "9", "isCorrect": True},
            {"id": "3", "text": "3", "isCorrect": False},
            {"id": "4", "text": "8", "isCorrect": False}
        ]
    },
    "q60": {
        "questionText": "Let the sum of the focal distances of the point $P(4, 3)$ on the hyperbola $H : \\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$ be $\\frac{8\\sqrt{5}}{3}$. If for $H$, the length of the latus rectum is $l$ and the product of the focal distances of the point $P$ is $m$, then $9l^2 + 6m$ is equal to :",
        "options": [
            {"id": "1", "text": "184", "isCorrect": False},
            {"id": "2", "text": "186", "isCorrect": True},
            {"id": "3", "text": "185", "isCorrect": False},
            {"id": "4", "text": "187", "isCorrect": False}
        ]
    },
    "q61": {
        "questionText": "Let the matrix $A = \\begin{bmatrix} 1 & 0 & 0 \\\\ 1 & 0 & 1 \\\\ 0 & 1 & 0 \\end{bmatrix}$ satisfy $A^n = A^{n-2} + A^2 - I$ for $n \\ge 3$. Then the sum of all the elements of $A^{50}$ is :",
        "options": [
            {"id": "1", "text": "53", "isCorrect": False},
            {"id": "2", "text": "52", "isCorrect": True},
            {"id": "3", "text": "39", "isCorrect": False},
            {"id": "4", "text": "44", "isCorrect": False}
        ]
    },
    "q62": {
        "questionText": "If the sum of the first 20 terms of the series $\\frac{4 \\cdot 1}{4 + 3 \\cdot 1^2 + 1^4} + \\frac{4 \\cdot 2}{4 + 3 \\cdot 2^2 + 2^4} + \\frac{4 \\cdot 3}{4 + 3 \\cdot 3^2 + 3^4} + \\dots$ is $\\frac{m}{n}$, where $m$ and $n$ are coprime, then $m + n$ is equal to :",
        "options": [
            {"id": "1", "text": "423", "isCorrect": False},
            {"id": "2", "text": "420", "isCorrect": False},
            {"id": "3", "text": "421", "isCorrect": True},
            {"id": "4", "text": "422", "isCorrect": False}
        ]
    },
    "q63": {
        "questionText": "If $1^2 \\cdot \\binom{15}{1} + 2^2 \\cdot \\binom{15}{2} + 3^2 \\cdot \\binom{15}{3} + \\dots + 15^2 \\cdot \\binom{15}{15} = 2^m \\cdot 3^n \\cdot 5^k$, where $m, n, k \\in \\mathbb{N}$, then $m + n + k$ is equal to :",
        "options": [
            {"id": "1", "text": "19", "isCorrect": True},
            {"id": "2", "text": "21", "isCorrect": False},
            {"id": "3", "text": "18", "isCorrect": False},
            {"id": "4", "text": "20", "isCorrect": False}
        ]
    },
    "q66": {
        "questionText": "If a curve $y = y(x)$ passes through the point $(1, \\frac{\\pi}{2})$ and satisfies the differential equation $(7x^4\\cot y - e^x\\csc y)dx = x^5 dy, \\ x \\ge 1$, then at $x = 2$, the value of $\\cos y$ is :",
        "options": [
            {"id": "1", "text": "$\\frac{2e^2 - e}{64}$", "isCorrect": False},
            {"id": "2", "text": "$\\frac{2e^2 + e}{64}$", "isCorrect": False},
            {"id": "3", "text": "$\\frac{2e^2 - e}{128}$", "isCorrect": True},
            {"id": "4", "text": "$\\frac{2e^2 + e}{128}$", "isCorrect": False}
        ]
    },
    "q70": {
        "questionText": "Let the mean and the standard deviation of the observations $2, 3, 3, 4, 5, 7, a, b$ be $4$ and $\\sqrt{2}$ respectively. Then the mean deviation about the mode of these observations is :",
        "options": [
            {"id": "1", "text": "1", "isCorrect": False},
            {"id": "2", "text": "$\\frac{3}{4}$", "isCorrect": False},
            {"id": "3", "text": "2", "isCorrect": False},
            {"id": "4", "text": "$\\frac{1}{2}$", "isCorrect": True}
        ]
    },
    "q71": {
        "questionText": "If $\\alpha$ is a root of the equation $x^2 + x + 1 = 0$ and $\\sum_{k=1}^n \\left(\\alpha^k + \\frac{1}{\\alpha^k}\\right)^2 = 20$, then $n$ is equal to _______."
    },
    "q74": {
        "questionText": "Let $m$ and $n$, $(m < n)$ be two 2-digit numbers. Then the total number of pairs $(m, n)$, such that $\\gcd(m, n) = 6$, is _______."
    },
    "q75": {
        "questionText": "Let the three sides of a triangle $ABC$ be given by the vectors $2\\hat{i} - \\hat{j} + \\hat{k}$, $\\hat{i} - 3\\hat{j} - 5\\hat{k}$ and $3\\hat{i} - 4\\hat{j} - 4\\hat{k}$. Let $G$ be the centroid of the triangle $ABC$. Then $6(|\\vec{AG}|^2 + |\\vec{BG}|^2 + |\\vec{CG}|^2)$ is equal to _______."
    }
}

for s in paper['sections']:
    for sub in s.get('subsections', []):
        for q in sub.get('questions', []):
            qid = q['id']
            if qid in updates:
                for k, v in updates[qid].items():
                    q[k] = v

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(paper, f, indent=2, ensure_ascii=False)
    f.write('\n')

print("Successfully updated jee_mains_04_apr_2025_shift_2.json!")
