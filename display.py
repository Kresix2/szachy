import pygame as py

if __name__ == '__main__':
    import szachy_main as szy 
    board = szy.board()
    py.init()
    window_size = (800,800)
    window = py.display.set_mode(window_size)
    surface = py.Surface(window_size)
    moves =0b1
    moves_surface = py.Surface(window_size, py.SRCALPHA)
    while True:
        moves_surface.fill((0,0,0,0))
        for i in range(8):
            for j in range(8): 
                square = py.Rect((j*window_size[0]/8,i*window_size[1]/8,window_size[0]/8,window_size[1]/8))     
                         
                if (j+i)%2== 0:
                    color = (238,238,210)
                else:
                    color = (118,150,86)
                py.draw.rect(surface,color,square)
                
                


                
                piece = board.find_piece(i*8+j)
                if piece != None:
                        image = py.image.load('pieces_img/'+piece+'.png').convert_alpha()
                        image = py.transform.scale(image,(window_size[0]/8,window_size[1]/8))
                        surface.blit(image,(j*window_size[0]/8,i*window_size[1]/8))
                if 0b1<<(i*8+j)& moves and 0b1<<(i*8+j)&board.occupied :
                    py.draw.circle(moves_surface,(255,0,0,100),(j*window_size[0]/8+window_size[0]/16,i*window_size[1]/8+window_size[1]/16),15)
                elif 0b1<<(i*8+j)& moves:
                    py.draw.circle(moves_surface,(100,100,100,100),(j*window_size[0]/8+window_size[0]/16,i*window_size[1]/8+window_size[1]/16),15)
        
        window.blit(surface,(0,0))
        window.blit(moves_surface,(0,0))
        py.display.flip()
        for event in py.event.get():
            if event.type == py.MOUSEBUTTONUP:
                mouse_pos = py.mouse.get_pos()
                mouse_pos = (mouse_pos[0]//(window_size[0]/8),mouse_pos[1]//(window_size[1]/8))
                chosen_piece = int(mouse_pos[1]*8+mouse_pos[0])
                piece = board.find_piece(chosen_piece)
                if piece:
                    moves = board.possible_moves_compiled(chosen_piece,piece)
                
            if event.type == py.QUIT:
                py.quit()