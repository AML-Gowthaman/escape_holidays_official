import sys

css_path = r"s:\escape holidays\original_site\css\style.css"

try:
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    # 1. Update CSS Variables (Hex colors)
    css = css.replace("--orange: #E63E00;", "--orange: #FFC107;") # Deeper yellow/amber for gradient depth
    css = css.replace("--yellow: #FFEA00;", "--white: #FFFFFF;")       # The exact Escape Holidays logo yellow

    # 2. Update RGBA values (Shadows, backgrounds, borders, overlays)
    # Old --orange rgb: 230, 62, 0 -> New: 255, 193, 7
    css = css.replace("230, 62, 0", "255, 234, 0")

    # Old --sun rgb: 247, 147, 26 -> New: 255, 215, 0
    css = css.replace("247, 147, 26", "255, 255, 255")

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    
    print("Theme updated successfully to Logo Theme (Yellow/Gold).")

except Exception as e:
    print(f"Error: {e}")
