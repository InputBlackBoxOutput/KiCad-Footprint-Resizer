import streamlit as st
import re

st.set_page_config(page_title='KiCad Footprint Resizer', page_icon='🛠️', layout='centered')
st.title("KiCad Footprint Resizer")

footprint = st.file_uploader("Upload footprint file", type=['kicad_mod'])


def scale_start(val):
    x = float(val.group(1)) * scale
    y = float(val.group(2)) * scale
    return f'(start {x} {y})'


def scale_end(val):
    x = float(val.group(1)) * scale
    y = float(val.group(2)) * scale
    return f'(end {x} {y})'


def scale_width(val):
    x = float(val.group(1)) * scale
    y = float(val.group(2)) * scale
    return f'(width {x} {y})'


def scale_size(val):
    x = float(val.group(1)) * scale
    y = float(val.group(2)) * scale
    return f'(size {x} {y})'


def scale_xy(val):
    x = float(val.group(1)) * scale
    y = float(val.group(2)) * scale
    return f'(xy {x} {y})'


def scale_at(val):
    x = float(val.group(1)) * scale
    y = float(val.group(2)) * scale
    return f'(at {x} {y})'


if footprint is not None:
    with open("footprint", 'wb') as footprint_file:
        footprint_file.write(footprint.read())

    scale = st.number_input(label="Scale", value=0.5)

    try:
        # Source: https://gist.github.com/urish/9c5b4aea6362da086541be14acdf0f72#gistcomment-4298113
        output = ""

        with open("footprint", 'r') as file:
            for line in file.read().splitlines():
                line = re.sub(r'\(start ([0-9-.]+) ([0-9-.]+)\)', scale_start, line)
                line = re.sub(r'\(end ([0-9-.]+) ([0-9-.]+)\)', scale_end, line)
                line = re.sub(r'\(width ([0-9-.]+) ([0-9-.]+)\)', scale_width, line)
                line = re.sub(r'\(size ([0-9-.]+) ([0-9-.]+)\)', scale_size, line)
                line = re.sub(r'\(xy ([0-9-.]+) ([0-9-.]+)\)', scale_xy, line)
                line = re.sub(r'\(at ([0-9-.]+) ([0-9-.]+)\)', scale_at, line)

                output += line + '\n'

    except Exception:
        st.error("Something went wrong!")
        st.stop()

    if st.button("Resize"):
        st.markdown("-----")
        st.success("Footprint resized successfully!") 

        st.download_button(
            label="Download footprint", 
            data=output, 
            file_name="footprint.kicad_mod", 
            mime="plain/text")

st.markdown("""

-----
##### Made with lots of ⏱️, 📚 and ☕ by InputBlackBoxOutput
""")