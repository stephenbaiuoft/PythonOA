import re;


def process_line(input, r_dic):
    #prog = re.compile(pattern)
    for rc_pattern, cm_pattern in r_dic.items():
        # updating input through all regex expressions
        input = re.sub(rc_pattern, cm_pattern, input, 0, re.IGNORECASE)

    return input


# init dictionary of regex for html tags
def init_regex():
    # regex of opening tag
    rc_html = r'(<html[\w\d\s"\'=]*>)'
    rc_head = r'(<head[\w\d\s"\'=]*>)'
    rc_title = r'(<title[\w\d\s"\'=]*>)'
    rc_body = r'(<body[\w\d\s"\'=]*>)'
    rc_br = r'(<br[\s=]*>)'
    rc_h = r'(<h[1-7][\w\d\s"\'=]*>)'
    rc_p = r'(<p[\w\d\s"\'=]*>)'
    rc_a = r'(<A[\w\d\s"\'=]*>)'

    # regex of closing tag
    rc_chtml = r'(\s*)([^<>]*[\w\d\s"\']*</html[\w\d\s"\'=]*>)'
    rc_chead = r'(\s*)([^<>]*[\w\d\s"\']*</head[\w\d\s"\'=]*>)'
    rc_ctitle = r'(\s*)([^<>]*[\w\d\s"\']*</title[\w\d\s"\'=]*>)'
    rc_cbody = r'(\s*)([^<>]*</body[\w\d\s"\'=]*>)'
    rc_ch = r'(\s*)([^<>]*[\w\d\s"\']*</h[1-7][\w\d\s"\'=]*>)'
    rc_cp = r'(\s*)([^<>]*[\w\d\s"\'\.]*</p[\w\d\s"\'=]*>)'
    rc_ca = r'(\s*)([^<>]*[\w\d\s"\']*</A[\w\d\s"\'=]*>)'

    # replacing of open tag
    cm_html = r'\\color[RED]\1'
    cm_head = r'\\color[YELLOW]\1'
    cm_title = r'\\color[GREEN]\1'
    cm_body = r'\\color[TURQUOISE]\1'
    cm_br = r'\\color[PINK]\1'
    cm_h = r'\\color[DARKGREEN]\1'
    cm_p = r'\\color[DARKGRAY]\1'
    cm_a = r'\\color[BLUE]\1'

    # replacing of closing tag
    cm_chtml = r'\1\\color[RED]\2'
    cm_chead = r'\1color[YELLOW]\2'
    cm_ctitle = r'\1\\color[GREEN]\2'
    cm_cbody = r'\1\\color[TURQUOISE]\2'
    cm_ch = r'\1\\color[DARKGREEN]\2'
    cm_cp = r'\1\\color[DARKGRAY]\2'
    cm_ca = r'\1\\color[BLUE]\2'


    r_dic = {rc_html: cm_html,
             rc_head: cm_head,
             rc_title: cm_title,
             rc_body: cm_body,
             rc_br: cm_br,
             rc_h: cm_h,
             rc_p: cm_p,
             rc_a: cm_a,

             rc_chtml: cm_chtml,
             rc_chead: cm_chead,
             rc_ctitle: cm_ctitle,
             rc_cbody: cm_cbody,
             rc_ch: cm_ch,
             rc_cp: cm_cp,
             rc_ca: cm_ca

             }

    return r_dic
