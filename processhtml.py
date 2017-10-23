import re;


def process_line(input, r_dic):
    #prog = re.compile(pattern)
    for rc_pattern, cm_pattern in r_dic:
        # updating input through all regex expressions
        input = rc_pattern.sub(cm_pattern, input, 0 )

    return input


# init dictionary of regex for html tags
def init_regex():
    rc_html = r'(</*html[\w\d\s"\'=]*>)'
    rc_head = r'(</*head[\w\d\s"\'=]*>)'
    rc_title = r'(</*title[\w\d\s"\'=]*>)'
    rc_body = r'(</*body[\w\d\s"\'=]*>)'
    rc_br = r'(<br[\s=]*>)'
    rc_h = r'(</*h[1-7][\w\d\s"\'=]*>)'
    rc_p = r'(</*p[\w\d\s"\'=]*>)'
    rc_a = r'(</*A[\w\d\s"\'=]*>)'

    cm_html = r'\\color[RED]\1'
    cm_head = r'\\color[YELLOW]\1'
    cm_title = r'\\color[GREEN]\1'
    cm_r_body = r'\\color[TURQUOISE]\1'
    cm_br = r'\\color[PINK]\1'
    cm_h = r'\\color[DARKGREEN]\1'
    cm_p = r'\\color[DARKGRAY]\1'
    cm_a = r'\\color[BLUE]\1'

    r_dic = {rc_html: cm_html,
             rc_head: cm_head,
             rc_title: cm_title,
             rc_body: cm_r_body,
             rc_br: cm_br,
             rc_h: cm_h,
             rc_p: cm_p,
             rc_a: cm_a
             }

    return r_dic
