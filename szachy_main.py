import display
class board:
    def __init__(self):
        #//////////////////////
        #   board and details
        #//////////////////////
        self.bitboards = {
            "Bpawn":   0b00000000_11111111_00000000_00000000_00000000_00000000_00000000_00000000,
            "Bknight": 0b01000010_00000000_00000000_00000000_00000000_00000000_00000000_00000000,
            "Brook":   0b10000001_00000000_00000000_00000000_00000000_00000000_00000000_00000000,
            "Bbishop": 0b00100100_00000000_00000000_00000000_00000000_00000000_00000000_00000000,
            "Bqueen":  0b00010000_00000000_00000000_00000000_00010000_00000000_00000000_00000000,
            "Bking":   0b00001000_00000000_00000000_00000000_00000000_00000000_00000000_00000000,
            "Wpawn":   0b0000000000000000000000000000000000000000000000001111111100000000,
            "Wknight": 0b0000000000000000000000000000000000000000000000000000000001000010,
            "Wrook":   0b0000000000000000000000000000000000000000000000000000000010000001,
            "Wbishop": 0b0000000000000000000000000000000000000000000000000000000000100100,
            "Wqueen":  0b0000000000000000000000000000000000000000000000000000000000010000,
            "Wking":   0b0000000000000000000000000000000000000000000000000000000000001000,
        }
        self.moves = {
             'Wpawn':  [512, 1280, 2560, 5120, 10240, 20480, 40960, 16384, 131072, 327680, 655360, 1310720, 2621440, 5242880, 10485760, 4194304, 33554432, 83886080, 167772160, 335544320, 671088640, 1342177280, 2684354560, 1073741824, 8589934592, 21474836480, 42949672960, 85899345920, 171798691840, 343597383680, 687194767360, 274877906944, 2199023255552, 5497558138880, 10995116277760, 21990232555520, 43980465111040, 87960930222080, 175921860444160, 70368744177664, 562949953421312, 1407374883553280, 2814749767106560, 5629499534213120, 11258999068426240, 22517998136852480, 45035996273704960, 18014398509481984, 144115188075855872, 360287970189639680, 720575940379279360, 1441151880758558720, 2882303761517117440, 5764607523034234880, 11529215046068469760, 4611686018427387904, 0, 0, 0, 0, 0, 0, 0, 0]
            ,'Bpawn':  [0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 10, 20, 40, 80, 160, 64, 512, 1280, 2560, 5120, 10240, 20480, 40960, 16384, 131072, 327680, 655360, 1310720, 2621440, 5242880, 10485760, 4194304, 33554432, 83886080, 167772160, 335544320, 671088640, 1342177280, 2684354560, 1073741824, 8589934592, 21474836480, 42949672960, 85899345920, 171798691840, 343597383680, 687194767360, 274877906944, 2199023255552, 5497558138880, 10995116277760, 21990232555520, 43980465111040, 87960930222080, 175921860444160, 70368744177664, 562949953421312, 1407374883553280, 2814749767106560, 5629499534213120, 11258999068426240, 22517998136852480, 45035996273704960, 18014398509481984]
            ,'knight': [132096, 329728, 659712, 1319424, 2638848, 5277696, 10489856, 4202496, 33816580, 84410376, 168886289, 337772578, 675545156, 1351090312, 2685403152, 1075839008, 8657044482, 21609056261, 43234889994, 86469779988, 172939559976, 345879119952, 687463207072, 275414786112, 2216203387392, 5531918402816, 11068131838464, 22136263676928, 44272527353856, 88545054707712, 175990581010432, 70506185244672, 567348067172352, 1416171111120896, 2833441750646784, 5666883501293568, 11333767002587136, 22667534005174272, 45053588738670592, 18049583422636032, 145241105196122112, 362539804446949376, 725361088165576704, 1450722176331153408, 2901444352662306816, 5802888705324613632, 11533718717099671552, 4620693356194824192, 288234782788157440, 576469569871282176, 1224997833292120064, 2449995666584240128, 4899991333168480256, 9799982666336960512, 1152939783987658752, 2305878468463689728, 1128098930098176, 2257297371824128, 4796069720358912, 9592139440717824, 19184278881435648, 38368557762871296, 4679521487814656, 9077567998918656]
            ,'king':   [770, 1797, 3594, 7188, 14376, 28752, 57504, 49216, 197123, 460039, 920078, 1840156, 3680312, 7360624, 14721248, 12599488, 50463488, 117769984, 235539968, 471079936, 942159872, 1884319744, 3768639488, 3225468928, 12918652928, 30149115904, 60298231808, 120596463616, 241192927232, 482385854464, 964771708928, 825720045568, 3307175149568, 7718173671424, 15436347342848, 30872694685696, 61745389371392, 123490778742784, 246981557485568, 211384331665408, 846636838289408, 1975852459884544, 3951704919769088, 7903409839538176, 15806819679076352, 31613639358152704, 63227278716305408, 54114388906344448, 216739030602088448, 505818229730443264, 1011636459460886528, 2023272918921773056, 4046545837843546112, 8093091675687092224, 16186183351374184448, 13853283560024178688, 144959613005987840, 362258295026614272, 724516590053228544, 1449033180106457088, 2898066360212914176, 5796132720425828352, 11592265440851656704, 4665729213955833856]
        }
        self.masks = {
            'cross_ver' :    [72340172838076673, 144680345676153346, 289360691352306692, 578721382704613384, 1157442765409226768, 2314885530818453536, 4629771061636907072, 9259542123273814144]
            ,'cross_hor':    [255, 65280, 16711680, 4278190080, 1095216660480, 280375465082880, 71776119061217280, 18374686479671623680]
            ,'diagonal':     [72057594037927936, 144396663052566528, 288794425616760832, 577588855528488960, 1155177711073755136, 2310355422147575808, 4620710844295151872, 9241421688590303745, 36099303471055874, 141012904183812, 550831656968, 2151686160, 8405024, 32832, 128]
            ,'anti_diagonal':[1, 258, 66052, 16909320, 4328785936, 1108169199648, 283691315109952, 72624976668147840, 145249953336295424, 290499906672525312, 580999813328273408, 1161999622361579520, 2323998145211531264, 4647714815446351872, 9223372036854775808]
        }
        #what ocupies each of the sides, W => white, B => black
        self.occupied_sides = {
            'B':sum([bitboard  for name,bitboard in self.bitboards.items() if name.startswith('B')])
            ,'W':sum([bitboard  for name,bitboard in self.bitboards.items() if name.startswith('W')])
            }

        self.occupied =  sum(self.occupied_sides.values())
        #/////////////////////////////
        #   move generation details
        #////////////////////////////
        self.inside = 0b1111111111111111111111111111111111111111111111111111111111111111
        self.A_file = 0b0111111101111111011111110111111101111111011111110111111101111111
        self.H_file = 0b1111111011111110111111101111111011111110111111101111111011111110
        self.AB_file = 0b0011111100111111001111110011111100111111001111110011111100111111
        self.GH_file = 0b1111110011111100111111001111110011111100111111001111110011111100
    
    @staticmethod
    def get_columns(start,end):
        lst = []
        for i in range(8):
            if i<end and i>start:
                lst.append('0')
            else:
                lst.append('1')
        return int(''.join(lst*8),2)
    
    
    @staticmethod
    def format_bin(binaries):
        return_bin = []
        if type(binaries) != list:
            return '{:064b}'.format(binaries)
        for binary in binaries:
            return_bin.append('{:064b}'.format(binary))
        return return_bin
    
    def log_chessboard(self):
        printout = ['.']*64
        white_names = ['♟','♞','♜','♝','♛','♚']
        whites = [bitboard  for name,bitboard in self.bitboards.items() if name.startswith('W')]
        whites = self.format_bin(whites)
        black_names = ['♙','♘','♖','♗','♕','♔']
        blacks = [bitboard  for name,bitboard in self.bitboards.items() if name.startswith('B')]
        blacks = self.format_bin(blacks)
        for i,piece in enumerate(whites):
            for j in range(64):
                if piece[j] == '1':
                    printout[j] = white_names[i]

        for i,piece in enumerate(blacks):
            for j in range(64):
                if piece[j] == '1':
                    printout[j] = black_names[i]
        print('    A B C D E F G H')
        for i in range(8):
            print(8-i,'|',' '.join(printout[i*8:i*8+8]))
    
    def possible_moves_cross(self,slider):
        column = self.check_bits(slider)%8
        row = self.check_bits(slider)//8
        mask_hor = self.masks['cross_hor'][row]
        mask_ver = self.masks['cross_ver'][column]
        return self.possible_moves_slider(mask_hor,slider)|self.possible_moves_slider(mask_ver,slider)&self.inside
    
    def possible_moves_diagonals(self,slider):
        slider_index = self.check_bits(slider)
        mask_diag = self.masks['diagonal'][slider_index%8+7-slider_index//8]
        mask_antidiag = self.masks['anti_diagonal'][slider_index%8+slider_index//8]
        return self.possible_moves_slider(mask_diag,slider)|self.possible_moves_slider(mask_antidiag,slider)       
    
    def possible_moves_slider(self,mask,slider):
        def reverse_bitboard(b):
            #from chess code exchanhge https://chess.stackexchange.com/questions/37309/move-generation-for-sliding-pieces-and-hyperbola-quintessence
            b = (b & 0x5555555555555555) << 1 | ((b >> 1) & 0x5555555555555555)
            b = (b & 0x3333333333333333) << 2 | ((b >> 2) & 0x3333333333333333)
            b = (b & 0x0f0f0f0f0f0f0f0f) << 4 | ((b >> 4) & 0x0f0f0f0f0f0f0f0f)
            b = (b & 0x00ff00ff00ff00ff) << 8 | ((b >> 8) & 0x00ff00ff00ff00ff)

            return (b << 48) | ((b & 0xffff0000) << 16) | ((b >> 16) & 0xffff0000) | (b >> 48)
        # assure there is only one piece
        assert slider&(slider-1) == 0

        
        #cross_attack_hor = (self.occupied&mask)^((self.occupied&mask)-2*slider)
        #masked occupied
        m_o = self.occupied&mask
        #reverse_bitboard mask occupied
        m_oR = reverse_bitboard(self.occupied&mask)

        #slider pos
        s = slider
        #reverse_bitboardd slider pos
        sR = reverse_bitboard(slider)

        cross_attack = (m_o-2*s)^reverse_bitboard(m_oR-2*sR)
        cross_attack &= mask
         
        
        return cross_attack&~slider

    
    def generate_mask_cross(self):
        #generates masks needed for rook and queen sliding movement generation

        cross_mask_vertical = []
        cross_mask_horizontal = []
        curr = 0b1
        curr2 =0b1

        for i in range(8):


            vertical = curr
            for j in range(1,8):
                vertical |= (curr<<j*8|curr>>j*8)&self.inside
            
            horizontal = curr2
            for j in range(1,8):
                horizontal = (horizontal|curr2<<j&self.get_columns(7-j,8)|curr2>>j&self.get_columns(-1,j))&self.inside


            cross_mask_vertical.append(vertical)
            cross_mask_horizontal.append(horizontal)
            curr = curr<<1
            curr2 = curr2<<8
            self.log_bitboard(vertical)
            self.log_bitboard(horizontal)
        print(cross_mask_horizontal)
        print(cross_mask_vertical)
    
    def generate_mask_diagonal(self):
        #generates masks needed for bishop and queen sliding movement generation
        #\
        # \
        #  \
        #   \
        diagonal_mask = []
        #   /
        #  /
        # /
        #/
        anti_diagonal_mask = []
        curr = 0x100000000000000
        curr2 =0b1

        for i in range(7):


            diagonal = curr
            for j in range(1,8):
                diagonal |= curr<<j*9&self.get_columns(7-j,8)|curr>>j*9&self.get_columns(-1,j)
            diagonal &= self.inside


            anti_diagonal= curr2
            for j in range(1,8):
                anti_diagonal |= curr2<<j*7&self.get_columns(-1,j)|curr2>>j*7&self.get_columns(7-j,8)
            anti_diagonal &= self.inside

            diagonal_mask.append(diagonal)
            anti_diagonal_mask.append(anti_diagonal)
            curr = curr>>8
            curr2 = curr2<<8
            self.log_bitboard(diagonal)
            self.log_bitboard(anti_diagonal)

        
        curr = 0b1
        curr2 = 0x100000000000000
        for i in range(8):


            diagonal = curr
            for j in range(1,8):
                diagonal |= curr<<j*9&self.get_columns(7-j,8)|curr>>j*9&self.get_columns(-1,j)
            diagonal &= self.inside

            anti_diagonal= curr2
            for j in range(1,8):
                anti_diagonal |= curr2<<j*7&self.get_columns(-1,j)|curr2>>j*7&self.get_columns(7-j,8)
            anti_diagonal &= self.inside

            diagonal_mask.append(diagonal)
            anti_diagonal_mask.append(anti_diagonal)


            curr = curr<<1
            curr2 = curr2<<1

            self.log_bitboard(diagonal)
            self.log_bitboard(anti_diagonal)
        print(diagonal_mask)
        print(anti_diagonal_mask)
    
    def generate_moves_pawn(self):
        A_file = 0b0111111101111111011111110111111101111111011111110111111101111111
        H_file = 0b1111111011111110111111101111111011111110111111101111111011111110
        inside = 0b1111111111111111111111111111111111111111111111111111111111111111
        w_pawn_lookup = []
        b_pawn_lookup = []
        curr = 0b1
        
        
        for i in range(64):
            
            temp = (curr<<7&A_file|curr<<9&H_file)&inside
            w_pawn_lookup.append(temp)
            curr = curr<<1
        print(w_pawn_lookup)
        curr = 0b1
        for i in range(64):
            
            temp = (curr>>7&H_file|curr>>9&A_file)&inside
            b_pawn_lookup.append(temp)
            curr = curr<<1
        print(b_pawn_lookup)
    
    def log_moves(self,name):
        for board in self.moves[name]:
            self.log_bitboard(board)
    
    def generate_moves_knight(self):
        A_file = 0b0111111101111111011111110111111101111111011111110111111101111111
        H_file = 0b1111111011111110111111101111111011111110111111101111111011111110
        inside = 0b1111111111111111111111111111111111111111111111111111111111111111
        ext_A_file = 0b0011111100111111001111110011111100111111001111110011111100111111
        ext_H_file = 0b1111110011111100111111001111110011111100111111001111110011111100
        knight_lookup = []
        curr = 0b1


        for i in range(64):
            vertical = curr<<17&H_file|curr<<15&A_file|curr>>17&A_file|curr>>15&H_file
            horizontal = curr<<10&ext_H_file|curr<<6&ext_A_file|curr>>10&ext_A_file|curr>>6&ext_H_file
            temp = (vertical|horizontal)&inside
            knight_lookup.append(temp)
            curr = curr<<1
        print(knight_lookup)
    
    def generate_moves_king(self):
        A_file = 0x7f7f7f7f7f7f7f7f
        H_file = 0b1111111011111110111111101111111011111110111111101111111011111110
        inside = 0b1111111111111111111111111111111111111111111111111111111111111111
        king_lookup = []
        curr = 0b1
        for i in range(64):
            left = (curr<<9|curr<<1|curr>>7)&H_file
            right= (curr<<7|curr>>1|curr>>9)&A_file
            vertical = curr<<8|curr>>8
            temp = (left|right|vertical)&inside
            king_lookup.append(temp)
            curr = curr << 1 
            self.log_bitboard(temp)
    

    def move(self,piece,destination,piece_name):
        assert piece&(piece-1) == 0 and destination&(destination-1) == 0, 'more than one piece found'

        assert self.bitboards[piece_name]&piece != 0, 'no piece found at chosen location'
        #an attack
        if self.occupied&destination:
            for name,bitboard in self.bitboards.items():
                if bitboard&destination !=0:
                    self.bitboards[name] &= destination

        self.bitboards[piece_name] &= ~piece
        self.bitboards[piece_name] |= destination
    
    def possible_moves_compiled(self,piece_index,piece_name):

        piece = 0b1<<piece_index
        base_move = 0XFFFFFFFFFFFFFFFF
        side = piece_name[:1]
        piece_name = piece_name[1:]

        match piece_name:
            case 'pawn':           
                base_move = self.moves[side+'pawn'][piece_index]
                
            case 'knight':
                base_move = self.moves['knight'][piece_index]
            
            case 'queen':
                base_move = self.possible_moves_cross(piece)|self.possible_moves_diagonals(piece)
            case 'bishop':
                base_move = self.possible_moves_cross(piece)

            case 'rook':
                base_move = self.possible_moves_cross(piece)

            case 'king':
                base_move = self.moves['king'][piece_index]
            case _:
                raise SystemExit('Program Exited: No piece found under the name \''+ side + piece_name+'\'')
            
        base_move &= self.occupied_sides[side]^self.inside
        self.log_bitboard(base_move,piece)
        return base_move
            


        
    
    @staticmethod
    def check_bits(binary):
        for i in range(64):
            if binary>>i == 1:
                return i 
    @staticmethod
    def get_columns(start,end):
        lst = []
        for i in range(8):
            if i<end and i>start:
                lst.append('0')
            else:
                lst.append('1')
        return int(''.join(lst*8),2)
    
    @staticmethod
    def log_bitboard(*boards):
        print(boards)
        for board in boards:
            print('board',board)
            assert board & ~0xFFFFFFFFFFFFFFFF == 0
        symbols = 'XOYZ'
        square = 0x10000000000000000
        for rank in range(8):
            line = ""
            for file in range(8):
                square >>= 1
                square_symbol = "."
                for i,board in enumerate(boards):
                    if board & square:
                        square_symbol = symbols[i]

                line += square_symbol+' '
            print(line)
        print('')
    
    @staticmethod
    def format_bin(binaries):
        return_bin = []
        if type(binaries) != list:
            return '{:064b}'.format(binaries)
        for binary in binaries:
            return_bin.append('{:064b}'.format(binary))
        return return_bin     
    def find_piece(self,piece_index):

        for name,bitboard in self.bitboards.items():
            if bitboard&(1<<piece_index) !=0:
                return name
        



            







                

        
b = board()
print(b.find_piece(1))
#b.possible_moves_compiled(0b00000000_00000000_00000000_00000000_00010000_00000000_00000000_00000000,'Wqueen')
#b.possible_moves_compiled(0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00001000,'Brook')