import re
from collections import defaultdict

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

categories = {
    'salads': 'Salads & Raitas',
    'farsan': 'Farsan & Starters',
    'soups': 'Soups',
    'chaat': 'Chaat & Street Food',
    'south_indian': 'South Indian',
    'gujarati': 'Gujarati Sabji',
    'punjabi': 'Punjabi Sabji',
    'rice_dal': 'Rice, Dal & Breads',
    'chinese': 'Chinese & Sizzlers',
    'italian_pizza': 'Pizza & Italian',
    'beverages': 'Beverages'
}

items_by_cat = defaultdict(list)
matches = re.finditer(r'<div class="menu-card" data-category="([^"]+)">.*?<h3>([^<]+)</h3>', content, re.DOTALL)
for m in matches:
    cat = m.group(1)
    item = m.group(2).strip()
    items_by_cat[cat].append(item)

html = ''
for cat_key, cat_name in categories.items():
    html += f'        <div class="menu-category">\n'
    html += f'            <h4>{cat_name}</h4>\n'
    html += f'            <div class="checkbox-grid">\n'
    for item in items_by_cat[cat_key]:
        id_str = item.lower().replace(' ', '_').replace(',', '')
        html += f'                <label class="checkbox-label">\n'
        html += f'                    <input type="checkbox" name="menu_items" value="{item}">\n'
        html += f'                    <span>{item}</span>\n'
        html += f'                </label>\n'
    html += f'            </div>\n'
    html += f'        </div>\n'

with open('scratch_menu_html.txt', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done')
