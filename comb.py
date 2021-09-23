
def comb(paragraph: str):
    return paragraph.replace('\n', ' ')


if __name__ == '__main__':
    paragraph = """Rust is a programming language created by Graydon Hoare while working at
Mozilla Research. He first started working on it around 2006 as a personal
project, and by 2010 Mozilla had sponsored and announced the project.
While the language is relatively new, it has quickly earned a passionate
following of programmers who claim to even love using it."""
    print(comb(paragraph))
