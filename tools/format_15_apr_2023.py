import json
import os

filepath = os.path.join(os.path.dirname(__file__), '..', 'jee_mains_15_apr_2023_shift_1', 'jee_mains_15_apr_2023_shift_1.json')

with open(filepath, 'r', encoding='utf-8') as f:
    paper = json.load(f)

# Map question ID to updated question data
updates = {
    "math_q1": {
        "questionText": "Let $S$ be the set of all $(\\lambda, \\mu)$ for which the vectors $\\vec{a} = \\lambda\\hat{i} - \\hat{j} + \\hat{k}$, $\\vec{b} = \\hat{i} + 2\\hat{j} + \\mu\\hat{k}$ and $\\vec{c} = 3\\hat{i} - 4\\hat{j} + 5\\hat{k}$, where $\\lambda - \\mu = 5$, are coplanar. Then $80 \\sum_{(\\lambda, \\mu) \\in S} (\\lambda^2 + \\mu^2)$ is equal to",
        "options": [
            {"id": "A", "text": "2210", "isCorrect": False},
            {"id": "B", "text": "2130", "isCorrect": False},
            {"id": "C", "text": "2290", "isCorrect": True},
            {"id": "D", "text": "2370", "isCorrect": False}
        ]
    },
    "math_q2": {
        "questionText": "Let the determinant of a square matrix $A$ of order $m$ be $m - n$, where $m$ and $n$ satisfy $4m + n = 22$ and $17m + 4n = 93$. If $\\det(n \\cdot \\operatorname{adj}(\\operatorname{adj}(mA))) = 3^a 5^b 6^c$, then $a + b + c$ is equal to",
        "options": [
            {"id": "A", "text": "84", "isCorrect": False},
            {"id": "B", "text": "96", "isCorrect": True},
            {"id": "C", "text": "101", "isCorrect": False},
            {"id": "D", "text": "109", "isCorrect": False}
        ]
    },
    "math_q3": {
        "questionText": "If $(\\alpha, \\beta)$ is the orthocenter of the triangle $ABC$ with vertices $A(3, -7)$, $B(-1, 2)$ and $C(4, 5)$, then $9\\alpha - 6\\beta + 60$ is equal to",
        "options": [
            {"id": "A", "text": "25", "isCorrect": True},
            {"id": "B", "text": "35", "isCorrect": False},
            {"id": "C", "text": "30", "isCorrect": False},
            {"id": "D", "text": "40", "isCorrect": False}
        ]
    },
    "math_q4": {
        "questionText": "Let $ABCD$ be a quadrilateral. If $E$ and $F$ are the mid points of the diagonals $AC$ and $BD$ respectively and $(\\vec{AB} - \\vec{BC}) + (\\vec{AD} - \\vec{DC}) = k\\vec{FE}$, then $k$ is equal to",
        "options": [
            {"id": "A", "text": "4", "isCorrect": False},
            {"id": "B", "text": "-2", "isCorrect": False},
            {"id": "C", "text": "2", "isCorrect": False},
            {"id": "D", "text": "-4", "isCorrect": True}
        ]
    },
    "math_q5": {
        "questionText": "Let the foot of perpendicular of the point $P(3, -2, -9)$ on the plane passing through the points $(-1, -2, -3)$, $(9, 3, 4)$, $(9, -2, 1)$ be $Q(\\alpha, \\beta, \\gamma)$. Then the distance of $Q$ from the origin is",
        "options": [
            {"id": "A", "text": "$\\sqrt{42}$", "isCorrect": True},
            {"id": "B", "text": "$\\sqrt{38}$", "isCorrect": False},
            {"id": "C", "text": "$\\sqrt{35}$", "isCorrect": False},
            {"id": "D", "text": "$\\sqrt{29}$", "isCorrect": False}
        ]
    },
    "math_q6": {
        "questionText": "The number of common tangents to the circles $x^2 + y^2 - 18x - 15y + 131 = 0$ and $x^2 + y^2 - 6x - 6y - 7 = 0$ is",
        "options": [
            {"id": "A", "text": "3", "isCorrect": False},
            {"id": "B", "text": "1", "isCorrect": False},
            {"id": "C", "text": "4", "isCorrect": True},
            {"id": "D", "text": "2", "isCorrect": False}
        ]
    },
    "math_q7": {
        "questionText": "The total number of three-digit numbers, divisible by 3, which can be formed using the digits 1, 3, 5, 8, if repetition of digits is allowed, is",
        "options": [
            {"id": "A", "text": "21", "isCorrect": False},
            {"id": "B", "text": "20", "isCorrect": False},
            {"id": "C", "text": "22", "isCorrect": True},
            {"id": "D", "text": "18", "isCorrect": False}
        ]
    },
    "math_q8": {
        "questionText": "If the set $\\{\\mathrm{Re}\\left(\\frac{z - \\bar{z} + z\\bar{z}}{2 - 3z + 5\\bar{z}}\\right) : z \\in \\mathbb{C}, \\ \\mathrm{Re}(z) = 3\\}$ is equal to the interval $(\\alpha, \\beta]$, then $24(\\beta - \\alpha)$ is equal to",
        "options": [
            {"id": "A", "text": "36", "isCorrect": False},
            {"id": "B", "text": "27", "isCorrect": False},
            {"id": "C", "text": "30", "isCorrect": True},
            {"id": "D", "text": "42", "isCorrect": False}
        ]
    },
    "math_q9": {
        "questionText": "Let $(a + bx + cx^2)^{10} = \\sum_{i=0}^{20} p_i x^i$, where $a, b, c \\in \\mathbb{N}$. If $p_1 = 20$ and $p_2 = 210$, then $2(a + b + c)$ is equal to",
        "options": [
            {"id": "A", "text": "6", "isCorrect": False},
            {"id": "B", "text": "15", "isCorrect": False},
            {"id": "C", "text": "12", "isCorrect": True},
            {"id": "D", "text": "8", "isCorrect": False}
        ]
    },
    "math_q10": {
        "questionText": "The number of real roots of the equation $x|x| - 5|x + 2| + 6 = 0$ is",
        "options": [
            {"id": "A", "text": "5", "isCorrect": False},
            {"id": "B", "text": "4", "isCorrect": False},
            {"id": "C", "text": "6", "isCorrect": False},
            {"id": "D", "text": "3", "isCorrect": True}
        ]
    },
    "math_q11": {
        "questionText": "Let $A_1$ and $A_2$ be two arithmetic means and $G_1, G_2, G_3$ be three geometric means of two distinct positive numbers. Then $G_1^4 + G_2^4 + G_3^4 + G_1^2 G_3^2$ is equal to",
        "options": [
            {"id": "A", "text": "$(A_1 + A_2)^2 G_1 G_3$", "isCorrect": True},
            {"id": "B", "text": "$2(A_1 + A_2) G_1 G_3$", "isCorrect": False},
            {"id": "C", "text": "$(A_1 + A_2)^2 G_1^2 G_3^2$", "isCorrect": False},
            {"id": "D", "text": "$2(A_1 + A_2)^2 G_1^2 G_3^2$", "isCorrect": False}
        ]
    },
    "math_q12": {
        "questionText": "Let $[x]$ denote the greatest integer function and $f(x) = \\max\\{1 + x + [x], 2 + x, x + 2[x]\\}, \\ 0 \\le x \\le 2$. Let $m$ be the number of points in $[0, 2]$ where $f$ is not continuous and $n$ be the number of points in $(0, 2)$ where $f$ is not differentiable. Then $(m + n)^2 + 2$ is equal to",
        "options": [
            {"id": "A", "text": "2", "isCorrect": False},
            {"id": "B", "text": "11", "isCorrect": False},
            {"id": "C", "text": "6", "isCorrect": False},
            {"id": "D", "text": "3", "isCorrect": True}
        ]
    },
    "math_q13": {
        "questionText": "Let $S$ be the set of all values of $\\lambda$ for which the shortest distance between the lines $\\frac{x}{1} = \\frac{y-4}{3} = \\frac{z+\\lambda}{6}$ and $\\frac{x-3}{1} = \\frac{y+\\lambda}{-4} = \\frac{z}{0}$ is $13$. Then $8\\sum_{\\lambda \\in S} |\\lambda|$ is equal to",
        "options": [
            {"id": "A", "text": "306", "isCorrect": True},
            {"id": "B", "text": "304", "isCorrect": False},
            {"id": "C", "text": "308", "isCorrect": False},
            {"id": "D", "text": "302", "isCorrect": False}
        ]
    },
    "math_q14": {
        "questionText": "Negation of $(p \\land q) \\land (\\sim p \\land q)$ is",
        "options": [
            {"id": "A", "text": "$(p \\land q) \\lor \\sim p$", "isCorrect": False},
            {"id": "B", "text": "$p \\lor q$", "isCorrect": False},
            {"id": "C", "text": "$\\sim(p \\land q) \\lor \\sim q$", "isCorrect": True},
            {"id": "D", "text": "$(p \\land q) \\land \\sim q$", "isCorrect": False}
        ]
    },
    "math_q15": {
        "questionText": "Let the system of linear equations:\n$$\\begin{aligned} -x + 2y - 9z &= 7 \\\\ -x + 3y + 7z &= 9 \\\\ -2x + y + 5z &= 8 \\\\ -3x + y + 13z &= \\lambda \\end{aligned}$$\nhave a unique solution $x = \\alpha, y = \\beta, z = \\gamma$. Then the distance of the point $(\\alpha, \\beta, \\gamma)$ from the plane $2x - 2y + z = \\lambda$ is",
        "options": [
            {"id": "A", "text": "11", "isCorrect": False},
            {"id": "B", "text": "7", "isCorrect": True},
            {"id": "C", "text": "9", "isCorrect": False},
            {"id": "D", "text": "13", "isCorrect": False}
        ]
    },
    "math_q16": {
        "questionText": "A bag contains 6 white and 4 black balls. A die is rolled once and the number of balls equal to the number obtained on the die are drawn from the bag at random. The probability that all the balls drawn are white is",
        "options": [
            {"id": "A", "text": "$\\frac{1}{4}$", "isCorrect": False},
            {"id": "B", "text": "$\\frac{11}{50}$", "isCorrect": False},
            {"id": "C", "text": "$\\frac{1}{5}$", "isCorrect": True},
            {"id": "D", "text": "$\\frac{9}{50}$", "isCorrect": False}
        ]
    },
    "math_q17": {
        "questionText": "If $\\int_0^1 \\frac{dx}{(5 + 2x - 2x^2)(1 + e^{2 - 4x})} = \\frac{1}{\\alpha}\\log_e\\left(\\frac{\\alpha + 1}{\\beta}\\right)$, where $\\alpha, \\beta > 0$, then $\\alpha^4 - \\beta^4$ is equal to",
        "options": [
            {"id": "A", "text": "19", "isCorrect": False},
            {"id": "B", "text": "-21", "isCorrect": False},
            {"id": "C", "text": "0", "isCorrect": False},
            {"id": "D", "text": "21", "isCorrect": True}
        ]
    },
    "math_q18": {
        "questionText": "If the domain of the function $f(x) = \\log_e(4x^2 + 11x + 6) + \\sin^{-1}(4x + 3) + \\cos^{-1}\\left(\\frac{10x + 6}{3}\\right)$ is $(\\alpha, \\beta]$, then $36|\\alpha + \\beta|$ is equal to",
        "options": [
            {"id": "A", "text": "54", "isCorrect": False},
            {"id": "B", "text": "72", "isCorrect": False},
            {"id": "C", "text": "63", "isCorrect": False},
            {"id": "D", "text": "45", "isCorrect": True}
        ]
    },
    "math_q19": {
        "questionText": "Let $x = x(y)$ be the solution of the differential equation $2(y + 2)\\log_e(y + 2)\\,dx + (x + 4 - 2\\log_e(y + 2))\\,dy = 0, \\ y > -1$ with $x(e^4 - 2) = 1$. Then $x(e^9 - 2)$ is equal to",
        "options": [
            {"id": "A", "text": "3", "isCorrect": False},
            {"id": "B", "text": "4", "isCorrect": False},
            {"id": "C", "text": "$\\frac{32}{9}$", "isCorrect": True},
            {"id": "D", "text": "$\\frac{10}{3}$", "isCorrect": False}
        ]
    },
    "math_q20": {
        "questionText": "The mean and standard deviation of 10 observations are 20 and 8 respectively. Later on, it was observed that one observation was recorded as 50 instead of 40. Then the correct variance is",
        "options": [
            {"id": "A", "text": "11", "isCorrect": False},
            {"id": "B", "text": "13", "isCorrect": False},
            {"id": "C", "text": "12", "isCorrect": False},
            {"id": "D", "text": "14", "isCorrect": True}
        ]
    },
    "math_q21": {
        "questionText": "Let $f(x) = \\int \\frac{dx}{(3+4x)^{\\frac{3}{2}}(4-3x)^{\\frac{1}{2}}}$ for $x < \\frac{4}{3}$. If $f(0) = 0$ and $f(1) = \\tan^{-1}\\left(\\frac{\\alpha}{\\beta}\\right)$, where $\\alpha, \\beta > 0$, then $\\alpha^2 + \\beta^2$ is equal to _______."
    },
    "math_q22": {
        "questionText": "Let an ellipse with center $(1, 0)$ and latus rectum of length $\\frac{1}{2}$ have its major axis along the $x$-axis. If its minor axis subtends an angle $60^\\circ$ at the foci, then the square of the sum of the lengths of its minor and major axes is equal to _______."
    },
    "math_q23": {
        "questionText": "A person forgets his 4-digit ATM pin code. But he remembers that in the code all the digits are different, the greatest digit is 7 and the sum of the first two digits is equal to the sum of the last two digits. Then the maximum number of trials necessary to obtain the correct code is _______."
    },
    "math_q24": {
        "questionText": "The number of elements in the set $\\{n \\in \\mathbb{N} : 10 \\le n \\le 100 \\text{ and } 3^n - 3 \\text{ is a multiple of } 7\\}$ is _______."
    },
    "math_q25": {
        "questionText": "Let $A = \\{1, 2, 3, 4\\}$ and $R$ be a relation on the set $A \\times A$ defined by $R = \\{((a, b), (c, d)) : 2a + 3b = 4c + 5d\\}$. Then the number of elements in $R$ is _______."
    },
    "math_q26": {
        "questionText": "Consider the triangles with vertices $A(2, 1)$, $B(0, 0)$ and $C(t, 4)$, $t \\in [0, 4]$. If the maximum and the minimum perimeters of such triangles are obtained at $t = \\alpha$ and $t = \\beta$ respectively, then $6\\alpha + 21\\beta$ is equal to _______."
    },
    "math_q27": {
        "questionText": "If the area bounded by the curve $2y^2 = 3x$, lines $x + y = 3$, $y = 0$ and outside the circle $(x - 3)^2 + y^2 = 2$ is $A$, then $4(\\pi + 4A)$ is equal to _______."
    },
    "math_q28": {
        "questionText": "If the line $x = y = z$ intersects the line $x\\sin A + y\\sin B + z\\sin C - 18 = 0 = x\\sin 2A + y\\sin 2B + z\\sin 2C - 9$, where $A, B, C$ are the angles of a triangle $ABC$, then $80\\left(\\sin\\frac{A}{2}\\sin\\frac{B}{2}\\sin\\frac{C}{2}\\right)$ is equal to _______."
    },
    "math_q29": {
        "questionText": "If the sum of the series $\\left(\\frac{1}{2} - \\frac{1}{3}\\right) + \\left(\\frac{1}{2^2} - \\frac{1}{2 \\cdot 3} + \\frac{1}{3^2}\\right) + \\left(\\frac{1}{2^3} - \\frac{1}{2^2 \\cdot 3} + \\frac{1}{2 \\cdot 3^2} - \\frac{1}{3^3}\\right) + \\dots$ is equal to $\\frac{\\alpha}{\\beta}$, where $\\alpha$ and $\\beta$ are co-prime, then $\\alpha + 3\\beta$ is equal to _______."
    },
    "math_q30": {
        "questionText": "Let the plane $P$ contain the line $2x + y - z - 3 = 0 = 5x - 3y + 4z + 9$ and be parallel to the line $\\frac{x+2}{2} = \\frac{3-y}{-4} = \\frac{z-7}{5}$. Then the distance of the point $A(8, -1, -19)$ from the plane $P$ measured parallel to the line $\\frac{x}{-3} = \\frac{y-5}{4} = \\frac{2-z}{-12}$ is equal to _______."
    },
    "phys_q1": {
        "questionText": "A flask contains Hydrogen and Argon in the ratio $2 : 1$ by mass. The temperature of the mixture is $30^\\circ\\text{C}$. The ratio of average kinetic energy per molecule of the two gases $(K_{\\text{argon}} / K_{\\text{hydrogen}})$ is: (Given : Atomic Weight of $\\text{Ar} = 39.9$)",
        "options": [
            {"id": "A", "text": "2", "isCorrect": False},
            {"id": "B", "text": "1", "isCorrect": True},
            {"id": "C", "text": "39.9", "isCorrect": False},
            {"id": "D", "text": "$\\frac{39.9}{2}$", "isCorrect": False}
        ]
    },
    "phys_q2": {
        "questionText": "A $12\\text{ V}$ battery connected to a coil of resistance $6\\ \\Omega$ through a switch, drives a constant current in the circuit. The switch is opened in $1\\text{ ms}$. The emf induced across the coil is $20\\text{ V}$. The inductance of the coil is :",
        "options": [
            {"id": "A", "text": "$10\\text{ mH}$", "isCorrect": True},
            {"id": "B", "text": "$8\\text{ mH}$", "isCorrect": False},
            {"id": "C", "text": "$5\\text{ mH}$", "isCorrect": False},
            {"id": "D", "text": "$12\\text{ mH}$", "isCorrect": False}
        ]
    },
    "phys_q26": {
        "questionText": "In the given figure the total charge stored in the combination of capacitors is $100\\ \\mu\\text{C}$. The value of '$x$' is _______."
    },
    "phys_q27": {
        "questionText": "A $20\\text{ cm}$ long metallic rod is rotated with $210\\text{ rpm}$ about an axis normal to the rod passing through its one end. The other end of the rod is in contact with a circular metallic ring. A constant and uniform magnetic field of $0.5\\text{ T}$ parallel to the axis exists everywhere. The emf developed between the centre and the ring is _______ $\\text{mV}$. (Take $\\pi = \\frac{22}{7}$)"
    },
    "chem_q14": {
        "questionText": "Which one of the following is not an example of calcination?",
        "options": [
            {"id": "A", "text": "$\\text{CaCO}_3 \\xrightarrow{\\Delta} \\text{CaO} + \\text{CO}_2$", "isCorrect": False},
            {"id": "B", "text": "$\\text{Fe}_2\\text{O}_3 \\cdot x\\text{H}_2\\text{O} \\xrightarrow{\\Delta} \\text{Fe}_2\\text{O}_3 + x\\text{H}_2\\text{O}$", "isCorrect": False},
            {"id": "C", "text": "$2\\text{PbS} + 3\\text{O}_2 \\xrightarrow{\\Delta} 2\\text{PbO} + 2\\text{SO}_2$", "isCorrect": True},
            {"id": "D", "text": "$\\text{CaCO}_3 \\cdot \\text{MgCO}_3 \\xrightarrow{\\Delta} \\text{CaO} + \\text{MgO} + 2\\text{CO}_2$", "isCorrect": False}
        ]
    },
    "chem_q17": {
        "questionText": "Which of the following expressions is correct in case of a $\\text{CsCl}$ unit cell (edge length '$a$')?",
        "options": [
            {"id": "A", "text": "$r_{\\text{Cs}^+} + r_{\\text{Cl}^-} = \\frac{a}{2}$", "isCorrect": False},
            {"id": "B", "text": "$r_{\\text{Cs}^+} + r_{\\text{Cl}^-} = \\frac{\\sqrt{3}a}{2}$", "isCorrect": True},
            {"id": "C", "text": "$r_{\\text{Cs}^+} + r_{\\text{Cl}^-} = \\frac{3a}{2}$", "isCorrect": False},
            {"id": "D", "text": "$r_{\\text{Cs}^+} + r_{\\text{Cl}^-} = a$", "isCorrect": False}
        ]
    },
    "phys_q12": {
        "questionText": "A single slit of width $a$ is illuminated by a monochromatic light of wavelength $600\\text{ nm}$. The value of '$a$' for which first minimum appears at $\\theta = 30^\\circ$ on the screen will be :",
        "explanation": "$d\\sin\\theta = \\lambda \\implies d = \\frac{\\lambda}{\\sin 30^\\circ} = 2\\lambda = 1.2\\,\\mu\\text{m}$"
    },
    "phys_q13": {
        "questionText": "A vector in $x-y$ plane makes an angle of $30^\\circ$ with $y$-axis. The magnitude of $y$-component of vector is $2\\sqrt{3}$. The magnitude of $x$-component of the vector will be :",
        "explanation": "$a_y = 2\\sqrt{3}$. Therefore $a_x = a_y\\tan 30^\\circ = 2\\sqrt{3} \\times \\frac{1}{\\sqrt{3}} = 2$."
    },
    "phys_q29": {
        "questionText": "The refractive index of a transparent liquid filled in an equilateral hollow prism is $\\sqrt{2}$. The angle of minimum deviation for the liquid will be _______$^{\\circ}$.",
        "explanation": "For an equilateral prism, $A = 60^\\circ$. $\\mu = \\frac{\\sin((A + \\delta_m)/2)}{\\sin(A/2)} \\implies \\sqrt{2} = \\frac{\\sin((60^\\circ + \\delta_m)/2)}{\\sin 30^\\circ} = 2\\sin((60^\\circ + \\delta_m)/2) \\implies \\sin((60^\\circ + \\delta_m)/2) = \\frac{\\sqrt{2}}{2} = \\frac{1}{\\sqrt{2}} \\implies \\frac{60^\\circ + \\delta_m}{2} = 45^\\circ \\implies \\delta_m = 30^\\circ$."
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

print("Successfully updated jee_mains_15_apr_2023_shift_1.json!")
