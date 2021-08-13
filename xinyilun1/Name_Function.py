def get_fomatted_name(first,last,middle=""):
    "全名=姓+中间+名"
    if middle:
        full_name = first+""+middle+""+last
    else:
        full_name = first+""+last
    return full_name
