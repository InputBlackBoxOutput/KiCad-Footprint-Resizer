import streamlit as st
import script

st.set_page_config(page_title='KiCad Footprint Resizer',
                   page_icon='🛠️', layout='centered')
st.title("KiCad Footprint Resizer")

footprint = st.file_uploader("Upload footprint file", type=['kicad_mod'])

if footprint is not None:
    with open("footprint", 'wb') as footprint_file:
        footprint_file.write(footprint.read())

    script.scale = st.number_input(label="Scale", value=0.5)

    try:
        output = ""

        with open("footprint", 'r') as file:
            for line in file.read().splitlines():
                output += script.process_line(line) + '\n'

    except Exception:
        st.error("Something went wrong!")
        st.stop()

    if st.button("Resize", use_container_width=True):
        st.markdown("-----")
        st.success("Footprint resized successfully!")

        st.download_button(
            label="Download footprint",
            data=output,
            file_name="footprint.kicad_mod",
            mime="plain/text",
            use_container_width=True
        )

st.markdown("""\n
-----
##### Made with lots of ⏱️, 📚 and ☕ by InputBlackBoxOutput
""")
