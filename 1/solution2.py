import copy

def read_input():
    with open('input') as input_file:
        return list(map(int, input_file.readlines()))

'''
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel
required for a module, take its mass, divide by three, round down, and subtract 2.
'''
def compute_fuel_required(mass):
    mass_over_3 = int(mass // 3)
    if mass_over_3 < 3: return 0

    return mass_over_3 - 2


def compute_total_fuel_required(mass):
    total_fuel_required = compute_fuel_required(mass)
    extra_fuel_required = copy.deepcopy(total_fuel_required)
    while extra_fuel_required > 0:
        extra_fuel_required = compute_fuel_required(extra_fuel_required)
        total_fuel_required += extra_fuel_required

    return total_fuel_required


def main():
    module_masses = read_input()
    print('module masses')
    print(module_masses)
    module_fuels = list(map(compute_total_fuel_required, module_masses))
    print('module fuels')
    print(module_fuels)
    total_fuel = sum(module_fuels)
    print('total fuel: {}'.format(total_fuel))


if __name__== "__main__":
  main()
