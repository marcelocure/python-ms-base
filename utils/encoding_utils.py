def decode(str):
    return str.decode('unicode_escape').encode('ascii', 'replace').strip()
