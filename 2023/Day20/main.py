from collections import defaultdict
from math import prod

module_connections = dict()
flip_states = defaultdict(int)
conjunction_states = defaultdict(dict)

for line in open('input.txt'):
    signal_type, _, *dependent_signals = line.replace(',', '').split()
    type_modifier, signal_type = (signal_type[0], signal_type[1:]) if signal_type[0] in '%&' else ('', signal_type)

    module_connections[signal_type] = type_modifier, dependent_signals

    for dependent_signal in dependent_signals:
        conjunction_states[dependent_signal][signal_type] = 0
        if dependent_signal == 'rx': rx_signal_type = signal_type

rx_input_states = {module: 0 for module in conjunction_states[rx_signal_type]}

total_presses = 0
count_pulses = [0, 0]

while True:
    if total_presses == 1000:
        print(prod(count_pulses))
    total_presses += 1

    if all(rx_input_states.values()):
        print(prod(rx_input_states.values()))
        break

    process_queue = [(None, 'broadcaster', 0)]
    while process_queue:
        source_module, current_module, input_pulse = process_queue.pop(0)
        count_pulses[input_pulse] += 1

        if current_module not in module_connections: continue
        modifier_type, next_modules = module_connections[current_module]

        match modifier_type, input_pulse:
            case '', _:
                output_pulse = input_pulse
            case '%', 0:
                output_pulse = flip_states[current_module] = not flip_states[current_module]
            case '&', _:
                conjunction_states[current_module][source_module] = input_pulse
                output_pulse = not all(conjunction_states[current_module].values())

                if 'rx' in next_modules:
                    for key, value in conjunction_states[current_module].items():
                        if value: rx_input_states[key] = total_presses
            case _,_: continue

        for next_module in next_modules:
            process_queue.append((current_module, next_module, output_pulse))
