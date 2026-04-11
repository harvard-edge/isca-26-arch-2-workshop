import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the section blocks using Regex. Each block starts with an HTML comment and ends before the next block.
# We will split by `<!-- ` to find sections.
sections_raw = html.split('<!-- ')

sections = {}
other_parts = []
current_index = 0

for i, part in enumerate(sections_raw):
    if part.startswith('Schedule Section -->'):
        sections['schedule'] = '<!-- ' + part
    elif part.startswith('Competition Section -->'):
        sections['competition'] = '<!-- ' + part
    elif part.startswith('Call for Papers Section -->'):
        sections['cfp'] = '<!-- ' + part
    elif part.startswith('Call for Tutorials Section -->'):
        sections['cft'] = '<!-- ' + part
    else:
        # Just store the order
        pass

# Wait, a better way is to do it properly:
sections_regex = r"(<!-- Schedule Section -->.*?)(?=<!-- Competition Section -->|<!-- Call for Papers Section -->|<!-- Call for Tutorials Section -->|<!-- Resources Section -->)"
schedule_match = re.search(r"(<!-- Schedule Section -->.*?</section>\n)", html, re.DOTALL)
competition_match = re.search(r"(<!-- Competition Section -->.*?</section>\n)", html, re.DOTALL)
cfp_match = re.search(r"(<!-- Call for Papers Section -->.*?</section>\n)", html, re.DOTALL)
cft_match = re.search(r"(<!-- Call for Tutorials Section -->.*?</section>\n)", html, re.DOTALL)

schedule = schedule_match.group(1)
competition = competition_match.group(1)
cfp = cfp_match.group(1)
cft = cft_match.group(1)

# fix the background color alternation
# About is section
# 1. CFP -> section-alt
# 2. CFT -> section
# 3. Competition -> section-alt
# 4. Schedule -> section

def set_class(text, class_val):
    return re.sub(r'<section id="[^"]+" class="[^"]+">', lambda m: re.sub(r'class="[^"]+"', f'class="{class_val}"', m.group(0)), text, count=1)

cfp = set_class(cfp, "section section-alt")
cft = set_class(cft, "section")
competition = set_class(competition, "section section-alt")
schedule = set_class(schedule, "section")

# Now reassemble
# The portion before schedule
start_idx = min(schedule_match.start(), competition_match.start(), cfp_match.start(), cft_match.start())
end_idx = max(schedule_match.end(), competition_match.end(), cfp_match.end(), cft_match.end())

new_html = html[:start_idx] + cfp + "\n" + cft + "\n" + competition + "\n" + schedule + "\n    " + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Reordered successfully!")
