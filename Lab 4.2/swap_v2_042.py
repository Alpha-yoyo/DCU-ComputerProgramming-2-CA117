def swap_unique_keys_values(d):
   unique_keys = [k for k, v in d.items() if list(d.values()).count(v) == 1]
   unique_values = [d[v] for v in unique_keys]
   new_dict = dict(map(reversed, zip(unique_keys, unique_values)))
   return new_dict
