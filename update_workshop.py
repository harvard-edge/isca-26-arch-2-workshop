import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    (r'<title>Architecture 2.0 Workshop \| ISCA 2026</title>', r'<title>Architecture 2.0 Workshop & Tutorial | ISCA 2026</title>'),
    (r'<p class="hero-subtitle">Workshop on Agentic AI for Computing Systems Design</p>', r'<p class="hero-subtitle">Workshop & Tutorial on Agentic AI for Computing Systems Design</p>'),
    (r'<h2 class="section-title">About the Workshop</h2>', r'<h2 class="section-title">About the Workshop & Tutorial</h2>'),
    (r'The <strong>Architecture 2\.0</strong> workshop brings together', r'The <strong>Architecture 2.0</strong> workshop and tutorial brings together'),
    (r'this workshop provides a', r'this combined event provides a'),
    (r'The workshop focuses on', r'The workshop and tutorial focuses on'),
    
    # Complex block replacement for About section overview
    (r'The workshop consists of two separate components: a <a href="#competition">Competition</a> for\s*students to create architecture and systems questions for evaluating and developing AI systems agents and\s*a <a href="#cfp">Call for Papers</a> for research submissions\.\s*Both are part of the same workshop event\.', 
     r'The event consists of three main components: a <a href="#cfp">Call for Papers</a> for research submissions, a <a href="#cft">Call for Tutorials</a> for hands-on demonstrations, and a <a href="#competition">Competition</a> to evaluate AI reasoning capabilities. All are part of the same full-day program.'),

    (r'The workshop aims to bring together', r'The workshop and tutorial aims to bring together'),
    (r'Note: The workshop will not have formal proceedings', r'Note: The event will not have formal proceedings'),
    (r'We welcome works of three different formats to the workshop:', r'We welcome works of three different formats:'),
    (r'evaluated for relevance to the workshop', r'evaluated for relevance to the event\'s themes'),
    
    # Fix 'at the workshop'
    (r'practitioners at the workshop\.', r'practitioners at the event.'),
    (r'physical awards at the workshop\.', r'physical awards at the event.'),
    (r'\(at the workshop\)', r'(at the event)'),
    (r'part of the workshop\.', r'part of the program.'),

    (r'<h2 class="section-title">Workshop Schedule</h2>', r'<h2 class="section-title">Workshop & Tutorial Schedule</h2>'),
    (r'Workshop Schedule to be announced soon!', r'Schedule to be announced soon!'),
    (r'Architecture 2\.0 Workshop @ ISCA 2026</p>', r'Architecture 2.0 Workshop & Tutorial @ ISCA 2026</p>')
]

for old, new in replacements:
    new_html = re.sub(old, new, html, count=1)
    if new_html == html:
        print(f"Warning: pattern not found: {old}")
    html = new_html

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Text replaced!")
