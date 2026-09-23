import re, html, urllib.parse, os

def validate_email(email: str) -> bool:
    """Validate email format, disallowing leading/trailing dots around username or consecutive dots."""
    pattern = r'^[a-zA-Z0-9_%+-]+(?:\.[a-zA-Z0-9_%+-]+)*@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email) is not None

def validate_url(url: str) -> bool:
    """Validate URL scheme and hostname format (disallowing empty domain labels or special characters)."""
    try:
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme not in ['http', 'https']:
            return False
        hostname = parsed.hostname
        if not hostname:
            return False

        # Domain regex: valid labels (letters, numbers, hyphens) separated by dots, with 2+ char TLD
        domain_pattern = r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
        ip_pattern = r'^(?:\d{1,3}\.){3}\d{1,3}$'

        return bool(
            re.fullmatch(domain_pattern, hostname) or
            re.fullmatch(ip_pattern, hostname) or
            hostname == 'localhost'
        )
    except Exception:
        return False

def validate_filename(filename: str) -> bool:
    """Prevent path traversal and enforce valid filename format with safe alphabetic extensions."""
    if not filename or ".." in filename or "/" in filename or "\\" in filename or "\x00" in filename:
        return False
    if os.path.basename(filename) != filename:
        return False
    # Base name (letters, numbers, _, -, spaces) + extension (2 to 5 letters)
    pattern = r'^[a-zA-Z0-9_\s-]+\.[a-zA-Z]{2,5}$'
    if not re.fullmatch(pattern, filename):
        return False
    # Block dangerous executable extensions
    ext = filename.rsplit('.', 1)[-1].lower()
    dangerous_exts = {'php', 'exe', 'bat', 'cmd', 'sh', 'pl', 'cgi', 'vbs', 'py', 'js'}
    return ext not in dangerous_exts

def sanitize_sql_input(input_str: str) -> str:
    """Sanitize SQL input to prevent SQL injection."""
    sanitized = re.sub(r"(--|;|'|\"|#)", "", input_str)
    sanitized = re.sub(r"\b(OR|AND|SELECT|INSERT|DELETE|UPDATE|DROP|UNION|WHERE)\b",
                       "", sanitized, flags=re.IGNORECASE)
    return sanitized.strip()

def sanitize_html_input(html_str: str) -> str:
    """Escape HTML input to prevent XSS."""
    return html.escape(html_str)
