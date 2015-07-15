'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        '''
        Constructor of this class creates two empty lists, one that stores the 
        numbers on the board, and the other contains tuples of previous moves
        
        Arguments:        None
        
        Return value:     None
        '''
        self.board = []
        self.moves = []

    def load(self, filename):
        '''
        Fills the board with the numbers in the filename
        
        Arguments:        filename: name of file containing all the numbers
        
        Return value:     None
        '''
        self.moves = []
        f = open(filename)
        for line in f:
            sm_lst = []
            for i in range(9):
                sm_lst.append(int(line[i]))
            self.board.append(sm_lst)
        f.close()

    def save(self, filename):
        '''
        Saves the current state of the Sudoku board in a file
        
        Arguments:        filename: name of file to save to
        
        Return value:     None
        '''
        f = open(filename, 'w')
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                f.write(str(self.board[i][j]))
            f.write('\n')
        f.close()
        
        

    def show(self):
        '''Pretty-print the current board representation.'''
        print
        print '   1 2 3 4 5 6 7 8 9 '
        for i in range(9):
            if i % 3 == 0:
                print '  +-----+-----+-----+'
            sys.stdout.write('%d |' % (i + 1))
            for j in range(9):
                if self.board[i][j] == 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('%d' % self.board[i][j])
                if j % 3 != 2 :
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('|')
            print 
        print '  +-----+-----+-----+'
        print

    def move(self, row, col, val):
        '''
        Performs the operation of placing a value on the board. Otherwise raises
        various forms of error for different types of mistakes made in the 
        command.
        
        Arguments:        row: row number (1-9)
                          col: column number (1-9)
                          val: value to be inserted on the board (1-9)
        
        Return value:     None
        '''
        if row not in range(1, 10):
            raise SudokuMoveError('Please enter a valid range for the row')
        if col not in range(1, 10):
            raise SudokuMoveError('Please enter a valid range for the column')
        if val not in range(1, 10):
            raise SudokuMoveError('Please enter a valid range for the value')
        if self.board[row-1][col-1] != 0:
            raise SudokuMoveError('This space is already occupied. Try again')
        r = ((row-1)/3) * 3
        c = ((col-1)/3) * 3
        for i in range(r, r+3):
            for j in range(c, c+3):
                if val == self.board[i][j]:
                    found_box = True
                    raise SudokuMoveError('box conflict; please try again')
            found_box = False
        for i in range(9):
            if val == self.board[i][col-1]:
                found_col = True
                raise SudokuMoveError('column conflict; please try again')
            found_col = False
        if val in self.board[row-1]:
            found_row = True
            raise SudokuMoveError('row conflict; please try again')
        else:
            found_row = False
        if not found_row and not found_box and not found_col:
            self.board[row-1][col-1] = val
        self.moves.append((row-1, col-1, val-1))
        
            

    def undo(self):
        '''
        Undos the previous move operation
        
        Arguments:         None
        
        Return value:      None
        '''
        r, c, v = self.moves.pop()
        self.board[r][c] = 0
        print 'Undoing last move...'

    def solve(self):
        '''
        Asks the user for a command in an infinite loop until the 'q' quit 
        command is entered. 'u' calls the undo function, 's <filename>' saves 
        the current numbers on the board in the file <filename> by calling the 
        save function, and integer commands calls the move function. Else prints
        an error message.
        
        Arguments:          None
        
        Return value:       None
        '''
        while True:
            try:
                cmd = raw_input('Please enter a command: ')
                if cmd == 'q':
                    return
                elif cmd == 'u':
                    self.undo()
                elif cmd[0] == 's':
                    fil = cmd.split()[1]
                    self.save(fil)
                elif cmd[0] in '0123456789' and cmd[1] in '0123456789' and \
                     cmd[2] in '0123456789':
                    self.move(int(cmd[0]), int(cmd[1]), int(cmd[2]))
                else:
                    raise SudokuCommandError('%s is a bad command' % cmd) 
            except SudokuCommandError, e:
                print e
                print 'Please enter a valid command'
            except Exception, e:
                print e
            self.show()
        

if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = raw_input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError, e:
            print e
    s.show()
    s.solve()

