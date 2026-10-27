import json
import os

filepath = os.path.join(os.path.dirname(__file__), '..', 'jee_mains_03_apr_2025_shift_2', 'jee_mains_03_apr_2025_shift_2.json')

with open(filepath, 'r', encoding='utf-8') as f:
    paper = json.load(f)

updates = {
    "q1": {
        "questionText": "A magnetic dipole experiences a torque of $80\\sqrt{3}\\text{ N}\\cdot\\text{m}$ when placed in uniform magnetic field in such a way that dipole moment makes angle of $60^\\circ$ with magnetic field. The potential energy of the dipole is :",
        "options": [
            {"id": "A", "text": "$80\\text{ J}$", "isCorrect": False},
            {"id": "B", "text": "$-40\\sqrt{3}\\text{ J}$", "isCorrect": False},
            {"id": "C", "text": "$-60\\text{ J}$", "isCorrect": False},
            {"id": "D", "text": "$-80\\text{ J}$", "isCorrect": True}
        ]
    },
    "q3": {
        "questionText": "Two cylindrical vessels of equal cross sectional area of $2\\text{ m}^2$ contain water upto height $10\\text{ m}$ and $6\\text{ m}$ respectively. The vessels are interconnected by a pipe at the bottom. Work done by the gravity in establishing the new equilibrium level is : (Take $g = 10\\text{ m/s}^2$ and density of water $= 10^3\\text{ kg/m}^3$)",
        "options": [
            {"id": "A", "text": "$1 \\times 10^5\\text{ J}$", "isCorrect": False},
            {"id": "B", "text": "$4 \\times 10^4\\text{ J}$", "isCorrect": True},
            {"id": "C", "text": "$6 \\times 10^4\\text{ J}$", "isCorrect": False},
            {"id": "D", "text": "$8 \\times 10^4\\text{ J}$", "isCorrect": False}
        ]
    },
    "q4": {
        "questionText": "Width of one of the two slits in a Young's double slit interference experiment is half of the other slit. The ratio of maximum to minimum intensity in the interference pattern is :",
        "options": [
            {"id": "A", "text": "$(2\\sqrt{2} + 1) : (2\\sqrt{2} - 1)$", "isCorrect": False},
            {"id": "B", "text": "$(3 + 2\\sqrt{2}) : (3 - 2\\sqrt{2})$", "isCorrect": True},
            {"id": "C", "text": "$9 : 1$", "isCorrect": False},
            {"id": "D", "text": "$3 : 1$", "isCorrect": False}
        ]
    },
    "q9": {
        "questionText": "A monochromatic light of frequency $5 \\times 10^{14}\\text{ Hz}$ travelling through air, is incident on a medium of refractive index $1.5$. The wavelength of the light in the medium is : (Take $c = 3 \\times 10^8\\text{ m/s}$)",
        "options": [
            {"id": "A", "text": "$300\\text{ nm}$", "isCorrect": False},
            {"id": "B", "text": "$600\\text{ nm}$", "isCorrect": False},
            {"id": "C", "text": "$400\\text{ nm}$", "isCorrect": True},
            {"id": "D", "text": "$500\\text{ nm}$", "isCorrect": False}
        ]
    },
    "q17": {
        "questionText": "Pressure of an ideal gas, contained in a closed vessel, is increased by $0.4\\%$ when heated by $1^\\circ\\text{C}$. Its initial temperature must be :",
        "options": [
            {"id": "A", "text": "$25^\\circ\\text{C}$", "isCorrect": False},
            {"id": "B", "text": "$2500\\text{ K}$", "isCorrect": False},
            {"id": "C", "text": "$250\\text{ K}$", "isCorrect": True},
            {"id": "D", "text": "$250^\\circ\\text{C}$", "isCorrect": False}
        ]
    },
    "q21": {
        "questionText": "Light from a point source in air falls on a spherical glass surface (refractive index, $\\mu = 1.5$ and radius of curvature $= 50\\text{ cm}$). The image is formed at a distance of $200\\text{ cm}$ from the glass surface inside the glass. The magnitude of distance of the light source from the glass surface is _______ $\\text{m}$."
    },
    "q23": {
        "questionText": "Two cells of emf $1\\text{ V}$ and $2\\text{ V}$ and internal resistance $2\\ \\Omega$ and $1\\ \\Omega$, respectively, are connected in series with an external resistance $R$. If the current in the circuit is $0.5\\text{ A}$, then $R$ is equal to _______ $\\Omega$."
    },
    "q25": {
        "questionText": "A physical quantity $C$ is related to four other quantities $p, q, r$ and $s$ as follows: $C = \\frac{p q^2}{r^3 \\sqrt{s}}$. The percentage errors of measurement in $p, q, r$ and $s$ are $1\\%, 2\\%, 1\\%$ and $4\\%$ respectively. The maximum percentage error in $C$ is _______ $\\%$."
    },
    "q30": {
        "questionText": "For electron in '$2s$' and '$2p$' orbitals, the orbital angular momentum values, respectively are :",
        "options": [
            {"id": "A", "text": "$\\sqrt{2}\\frac{h}{2\\pi}$ and $0$", "isCorrect": False},
            {"id": "B", "text": "$\\frac{h}{2\\pi}$ and $\\sqrt{2}\\frac{h}{2\\pi}$", "isCorrect": False},
            {"id": "C", "text": "$0$ and $\\sqrt{6}\\frac{h}{2\\pi}$", "isCorrect": False},
            {"id": "D", "text": "$0$ and $\\sqrt{2}\\frac{h}{2\\pi}$", "isCorrect": True}
        ]
    },
    "q51": {
        "questionText": "Let $f : \\mathbb{R} \\to \\mathbb{R}$ be a function defined by $f(x) = ||x + 2| - 2|x||$. If $m$ is the number of points of local minima and $n$ is the number of points of local maxima of $f$, then $m + n$ is",
        "options": [
            {"id": "A", "text": "5", "isCorrect": False},
            {"id": "B", "text": "3", "isCorrect": True},
            {"id": "C", "text": "2", "isCorrect": False},
            {"id": "D", "text": "4", "isCorrect": False}
        ]
    },
    "q52": {
        "questionText": "Each of the angles $\\beta$ and $\\gamma$ that a given line makes with the positive $y$- and $z$-axes, respectively, is half of the angle that this line makes with the positive $x$-axis. Then the sum of all possible values of the angle $\\beta$ is",
        "options": [
            {"id": "A", "text": "$\\frac{3\\pi}{4}$", "isCorrect": True},
            {"id": "B", "text": "$\\frac{\\pi}{4}$", "isCorrect": False},
            {"id": "C", "text": "$\\pi$", "isCorrect": False},
            {"id": "D", "text": "$\\frac{3\\pi}{2}$", "isCorrect": False}
        ]
    },
    "q53": {
        "questionText": "If the four distinct points $(4, 6)$, $(-1, 5)$, $(0, 0)$ and $(k, 3k)$ lie on a circle of radius $r$, then $10k + r^2$ is equal to",
        "options": [
            {"id": "A", "text": "32", "isCorrect": False},
            {"id": "B", "text": "33", "isCorrect": False},
            {"id": "C", "text": "34", "isCorrect": True},
            {"id": "D", "text": "35", "isCorrect": False}
        ]
    },
    "q54": {
        "questionText": "Let the Mean and Variance of five observations $x_1 = 1, x_2 = 3, x_3 = a, x_4 = 7$ and $x_5 = b$, where $a > b$, be $5$ and $10$ respectively. Then the Variance of the observations $n + x_n$, $n = 1, 2, \\dots, 5$ is",
        "options": [
            {"id": "A", "text": "17", "isCorrect": False},
            {"id": "B", "text": "16.4", "isCorrect": True},
            {"id": "C", "text": "17.4", "isCorrect": False},
            {"id": "D", "text": "16", "isCorrect": False}
        ]
    },
    "q55": {
        "questionText": "Consider the lines $x(3\\lambda + 1) + y(7\\lambda + 2) = 17\\lambda + 5$, $\\lambda$ being a parameter, all passing through a point $P$. One of these lines (say $L$) is farthest from the origin. If the distance of $L$ from the point $(3, 6)$ is $d$, then the value of $d^2$ is",
        "options": [
            {"id": "A", "text": "20", "isCorrect": False},
            {"id": "B", "text": "30", "isCorrect": False},
            {"id": "C", "text": "10", "isCorrect": True},
            {"id": "D", "text": "15", "isCorrect": False}
        ]
    },
    "q57": {
        "questionText": "Let the equation $x(x + 2)(12 - k) = 2$ have equal roots. Then the distance of the point $(k, k^2)$ from the line $3x + 4y + 5 = 0$ is",
        "options": [
            {"id": "A", "text": "15", "isCorrect": False},
            {"id": "B", "text": "$5\\sqrt{3}$", "isCorrect": False},
            {"id": "C", "text": "$15\\sqrt{5}$", "isCorrect": False},
            {"id": "D", "text": "12", "isCorrect": True}
        ]
    },
    "q58": {
        "questionText": "Line $L_1$ of slope $2$ and line $L_2$ of slope $\\frac{1}{2}$ intersect at the origin $O$. In the first quadrant, $P_1, P_2, \\dots, P_{12}$ are 12 points on line $L_1$ and $Q_1, Q_2, \\dots, Q_9$ are 9 points on line $L_2$. Then the total number of triangles that can be formed having vertices at three of the 22 points $O, P_1, \\dots, P_{12}, Q_1, \\dots, Q_9$ is:",
        "options": [
            {"id": "A", "text": "1080", "isCorrect": False},
            {"id": "B", "text": "1134", "isCorrect": False},
            {"id": "C", "text": "1026", "isCorrect": True},
            {"id": "D", "text": "1188", "isCorrect": False}
        ]
    },
    "q59": {
        "questionText": "The integral $\\int_0^\\pi \\frac{8x\\,dx}{4\\cos^2 x + \\sin^2 x}$ is equal to",
        "options": [
            {"id": "A", "text": "$2\\pi^2$", "isCorrect": True},
            {"id": "B", "text": "$4\\pi^2$", "isCorrect": False},
            {"id": "C", "text": "$\\pi^2$", "isCorrect": False},
            {"id": "D", "text": "$\\frac{3\\pi^2}{2}$", "isCorrect": False}
        ]
    },
    "q60": {
        "questionText": "Let $f$ be a function such that $f(x) + 3f\\left(\\frac{24}{x}\\right) = 4x, \\ x \\neq 0$. Then $f(3) + f(8)$ is equal to",
        "options": [
            {"id": "A", "text": "11", "isCorrect": True},
            {"id": "B", "text": "10", "isCorrect": False},
            {"id": "C", "text": "12", "isCorrect": False},
            {"id": "D", "text": "13", "isCorrect": False}
        ]
    },
    "q61": {
        "questionText": "The area of the region $\\{(x, y) : |x - y| \\le y \\le \\sqrt{4 - x^2}\\}$ is",
        "options": [
            {"id": "A", "text": "$\\frac{512}{3}$", "isCorrect": False},
            {"id": "B", "text": "$\\frac{1024}{3}$", "isCorrect": False},
            {"id": "C", "text": "$2\\pi - 2$", "isCorrect": True},
            {"id": "D", "text": "$\\frac{2048}{3}$", "isCorrect": False}
        ]
    },
    "q62": {
        "questionText": "If the domain of the function $f(x) = \\log_7(1 - \\log_4(x^2 - 9x + 18))$ is $(\\alpha, \\beta) \\cup (\\gamma, \\delta)$, then $\\alpha + \\beta + \\gamma + \\delta$ is equal to",
        "options": [
            {"id": "A", "text": "18", "isCorrect": True},
            {"id": "B", "text": "16", "isCorrect": False},
            {"id": "C", "text": "15", "isCorrect": False},
            {"id": "D", "text": "17", "isCorrect": False}
        ]
    },
    "q66": {
        "questionText": "The number of solutions of the equation $\\frac{4 - \\sqrt{3}\\sin x}{1 + \\sqrt{3}\\cos 2x} = -4, \\ x \\in [-2\\pi, 5\\pi]$ is",
        "options": [
            {"id": "A", "text": "4", "isCorrect": False},
            {"id": "B", "text": "3", "isCorrect": False},
            {"id": "C", "text": "6", "isCorrect": False},
            {"id": "D", "text": "5", "isCorrect": True}
        ]
    },
    "q67": {
        "questionText": "Let $C$ be the circle of minimum area enclosing the ellipse $E : \\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ with eccentricity $e = \\frac{1}{2}$ and foci $(\\pm 2, 0)$. Let $PQR$ be a variable triangle, whose vertex $P$ lies on the circle $C$ and the side $QR$ of length $2a$ is parallel to the major axis of $E$ and contains the point of intersection of $E$ with the negative $y$-axis. Then the maximum area of the triangle $PQR$ is :",
        "options": [
            {"id": "A", "text": "$6(3 + \\sqrt{2})$", "isCorrect": False},
            {"id": "B", "text": "$8(3 + \\sqrt{2})$", "isCorrect": False},
            {"id": "C", "text": "$6(2 + \\sqrt{3})$", "isCorrect": False},
            {"id": "D", "text": "$8(2 + \\sqrt{3})$", "isCorrect": True}
        ]
    },
    "q68": {
        "questionText": "The shortest distance between the curves $y^2 = 8x$ and $x^2 + y^2 + 12y + 35 = 0$ is :",
        "options": [
            {"id": "A", "text": "$2\\sqrt{3} - 1$", "isCorrect": False},
            {"id": "B", "text": "$\\sqrt{2}$", "isCorrect": False},
            {"id": "C", "text": "$3\\sqrt{2} - 1$", "isCorrect": False},
            {"id": "D", "text": "$2\\sqrt{2} - 1$", "isCorrect": True}
        ]
    },
    "q69": {
        "questionText": "The distance of the point $(7, 10, 11)$ from the line $\\frac{x-4}{1} = \\frac{y-4}{0} = \\frac{z-2}{3}$ along the line $\\frac{x-9}{2} = \\frac{y-13}{3} = \\frac{z-17}{6}$ is",
        "options": [
            {"id": "A", "text": "18", "isCorrect": False},
            {"id": "B", "text": "14", "isCorrect": True},
            {"id": "C", "text": "12", "isCorrect": False},
            {"id": "D", "text": "16", "isCorrect": False}
        ]
    },
    "q70": {
        "questionText": "The sum $1 + \\frac{1+3}{2!} + \\frac{1+3+5}{3!} + \\frac{1+3+5+7}{4!} + \\dots$ up to $\\infty$ terms is equal to",
        "options": [
            {"id": "A", "text": "$6e$", "isCorrect": False},
            {"id": "B", "text": "$4e$", "isCorrect": False},
            {"id": "C", "text": "$3e$", "isCorrect": True},
            {"id": "D", "text": "$2e$", "isCorrect": False}
        ]
    },
    "q71": {
        "questionText": "Let $I$ be the identity matrix of order $3 \\times 3$ and for the matrix $A = \\begin{bmatrix} \\lambda & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & -1 & 2 \\end{bmatrix}$, $|A| = -1$. Let $B$ be the inverse of the matrix $\\operatorname{adj}(A \\operatorname{adj}(A^2))$. Then $|(\\lambda B + I)|$ is equal to _______."
    },
    "q72": {
        "questionText": "Let $(1 + x + x^2)^{10} = a_0 + a_1 x + a_2 x^2 + \\dots + a_{20} x^{20}$. If $(a_1 + a_3 + a_5 + \\dots + a_{19}) - 11a_2 = 121k$, then $k$ is equal to _______."
    },
    "q73": {
        "questionText": "If $\\lim_{x \\to 0} \\left(\\frac{\\tan x}{x}\\right)^{\\frac{1}{x^2}} = p$, then $96 \\log_e p$ is equal to _______."
    },
    "q74": {
        "questionText": "Let $\\vec{a} = \\hat{i} + 2\\hat{j} + \\hat{k}$, $\\vec{b} = 3\\hat{i} - 3\\hat{j} + 3\\hat{k}$, $\\vec{c} = 2\\hat{i} - \\hat{j} + 2\\hat{k}$ and $\\vec{d}$ be a vector such that $\\vec{b} \\times \\vec{d} = \\vec{c} \\times \\vec{d}$ and $\\vec{a} \\cdot \\vec{d} = 4$. Then $|\\vec{a} \\times \\vec{d}|^2$ is equal to _______."
    },
    "q75": {
        "questionText": "If the equation of the hyperbola with foci $(4, 2)$ and $(8, 2)$ is $3x^2 - y^2 - \\alpha x + \\beta y + \\gamma = 0$, then $\\alpha + \\beta + \\gamma$ is equal to _______."
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

print("Successfully updated jee_mains_03_apr_2025_shift_2.json!")
