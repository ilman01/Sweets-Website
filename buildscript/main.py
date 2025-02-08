import os
import shutil

def copy_and_replace(input_file, output_file, things_to_replace, replacements):
    """
    Copies the content of input_file to output_file,
    replacing occurrences of placeholders with provided values.
    things_to_replace and replacements should be lists of the same length.
    """
    if len(things_to_replace) != len(replacements):
        raise ValueError("Both lists should have the same length.")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        # Replace placeholders
        for i in range(len(things_to_replace)):
            content = content.replace(things_to_replace[i], replacements[i])
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        
        print(f"File '{output_file}' has been created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def copy_file(input_path, output_path):
    """
    Copies a file from input_path to output_path.
    """
    shutil.copy(input_path, output_path)
    print(f"File copied from {input_path} to {output_path}")

def replace_in_string(content, things_to_replace, replacements):
    """
    Replaces occurrences of placeholders in the given content string with provided values.
    things_to_replace and replacements should be lists of the same length.
    """
    if len(things_to_replace) != len(replacements):
        raise ValueError("Both lists should have the same length.")
    
    # Replace placeholders
    for i in range(len(things_to_replace)):
        content = content.replace(things_to_replace[i], replacements[i])
    
    return content

def make_directory_if_hasnt(path_to_directory):
    """
    Creates the specified directory if it doesn't exist, including parent directories.
    """
    os.makedirs(path_to_directory, exist_ok=True)

def file_lines_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def read_file(input_path):
    """
    Reads a file and returns its contents.
    """
    with open(input_path, 'r', encoding='utf-8') as file:
        return file.read()

def parse_key_value_file_wrapped_curly_braces(file_path):
    """
    Example usage:
    left_side_list, right_side_list = parse_key_value_file("your_file.txt")
    """
    left_side = []
    right_side = []
    
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.split(':', 1)
                left_side.append(f'{{{key.strip()}}}')
                right_side.append(value.strip())
    
    return left_side, right_side





def home_html_builder():
    left_side_data_list, right_side_data_list = parse_key_value_file_wrapped_curly_braces("site_configs.txt")
    copy_and_replace("./templates/home.html", "../index.html", left_side_data_list, right_side_data_list)

def header_js_builder():
    left_side_data_list, right_side_data_list = parse_key_value_file_wrapped_curly_braces("site_configs.txt")
    copy_and_replace("./templates/header.js", "../header.js", left_side_data_list, right_side_data_list)

def headloader_js_builder():
    left_side_data_list, right_side_data_list = parse_key_value_file_wrapped_curly_braces("site_configs.txt")
    copy_and_replace("./templates/headloader.js", "../headloader.js", left_side_data_list, right_side_data_list)

def search_html_builder():
    make_directory_if_hasnt("../search/")
    copy_file("./templates/search.html", "../search/index.html")

def favicon_builder():
    copy_file("./favicon/logo.ico", "../logo.ico")

def video_html_builder():
    videos_data_pointer = file_lines_to_list("./video_post_data/1_order_of_data_videos_data_pointer")

    for video_data_pointer in videos_data_pointer:
        left_side_data_list, right_side_data_list = parse_key_value_file_wrapped_curly_braces(f"./video_post_data/{video_data_pointer}")
        make_directory_if_hasnt(f"../video/{video_data_pointer}/")
        copy_and_replace("./templates/video_page.html", f"../video/{video_data_pointer}/index.html", left_side_data_list, right_side_data_list)

def contentgrid_js_builder():
    videos_data_pointer = file_lines_to_list("./video_post_data/1_order_of_data_videos_data_pointer")
    final_html = ""

    card = read_file("./templates/contentgrid_card.html")

    for video_data_pointer in videos_data_pointer:
        video_page_link = f"/video/{video_data_pointer}/"

        left_side_data_list, right_side_data_list = parse_key_value_file_wrapped_curly_braces(f"./video_post_data/{video_data_pointer}")

        left_side_data_list.append("{video_page_link}")
        right_side_data_list.append(video_page_link)

        final_html += replace_in_string(card, left_side_data_list, right_side_data_list) + "\n"
    
    copy_and_replace("./templates/contentgrid.js", "../contentgrid.js", ["{cards}"], [final_html])

if __name__ == "__main__":
    home_html_builder()
    header_js_builder()
    headloader_js_builder()
    search_html_builder()
    favicon_builder()
    video_html_builder()
    contentgrid_js_builder()