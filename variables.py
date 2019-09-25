#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: September 2019
# This program shows how global and local variables work

# global variable
variable_X = 25


def local_variable():
    # This shows what happens with local variables

    variable_X = 10
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print("Local variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
          format(variable_X, variable_Y, variable_Z))


def global_varible():
    # This shows what happens with global variables

    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print("Global variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
          format(variable_X, variable_Y, variable_Z))


def main():
    # This function shows how global and local variables work

    local_variable()
    global_varible()


if __name__ == "__main__":
    main()
