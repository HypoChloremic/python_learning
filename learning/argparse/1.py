import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-a', nargs=2)

# An illustration of how access the arguments.
# Den här kommer att spara det the user har entered, vilket är värt att förstå.
# Alltså, när användaren skriver exempelvis python 1.py -a hello world (för att -a
# accepterar två arguemnts) kommer man att spara skiten i en Namespace lista,
# verkar det som, där man har equatat argumenten utan bindestreck med the values 
# man entered som en string!

opts = ap.parse_args()
print(opts.a) # this will print a stringed list!
opts = ap.parse_args([])


# To require that at least one option be supplied (-a, -b, or -c)
# you have to write your own logic. For example:

if not any([opts.a, opts.b, opts.c]):
    ap.print_usage()
    quit()

print("This won't run.")