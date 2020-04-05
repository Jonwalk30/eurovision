import argparse

def grab_seed_as_arg():

    parser = argparse.ArgumentParser(description='Randomly assign players countries.')

    parser.add_argument('integers', metavar='seed', type=int, nargs='+',
                       help='The seed passed to the random number generator.')

    args = parser.parse_args()
    seed = args.integers[0]
    
    return seed
