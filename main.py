import sys
from parse import Parser
from solve_puzzle import Solver

if __name__ == '__main__':
	args = Parser.arguments();
	puzzle = Parser.get_puzzle(args.filename, args.size)
	if not Parser.puzzle_check(puzzle):
		sys.exit("Error: This puzzle can not be solve")
	solution = Solver.solve_puzzle(puzzle)
	Solver.solution(puzzle, solution)
