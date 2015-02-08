#!/usr/bin/python

import controlssr


def main():
    controlssr.init_rpi_io()
    controlssr.turn_off_light()

if __name__ == '__main__':
    main()
