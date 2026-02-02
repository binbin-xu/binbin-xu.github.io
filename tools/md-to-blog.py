#!/usr/bin/env python3
"""
Markdown to Blog HTML Converter
================================
Converts markdown blog files to styled HTML pages matching the site's design.

Usage:
    python tools/md-to-blog.py <markdown_file> [--update-index]

Examples:
    python tools/md-to-blog.py blogs/2026/2026.md
    python tools/md-to-blog.py blogs/2026/2026.md --update-index

Requirements:
    pip install markdown
"""

import os
import sys
import argparse
import re
from datetime import datetime

try:
    import markdown
except ImportError:
    print("Error: markdown library not found. Install with: pip install markdown")
    sys.exit(1)


def extract_title(content: str) -> str:
    """Extract the title from the markdown content (first H1)."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def extract_excerpt(content: str, max_length: int = 150) -> str:
    """Extract a brief excerpt from the markdown content."""
    # Remove headers
    text = re.sub(r'^#+\s+.+$', '', content, flags=re.MULTILINE)
    # Remove markdown formatting
    text = re.sub(r'[*_`#]', '', text)
    # Get first paragraph
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    if paragraphs:
        excerpt = paragraphs[0][:max_length]
        if len(paragraphs[0]) > max_length:
            excerpt += '...'
        return excerpt
    return ""


def convert_md_to_html(md_content: str) -> str:
    """Convert markdown content to HTML."""
    # Initialize markdown with extensions
    md = markdown.Markdown(extensions=['extra', 'toc'])
    html = md.convert(md_content)
    return html


def generate_blog_page(title: str, content_html: str, relative_path: str = "../../") -> str:
    """Generate a complete blog HTML page."""
    current_date = datetime.now().strftime("%B %Y")
    
    template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Binbin Xu's Blog</title>
    <link rel="stylesheet" type="text/css" href="{relative_path}css/main.css">
    <!-- Google Fonts: Noto Serif SC (SimSun equivalent) and Open Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;600;700&family=Open+Sans:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #fafafa;
            --text-primary: #2c2c2c;
            --text-secondary: #555555;
            --accent-color: #5b6abf;
            --code-bg: #f5f5f5;
        }}

        body {{
            margin: 0;
            padding: 0;
            font-family: 'Noto Serif SC', 'Songti SC', serif; /* Elegant serif for reading */
            background-color: var(--bg-color);
            color: var(--text-primary);
            font-size: 18px; /* Slightly larger for readability */
            line-height: 1.8;
            -webkit-font-smoothing: antialiased;
        }}

        .blog-post-container {{
            max-width: 720px; /* Optimal reading width */
            margin: 0 auto;
            padding: 60px 20px 100px;
        }}

        /* Header */
        .blog-post-header {{
            text-align: center;
            margin-bottom: 60px;
            padding-bottom: 40px;
            border-bottom: 1px solid #e0e0e0;
        }}

        .blog-post-header h1 {{
            font-family: 'Noto Serif SC', serif;
            font-size: 2.8rem;
            font-weight: 700;
            margin: 0 0 15px 0;
            color: #1a1a1a;
            letter-spacing: -0.02em;
            line-height: 1.3;
        }}

        .blog-post-date {{
            font-family: 'Open Sans', sans-serif;
            font-size: 0.95rem;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        /* Content */
        .blog-post-content {{
            font-weight: 400;
        }}

        .blog-post-content p {{
            margin-bottom: 1.8em;
            text-align: justify;
            text-justify: inter-ideograph;
        }}

        .blog-post-content h1 {{ display: none; }} /* Redundant with header */

        .blog-post-content h2 {{
            font-family: 'Noto Serif SC', serif;
            font-size: 1.8rem;
            font-weight: 600;
            color: #000000;
            margin-top: 2.5em;
            margin-bottom: 0.8em;
            border-bottom: 1px solid #eee; /* Subtle underline */
            padding-bottom: 0.3em;
        }}

        .blog-post-content h3 {{
            font-size: 1.4rem;
            font-weight: 600;
            margin-top: 2em;
            margin-bottom: 0.6em;
            color: #333;
        }}

        .blog-post-content ul, .blog-post-content ol {{
            margin-bottom: 1.8em;
            padding-left: 2em;
        }}

        .blog-post-content li {{
            margin-bottom: 0.5em;
        }}

        .blog-post-content a {{
            color: var(--accent-color);
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: border-color 0.2s;
        }}

        .blog-post-content a:hover {{
            border-bottom-color: var(--accent-color);
        }}
        
        /* Code blocks */
        .blog-post-content pre {{
            background: var(--code-bg);
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Menlo', 'Monaco', monospace;
            font-size: 0.9em;
            margin-bottom: 1.8em;
        }}

        /* Navigation */
        .nav-links {{
            display: flex;
            justify-content: space-between;
            margin-top: 80px;
            padding-top: 40px;
            border-top: 1px solid #e0e0e0;
        }}

        .nav-link {{
            font-family: 'Open Sans', sans-serif;
            font-size: 1rem;
            color: #666;
            text-decoration: none;
            transition: color 0.2s;
            display: inline-flex;
            align-items: center;
        }}

        .nav-link:hover {{
            color: var(--accent-color);
        }}

        @media (max-width: 768px) {{
            .blog-post-container {{
                padding-top: 40px;
            }}
            .blog-post-header h1 {{
                font-size: 2rem;
            }}
            body {{
                font-size: 17px;
            }}
        }}
    </style>
</head>
<body>
    <div class="blog-post-container">
        <header class="blog-post-header">
            <h1>{title}</h1>
            <div class="blog-post-date">{current_date}</div>
        </header>

        <article class="blog-post-content">
            {content_html}
        </article>

        <nav class="nav-links">
            <a href="{relative_path}blog.html" class="nav-link">← Back to Blog</a>
            <a href="{relative_path}index.html" class="nav-link">Home</a>
        </nav>
    </div>
</body>
</html>'''
    
    return template


def generate_blog_card(title: str, excerpt: str, html_path: str, date: str = None) -> str:
    """Generate a blog card HTML snippet for the blog index."""
    if date is None:
        date = datetime.now().strftime("%B %Y")
    
    return f'''
            <!-- Blog Post: {title} -->
            <a href="{html_path}" class="blog-card">
                <div class="blog-card-title">{title}</div>
                <div class="blog-card-date">{date}</div>
                <div class="blog-card-excerpt">
                    {excerpt}
                </div>
                <span class="blog-card-read-more">阅读全文 →</span>
            </a>
'''


def main():
    parser = argparse.ArgumentParser(
        description="Convert Markdown blogs to styled HTML pages",
        epilog="Example: python tools/md-to-blog.py blogs/2026/2026.md"
    )
    parser.add_argument("markdown_file", help="Path to the markdown file to convert")
    parser.add_argument("--update-index", action="store_true", 
                       help="Add a blog card to blog.html (requires manual placement)")
    parser.add_argument("--output", "-o", help="Output HTML file path (default: same directory as input)")
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.markdown_file):
        print(f"Error: File not found: {args.markdown_file}")
        sys.exit(1)
    
    # Read markdown content
    with open(args.markdown_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract metadata
    title = extract_title(md_content)
    excerpt = extract_excerpt(md_content)
    
    # Convert to HTML
    content_html = convert_md_to_html(md_content)
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        output_path = os.path.splitext(args.markdown_file)[0] + '.html'
    
    # Calculate relative path to root
    depth = len(os.path.dirname(args.markdown_file).split(os.sep))
    relative_path = "../" * depth if depth > 0 else ""
    
    # Generate full HTML page
    html_page = generate_blog_page(title, content_html, relative_path)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_page)
    
    print(f"✅ Created: {output_path}")
    print(f"   Title: {title}")
    
    if args.update_index:
        # Generate blog card HTML for manual insertion
        html_rel_path = args.markdown_file.replace('.md', '.html')
        card_html = generate_blog_card(title, excerpt, html_rel_path)
        
        print("\n📝 Add this to blog.html inside <div class=\"blog-list\">:")
        print(card_html)
    
    print("\n💡 Next steps:")
    print("   1. Open the generated HTML file to verify formatting")
    print("   2. Add a blog card entry to blog.html if not done automatically")
    print("   3. Commit and push to deploy")


if __name__ == "__main__":
    main()
