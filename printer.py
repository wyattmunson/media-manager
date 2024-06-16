def format_header_text(text, longest_txt_width):
    total_width = longest_txt_width + 4
    txt_width = len(text)
    total_buffer = total_width - txt_width
    half_buffer = total_buffer // 2
    # print(f"Tot wt: {total_width}, Txt wt: {txt_width}, Tot Buff: {total_buffer}, Half Buff: {half_buffer}")
    formatted_text = (half_buffer * " ") + text + (half_buffer * " ")
    return formatted_text


def render_header(header_text, sub_text=None, trailing_newline=True, leading_newline=False, line_char="="):
    longest_txt_width = 0
    if sub_text:
        longest_txt_width = len(header_text) if len(header_text) >= len(sub_text) else len(sub_text)
    else:
        longest_txt_width = len(header_text)
    
    total_width = longest_txt_width + 4
    fmt_header = format_header_text(header_text, longest_txt_width)
    fmt_sub = format_header_text(sub_text, longest_txt_width) if sub_text else None
    
    if leading_newline == True: print("")
    print(total_width * line_char)
    print(fmt_header)
    if sub_text: print(fmt_sub)
    print(total_width * line_char)
    if trailing_newline == True: print("")
    

def render_menu(title, items):
    print("=" * (len(title) + 4))
    print("  " + title)
    print("=" * (len(title) + 4))
    
    for index, item in enumerate(items):
        print(f"{index}. {item}")

