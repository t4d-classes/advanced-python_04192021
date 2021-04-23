from distutils.core import setup, Extension


def main():
    setup(name="myfputs",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="Eric Greene",
          author_email="eric@t4d.io",
          ext_modules=[Extension("myfputs", ["myfputsmodule.c"])])


if __name__ == "__main__":
    main()
