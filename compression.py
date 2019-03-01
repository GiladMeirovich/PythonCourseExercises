#!/usr/bin/env python3
"""
compression module
Uses:
    compress an str type by characters
"""


def compress_str(to_compress):
    """
    compresses an str type

    Args:
        to_compress - str type to compress

    Return:
        The compressed str type
    """
    if to_compress == "":
        return ""

    compressed_str = ""
    current_c = to_compress[0]
    counter = 0
    for c in to_compress:
        if c == current_c:
            counter += 1
        else:
            compressed_str += current_c
            compressed_str += str(counter)
            counter = 1
            current_c = c

    compressed_str += current_c
    compressed_str += str(counter)

    return compressed_str


def test():
    """
    Tests the compression on str type given as input
    """
    print("Enter a string")
    kelet = input()
    print("Compressed string:")
    print(compress_str(kelet))


def main():
    test()


if __name__ == '__main__':
    main()