import sys

css_path = r"s:\escape holidays\original_site\css\style.css"

try:
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    # 1. Add our button variables and change theme variables to Yellow
    if "--btn-orange" not in css:
        css = css.replace("--orange: #E63E00;", "--btn-orange: #E63E00;\n  --btn-sun: #F7931A;\n  --orange: #FFC107;")
        css = css.replace("--sun: #F7931A;", "--sun: #FFD700;")
    else:
        # If it was already added but we need to reset theme to yellow
        css = css.replace("--orange: #E63E00;", "--orange: #FFC107;")
        css = css.replace("--sun: #F7931A;", "--sun: #FFD700;")

    # 2. Change buttons to use the original orange variables
    buttons = [
        ".nav-cta",
        ".btn-primary",
        ".form-submit",
        ".pkg-btn",
        ".call-float",
        ".m-cta"
    ]
    
    # Simple replacement just for the background/color of buttons
    # Since we globally change --orange to yellow, we only need to substitute back the button variables
    import re
    for btn in buttons:
        # Find the block for the button and its hover state
        for suffix in ["", ":hover", "::before", "::after"]:
            target = btn + suffix
            pattern = re.compile(rf"({target}[^\{{]*\{{)(.*?)(\}})", re.DOTALL)
            def repl(m):
                inner = m.group(2)
                inner = inner.replace("var(--orange)", "var(--btn-orange)")
                inner = inner.replace("var(--sun)", "var(--btn-sun)")
                inner = inner.replace("230, 62, 0", "230, 62, 0") # Keep orange rgba
                return m.group(1) + inner + m.group(3)
            css = pattern.sub(repl, css)

    # 3. Change all remaining hardcoded rgba orange to yellow
    # Original orange: 230, 62, 0 -> New: 255, 193, 7
    # Original sun: 247, 147, 26 -> New: 255, 215, 0
    # Wait! If we replace all, it might replace button shadows!
    # Let's manually replace the non-button instances we know about:
    
    # Hero badge
    css = css.replace("rgba(230, 62, 0, 0.1)", "rgba(255, 215, 0, 0.1)")
    css = css.replace("rgba(230, 62, 0, 0.3)", "rgba(255, 215, 0, 0.3)")
    
    # Section tags & points
    css = css.replace("rgba(230, 62, 0, 0.08)", "rgba(255, 215, 0, 0.08)")
    
    # Service icons
    css = css.replace("rgba(230, 62, 0, 0.15)", "rgba(255, 215, 0, 0.15)")
    css = css.replace("rgba(247, 147, 26, 0.15)", "rgba(255, 215, 0, 0.15)")
    css = css.replace("rgba(247, 147, 26, 0.2)", "rgba(255, 215, 0, 0.2)")
    
    # Form focus
    css = css.replace("0 0 0 4px rgba(230, 62, 0, 0.1)", "0 0 0 4px rgba(255, 215, 0, 0.1)")
    
    # 4. Also make the word "HOLIDAYS" in the hero yellow to match the logo perfectly!
    css = css.replace(".hero-sub-text {\n  font-size: clamp(2rem, 7vw, 4.5rem);\n  letter-spacing: 8px;\n  color: var(--white);",
                      ".hero-sub-text {\n  font-size: clamp(2rem, 7vw, 4.5rem);\n  letter-spacing: 8px;\n  color: var(--yellow);")

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    
    print("Theme updated to Logo Theme (Yellow), keeping buttons Orange!")

except Exception as e:
    print(f"Error: {e}")
