generate_range = lambda min, max, step: list(range(min, max, step))

def generate_range(min, max, step):
    result_list = []
    while min < max:
        result_list.append(min)
        min += step
    return result_list
  
