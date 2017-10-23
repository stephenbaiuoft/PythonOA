import re;

def process_line(input, re_pattern):
    #prog = re.compile(pattern)
    result = re_pattern.match(input)

    pass


def init_regex():
    rc_html = re.compile(r'(</*html[\w\d\s"\'=]*>)', re.IGNORECASE)
    rc_head = re.compile(r'(</*head[\w\d\s"\'=]*>)', re.IGNORECASE)
    rc_title = re.compile(r'(</*title[\w\d\s"\'=]*>)', re.IGNORECASE)
    rc_body = re.compile(r'(</*body[\w\d\s"\'=]*>)', re.IGNORECASE)
    rc_br = re.compile(r'(<br[\s=]*>)', re.IGNORECASE)
    rc_h = re.compile(r'(</*h[1-7][\w\d\s"\'=]*>)', re.IGNORECASE)
    rc_p = re.compile(r'(</*p[\w\d\s"\'=]*>)', re.IGNORECASE)
    rc_a = re.compile(r'(</*A[\w\d\s"\'=]*>)', re.IGNORECASE)

    rcm_html = r'\\color[RED]\1'
    rcm_r_head = r'\\color[YELLOW]\1'
    rcm_title = r'\\color[GREEN]\1'
    rcm_r_body = r'\\color[TURQUOISE]\1'
    rcm_br = r'\\color[PINK]\1'
    rcm_h = r'\\color[DARKGREEN]\1'
    rcm_p = r'\\color[DARKGRAY]\1'
    rcm_a = r'\\color[BLUE]\1'


    pass