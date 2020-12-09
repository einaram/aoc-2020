import timeit


t = timeit.timeit('run_console_try(parse_input())',
                  setup='from Day8 import run_console, parse_input, run_console_try ', number=5000)
print("run_console try", t)

t = timeit.timeit('run_console(parse_input())',
                 setup='from Day8 import run_console, parse_input, run_console_try ', number=5000)
print("run_console len", t)




