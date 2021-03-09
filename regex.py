regex_pair = '\s([a-zA-Z0-9_-]{0,10})_([a-zA-Z0-9_-]{0,10})$'
regex_one = '\s([a-zA-Z0-9_-]{0,20})$'

all_regex_one = (f"(^!{regex_one})|"
                 f"(^!c{regex_one})|"
                 f"(^\/c{regex_one})|"
                 f"(^\/price{regex_one})")

all_regex_pair = (f"(^\/c{regex_pair})|"
                  f"(^!c{regex_pair})|"
                  f"(^!{regex_pair})|"
                  f"(^!pair{regex_pair})|"
                  f"(^\/pair{regex_pair})|"
                  f"(^\/price{regex_pair})")