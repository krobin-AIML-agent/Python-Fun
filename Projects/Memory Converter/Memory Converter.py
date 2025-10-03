# %% [markdown]
# **Memory Converter Project**

# %%
def memory_converter(value: float, unit: str):
    # Note: b = bit, B = byte
    units = {
        "b": 1/8,         # bit = smallest, 1 bit = 1/8 of a byte
        "B": 1,           # byte
        "KB": 1024,       # kilobyte
        "MB": 1024**2,    # megabyte
        "GB": 1024**3,    # gigabyte
        "TB": 1024**4     # terabyte (optional extension)
    }

    unit = unit.upper() if unit != "b" else unit  # keep lowercase 'b' for bits

    if unit not in units:
        raise ValueError(f" Unknown unit '{unit}'. Valid units: {', '.join(units)}")

    # Convert everything to bytes first
    bytes_value = value * units[unit]

    results = {}
    for k, v in units.items():
        results[k] = round(bytes_value / v, 2)

    return results

print(memory_converter(1, "B"))   # from 1 Byte
print(memory_converter(8, "b"))   # from 8 bits
print(memory_converter(2, "GB"))  # from 2 Gigabytes


