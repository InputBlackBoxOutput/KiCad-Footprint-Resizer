import streamlit as st
import re

st.set_page_config(page_title='KiCad Footprint Resizer',
                   page_icon='🛠️', layout='centered')
st.title("KiCad Footprint Resizer")

footprint = st.file_uploader("Upload footprint file", type=['kicad_mod'])


def scale_start(val):
    x = float(val.group(1)) * scale
    y = float(val.group(2)) * scale
    return f'(start {x} {y})'


def scale_mid(val):
    x = float(val.group(1)) * scale
    y = float(val.group(2)) * scale
    return f'(mid {x} {y})'


def scale_center(val):
    x = float(val.group(1)) * scale
    y = float(val.group(2)) * scale
    return f'(center {x} {y})'


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
    return f'(at {x} {y}'


def scale_drill(val):
    x = float(val.group(1)) * scale
    return f'(drill {x})'


def scale_width(val):
    x = float(val.group(1)) * scale
    return f'(width {x})'


def scale_thickness(val):
    x = float(val.group(1)) * scale
    return f'(thickness {x})'


if footprint is not None:
    with open("footprint", 'wb') as footprint_file:
        footprint_file.write(footprint.read())

    scale = st.number_input(label="Scale", value=0.5)

    try:
        output = ""

        with open("footprint", 'r') as file:
            for line in file.read().splitlines():
                line = re.sub(r'\(start ([0-9-.]+) ([0-9-.]+)\)', scale_start, line)
                line = re.sub(r'\(mid ([0-9-.]+) ([0-9-.]+)\)', scale_mid, line)
                line = re.sub(r'\(center ([0-9-.]+) ([0-9-.]+)\)', scale_center, line)
                line = re.sub(r'\(end ([0-9-.]+) ([0-9-.]+)\)', scale_end, line)
                line = re.sub(r'\(width ([0-9-.]+) ([0-9-.]+)\)', scale_width, line)
                line = re.sub(r'\(size ([0-9-.]+) ([0-9-.]+)\)', scale_size, line)
                line = re.sub(r'\(xy ([0-9-.]+) ([0-9-.]+)\)', scale_xy, line)
                line = re.sub(r'\(at ([0-9-.]+) ([0-9-.]+)', scale_at, line)
                line = re.sub(r'\(drill ([0-9-.]+)\)', scale_drill, line)
                line = re.sub(r'\(width ([0-9-.]+)\)', scale_width, line)
                line = re.sub(r'\(thickness ([0-9-.]+)\)', scale_thickness, line)

                print(line)
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
