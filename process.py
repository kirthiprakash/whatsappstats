import simplejson
import re


pattern = "(2015/\d\d?/\d \d\d?:\d\d - )((?s).*)"

name_msglen_map = {}
name_chatcount_map = {}
date_name_msg_map = {}
name = msg = None
with open("Local_muchass.txt", 'r') as chat_file:
    while True:
        line = chat_file.readline()
        if not line:
            break
        m = re.match(pattern, line)
        if m:
            if name and msg:
                if name_msglen_map.has_key(name):
                    name_msglen_map[name] += len(msg)
                else:
                    name_msglen_map[name] = len(msg)
            if name:
                if name_chatcount_map.has_key(name):
                    name_chatcount_map[name] += 1
                else:
                    name_chatcount_map[name] = 1
            name = ""
            msg = ""
            time = m.group(1)
            name_msg = m.group(2)
            arr = name_msg.split(':')
            if arr:
                name = arr[0]
                msg = ""
                for elems in arr[1:]:
                    msg += elems
        else:
            msg += line

    print simplejson.dumps(name_msglen_map, indent=2)
    print simplejson.dumps(name_chatcount_map, indent=2)