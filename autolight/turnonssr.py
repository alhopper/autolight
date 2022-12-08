#!/usr/bin/env python3

import controlssr


def main():
    controlssr.init_rpi_io()
    controlssr.turn_on_light()

if __name__ == '__main__':
    main()
