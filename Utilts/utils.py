


def insert_data_to_form(form_element,data_fields):
    index = 0
    for i in form_element:
        if i.tag_name == "input" or i.tag_name == "textarea":
            if index < 3:
                i.send_keys(data_fields[index])
                index += 1

def is_send_message_button_enabled(form_element):
    button = form_element[-1]
    return button.is_enabled()


def test_send_message_button(form_element,
                             data_fields,
                             expected_is_enabled):
    insert_data_to_form(form_element, data_fields)
    is_enabled = is_send_message_button_enabled(form_element)

    assert is_enabled == expected_is_enabled