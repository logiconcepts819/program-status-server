import re

def print_help(progname):
    print("Usage: %s green_led_gpio_number,red_led_gpio_number [...]"%(
        progname))

def parse_command_line(argv):
    leds = []
    
    first = argv[0]
    rest = argv[1:]
    
    for arg in rest:
        if arg == '-h' or arg == '--help':
            print_help(first)
            return None
        
        matches = re.search( \
          '^\\s*([^\\s,]+)\\s*,\\s*([^\\s,\\}]+)(\\s*,\\s*([^\\s\\}]+))?\\s*$',
          arg)
        if not matches:
            print("Invalid argument '%s'"%(arg))
            print_help(first)
            return None
        
        try:
            green_led_gpio_num = int(matches.group(1))
            red_led_gpio_num = int(matches.group(2))
            button_gpio_num = None
            if matches.group(4) is not None:
                button_gpio_num = int(matches.group(4))

        except ValueError:
            print("Expecting integers in argument '%s'"%(arg))
            print_help(first)
            return None

        if button_gpio_num is None:        
            leds.append((green_led_gpio_num, red_led_gpio_num))
        else:
            leds.append((green_led_gpio_num, red_led_gpio_num, button_gpio_num))
    
    if len(leds) == 0:
        print("No command line arguments specified")
        print_help(first)
        return None
    
    return leds
