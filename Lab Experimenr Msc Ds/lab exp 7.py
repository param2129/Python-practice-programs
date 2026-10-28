#Program to compute the value of cos and sin using cosine/sine series, using functions
import math
def sine(x, terms=15):
    """sin(x), x in radians."""
    result = term = x
    for n in range(1, terms):
        term *= -x * x / ((2 * n) * (2 * n + 1))
        result += term
    return result


def cosine(x, terms=15):
    """cos(x), x in radians."""
    result = term = 1
    for n in range(1, terms):
        term *= -x * x / ((2 * n) * (2 * n - 1))
        result += term
    return result


angle_deg = float(input("Enter angle in degrees: "))
terms = int(input("Enter number of terms (default 15): ") or 15)

angle_rad = math.radians(angle_deg)

sin_val = sine(angle_rad, terms)
cos_val = cosine(angle_rad, terms)

print(f"\nSeries -> sin({angle_deg}) = {sin_val:.6f}, cos({angle_deg}) = {cos_val:.6f}")
print(f"math   -> sin({angle_deg}) = {math.sin(angle_rad):.6f}, "
      f"cos({angle_deg}) = {math.cos(angle_rad):.6f}")