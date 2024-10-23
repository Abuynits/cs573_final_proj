import re
def generate_variable_map(hard_vars, ds_vars, ds_desc):
    variable_map = {}
    num_vars = len(ds_vars)
    for var_idx in range(num_vars):
        var_name = ds_vars[var_idx]
        if var_name in hard_vars:
            continue
        variable_map[var_name] = {}
        # need to split the description by '-'
        ds_desc[var_idx] = ds_desc[var_idx].replace('–', '-')
        # description = ds_desc[var_idx].split('-')
        description = re.split(r'(?<=\d) - ', ds_desc[var_idx])
        current_key = int(description[0].strip())
        for i, key_value_pair in enumerate(description[1:]):
            # will have the value
            if i < len(description[1:]) - 1:
                current_value = " ".join(key_value_pair.split()[:-1])
                next_key = int(key_value_pair.split()[-1].strip())
            else:
                current_value = key_value_pair.strip()
                next_key = None
            # print(f"({current_key}, {current_value})")
            variable_map[var_name][current_key] = current_value
            current_key = next_key
    return variable_map