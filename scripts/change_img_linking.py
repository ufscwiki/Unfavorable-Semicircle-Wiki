#!/bin/python3

# md image formatting fixing fileing originally by N25_CT13 which is me Hi :)

import os



def _skip_to(string:str, start:int, end_chars:str) -> int:
    # this is to skip any in quote parenthesis and escaped characters

    point = start-1
    len_string = len(string)
    in_quotes = False
    quote_type = ''

    while point <= len_string-2:
        point += 1
        char = string[point]

        if char == '\\':
            point += 1
            continue
        elif char in '"\'':
            if in_quotes and quote_type == char:
                in_quotes = False
            else:
                in_quotes = True
                quote_type = char
        elif char in end_chars and not in_quotes:
            return point
    
    return -1# error

def _right_skip_to(string:str, start:int, end_chars:str, ignore_quotes=True) -> int:
    # same as above, from the right. what's a DRY??

    point = start
    len_string = len(string)
    in_quotes = False
    quote_type = ''

    while point > 0:
        point -= 1
        
        char = string[point]
        if point > 0:
            escaped = string[point-1] == '\\' 

        if escaped:
            point -= 1
            continue
        elif char in '"\'' and not ignore_quotes:
            if in_quotes and quote_type == char:
                in_quotes = False
            else:
                in_quotes = True
                quote_type = char
        elif char in end_chars and not in_quotes:
            return point
    
    return -1# error


def format_image_linking(
        file_path:str,
        preserve_alt_text=False,
        preserve_hover_text=False,
        create_new_hover_text=True,

        log_found_image_tags=False
        ):
    """formats a markdown file to fix up image linking, and writes it back to disk."""
    # this formatting doesn't use regex, and is inefficient.
    # Sorry i just don't like using regexes they are hard to look at

    # it's maybe prone to weird name edge cases i think. idk..

    with open(file_path, 'r') as f:
        data = f.read()

    data_out = ''
    
    point = 0
    data_len = len(data)
    while point < data_len:
        
        if data[point:point+2] == '![' or data[point:point+3] == '[![':

            # point finding
            linked = data[point] == '['
            if linked: point += 1
            
            if log_found_image_tags:
                print(f"  found an image tag at character {point}")

            alt_start = point+1
            alt_end = _skip_to(data, alt_start, ']')+1
            img_start = alt_end
            img_end = _skip_to(data, img_start, ')')+1
            if linked:
                wrap_start = point-1
                wrap_end = img_end+1
                link_start = wrap_end
                link_end = _skip_to(data, link_start, ')]')+1
                tag_start = wrap_start
                tag_end = link_end
            else:
                tag_start = point
                tag_end = img_end
            
            # data "extraction" and modification
            img = data[img_start+1:img_end-1]
            
            # doing this so because files can have spaces like that. Ugh spaces
            if img[-1] == '"':
                hover_text_end = len(img)-1
                hover_text_start = _right_skip_to(img, hover_text_end, '"')+1
                img_path_end = hover_text_start-2
                img_path = img[:img_path_end]
                hover_text = img[hover_text_start:hover_text_end]
            else:
                img_path = data[img_start+1:img_end-1]
                hover_text = None

            split = img_path.rsplit('.', 2)
            is_full = split[1] == 'full'
            if is_full:
                full_size_path = '.'.join(split)
                split.pop(1)
                regular_size_path = '.'.join(split)
            else:
                regular_size_path = '.'.join(split)
                split.insert(1, 'full')
                full_size_path = '.'.join(split)
            
            if preserve_alt_text:
                alt_text = data[alt_start+1:alt_end-1]
            else:
                alt_text = regular_size_path
            
            # NOTE You can edit the hover/title text here, if you need to.
            # For example: hover_text = f"{regular_size_path} Click to go to the Full sized file."
            if (create_new_hover_text and hover_text is None) or not preserve_hover_text:
                hover_text = regular_size_path
    
            # the rebuilt image link
            fixed = f"[![{alt_text}]({regular_size_path}{' "'+hover_text+'"' if hover_text else ''})]({full_size_path})"
            
            # revert if image doesn't exist
            if not os.path.exists(f'docs/{full_size_path}'):
                fixed = data[tag_start:tag_end]
                
            if log_found_image_tags:
                print(f"    original tag: '{data[tag_start:tag_end]}'")
                print(f"    replacing with: '{fixed}'")
            data_out += fixed
            point = tag_end
        else:
            data_out += data[point]
            point += 1
    
    with open(file_path, 'w') as f:
        f.write(data_out)

def _yesnoq(text):
    uinp = input(text)
    return uinp and uinp[0].lower() == 'y'

def _yesnod(text, default):
    uinp = input(text)
    if uinp:
        return uinp[0].lower() == 'y'
    return default

def main():
    while 1:
        uinp = input("enter the formatting root directory (leave blank to use the script directory, \"!exit\" to exit)\n> ")
        if uinp:
            if len(uinp) >= 2 and uinp.lower()[:2] == "!e":
                print("Exiting")
                return
            if not os.path.exists(uinp):
                print("Invalid path. Try again.")
                continue
            root_directory = uinp
        else:
            root_directory = os.path.dirname(os.path.realpath(__file__))
        uinp = input((
           f"Set the formatting root to '{root_directory}'.\n"
            "Plz confirm (Yes/No/Exit)\n> "
        ))
        if uinp:
            match uinp[0].lower():
                case 'y':
                    break
                case 'e':
                    print("Exiting")
                    return
    
    uinp = input((
        "\nhow vocal should the formatting be?\n"
        "2 - file paths and found image tags\n"
        "1 - file paths\n"
        "anything else - silent\n"
        "> "
    ))

    log_file_paths = False
    log_found_image_tags = False

    if uinp:
        match uinp[0]:
            case '1':
                log_file_paths = True
            case '2':
                log_file_paths = True
                log_found_image_tags = True
            case _:
                pass
    
    print("Settings time. Leave blank for default.")
    preserve_alt_text = _yesnod("Preserve alt text? (Yes/No (default)) > ", 0)
    preserve_hover_text = _yesnod("Preserve existing hover text? (Yes/No (default)) > ", 0)
    create_hover_text = _yesnod("Create new hover text when possible? (Yes (default)/No) > ", 1)
    
    print("\nfinding files...")
    markdown_files = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if os.path.splitext(file)[1] == ".md":
                abs_path = os.path.join(root, file)
                if log_file_paths:
                    print(f"found {abs_path}")
                markdown_files.append(abs_path)
    
    files_amt = len(markdown_files)
    plural = files_amt > 1

    uinp = _yesnoq((
       f"\nThis operation will try to format {files_amt} markdown (.md) file{'s' if plural else ''}.\n"
       f"Please make sure the file{'s are' if plural else ' is'} backed up before committing to formatting.\n"
        "The script assumes that each file is valid to begin with.\n"
        "If something breaks and there were no backups, I'm not to blame.\n"
        "Thank you for understanding.\n"
        "\nAre you sure you want to continue to formatting? (Yes/No (exit))\n> "
    ))
    if not uinp:
        print("Exiting")
        return

    print("Starting formatting.")
    for file in markdown_files:
        if log_file_paths:
            print(f"Formatting {file}")
        format_image_linking(
            file,
            preserve_alt_text = preserve_alt_text,
            preserve_hover_text = preserve_hover_text,
            create_new_hover_text = create_hover_text,

            log_found_image_tags = log_found_image_tags
        )

    print(f"Finished formatting {files_amt} file{'s' if plural else ''}.")
    print("Ty 4 using the script - N25_CT13")




if __name__ == "__main__":
    main()
