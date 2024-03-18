import math

def main():
    r = float(input("Nhập bán kính của hình tròn : "))

    P = 2 * math.pi * r
    S = math.pi * r ** 2

    print(f"Chu vi của hình tròn là : {P}")
    print(f"Diện tích của hình tròn là : {S}")

if __name__ == "__main__":
    main()

