import sys
import re

scale = 1.0

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


def process_line(line):
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

    return line


if __name__ == "__main__":
    # Set scale factor
    scale = float(sys.argv[3])

    # Process the kicad_mod file
    with open(sys.argv[1], 'r') as in_file, open(sys.argv[2], 'w', newline='') as out_file:
        for line in in_file:
            out_file.write(process_line(line))
