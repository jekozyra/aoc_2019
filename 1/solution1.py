def read_input():
    with open('input') as input_file:
        return list(map(int, input_file.readlines()))

'''
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel
required for a module, take its mass, divide by three, round down, and subtract 2.
'''
def compute_fuel_for_module(module_mass):
    mass_over_3 = int(module_mass // 3)
    return mass_over_3 - 2


def main():
    module_masses = read_input()
    print('module masses')
    print(module_masses)
    module_fuels = list(map(compute_fuel_for_module, module_masses))
    print('module fuels')
    print(module_fuels)
    total_fuel = sum(module_fuels)
    print('total fuel: {}'.format(total_fuel))


if __name__== "__main__":
  main()
