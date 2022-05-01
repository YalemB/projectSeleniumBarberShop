

def insert_data_to_form(elemnet,l):
    x = 0
    for i in elemnet:
        if i.tag_name == "input" or i.tag_name == "textarea":
            if x < 3:
                i.send_keys(l[x])
                x += 1
            else:
                i.click()

