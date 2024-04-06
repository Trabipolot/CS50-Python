def main():
    m = int(input("Please enter mass in kg: "))
    e = calculate_energy(m)
    print(f"{e} Joules")


def calculate_energy(m):
    c = 300000000  # speed of light in m/s
    e = m * c**2
    return e


if __name__ == "__main__":
    main()
