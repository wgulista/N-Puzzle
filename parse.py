import argparse

class Parser(argparse.HelpFormatter):
	def get_puzzle(filename, size):
		pass

	def puzzle_check(puzzle):
		pass

	def arguments():
		parser = argparse.ArgumentParser(formatter_class=Parser)
		parser.add_argument("-f", "--filename", type=str, help="Filename", default=None)
		parser.add_argument("-s", "--size", choices=[3, 4], default=3, type=int)
		args = parser.parse_args();
		return args;
