import pygame
import math
import logic
import random
import os
import json
import pygame.mixer

pygame.init()
pygame.mixer.init()

class Hexagon:
    def __init__(self, x, y, numero, bordure_color, size = 30, color = (220, 220, 220), grid_size: int = 11):
        """Initialise une instance de la classe Hexagon.

        Args:
            x (int): Position en abscisse de l'hexagone.
            y (int): Position en ordonnée de l'hexagone.
            numero (int): Numéro de l'hexagone.
            bordure_color (tuple): Couleur de la bordure de l'hexagone.
            size (int, optionnel): Taille de l'hexagone. Par défaut, 30.
            color (tuple, optionnel): Couleur de remplissage de l'hexagone. Par défaut, (220, 220, 220).
            grid_size (int, optionnel): Taille de la grille. Par défaut, 11.
        """
        self.x = x
        self.y = y
        self.numero = numero
        self.bordure_color = bordure_color
        self.size = size  
        self.color = color
        self.grid_size = grid_size
        if self.grid_size == 9 or self.grid_size == 11:
            self.size = 30
        elif self.grid_size == 13:
            self.size = 25
        elif self.grid_size == 19:
            self.size = 18


    def draw(self, surface):
        """Dessine l'hexagone sur la surface spécifiée.

        Args:
            surface (pygame.Surface): Surface sur laquelle dessiner l'hexagone.
        """
        points = []
        for angle in range(30, 391, 60):
            x_point = self.x + self.size * math.cos(math.radians(angle))
            y_point = self.y + self.size * math.sin(math.radians(angle))
            points.append((x_point, y_point))
        pygame.draw.polygon(surface, self.color, points)
        pygame.draw.polygon(surface, self.bordure_color, points, 2)

        # Dessine les bordures en fonction de la taille de la grille
        if self.grid_size == 11:
            if 0 < self.numero < 12:
                pygame.draw.line(surface, (235, 0, 0), (self.x - 26, self.y - 22), (self.x, self.y - 37), 5)
                pygame.draw.line(surface, (235, 0, 0), (self.x + 26, self.y - 22), (self.x, self.y - 37), 5)
            if 110 < self.numero < 122:
                pygame.draw.line(surface, (235, 0, 0), (self.x - 26, self.y + 22), (self.x, self.y + 37), 5)
                pygame.draw.line(surface, (235, 0, 0), (self.x + 26, self.y + 22), (self.x, self.y + 37), 5)
            if self.numero % 11 == 1:
                if self.numero != 111:
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 31, self.y - 13), (self.x - 31, self.y + 20), 5)
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 31, self.y + 20), (self.x - 5, self.y + 34), 5)
                else:
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 30, self.y - 11), (self.x - 30, self.y + 19), 5)
            if self.numero % 11 == 0:
                if self.numero != 111 and self.numero != 11:
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 5, self.y - 32), (self.x + 32, self.y - 16), 5)
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 32, self.y - 16), (self.x + 32, self.y + 16), 5)
                else:
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 32, self.y - 16), (self.x + 32, self.y + 16), 5)

        elif self.grid_size == 9:
            if 0 < self.numero < 10:
                pygame.draw.line(surface, (235, 0, 0), (self.x - 26, self.y - 22), (self.x, self.y - 37), 5)
                pygame.draw.line(surface, (235, 0, 0), (self.x + 26, self.y - 22), (self.x, self.y - 37), 5)
            if 72 < self.numero < 83 :
                pygame.draw.line(surface, (235, 0, 0), (self.x - 26, self.y + 22), (self.x, self.y + 37), 5)
                pygame.draw.line(surface, (235, 0, 0), (self.x + 26, self.y + 22), (self.x, self.y + 37), 5)
            if self.numero % 9 == 1:
                if self.numero != 73:
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 31, self.y - 13), (self.x - 31, self.y + 20), 5)
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 31, self.y + 20), (self.x - 5, self.y + 34), 5)
                else:
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 30, self.y - 11), (self.x - 30, self.y + 19), 5)
            if self.numero % 9 == 0:
                if self.numero != 73 and self.numero != 9:
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 5, self.y - 32), (self.x + 32, self.y - 16), 5)
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 32, self.y - 16), (self.x + 32, self.y + 16), 5)
                else:
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 32, self.y - 16), (self.x + 32, self.y + 16), 5)

        elif self.grid_size == 13:
            if 0 < self.numero < 14:
                pygame.draw.line(surface, (235, 0, 0), (self.x - 22, self.y - 22), (self.x, self.y - 34), 5)
                pygame.draw.line(surface, (235, 0, 0), (self.x + 22, self.y - 22), (self.x, self.y - 34), 5)
            if 156 < self.numero < 170:
                pygame.draw.line(surface, (235, 0, 0), (self.x - 22, self.y + 22), (self.x, self.y + 34), 5)
                pygame.draw.line(surface, (235, 0, 0), (self.x + 22, self.y + 22), (self.x, self.y + 34), 5)
            if self.numero % 13 == 1:
                if self.numero != 157:
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 31, self.y - 8), (self.x - 31, self.y + 20), 5)
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 31, self.y + 20), (self.x - 8, self.y + 31), 5)
                else:
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 30, self.y - 7), (self.x - 30, self.y + 19), 5)
            if self.numero % 13 == 0:
                if self.numero != 157 and self.numero != 13:
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 8, self.y - 29), (self.x + 32, self.y - 16), 5)
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 32, self.y - 16), (self.x + 32, self.y + 11), 5)
                else:
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 32, self.y - 16), (self.x + 32, self.y + 10), 5)

        elif self.grid_size == 19:
            if 0 < self.numero < 20:
                pygame.draw.line(surface, (235, 0, 0), (self.x - 17, self.y - 15), (self.x, self.y - 25), 5)
                pygame.draw.line(surface, (235, 0, 0), (self.x + 17, self.y - 15), (self.x, self.y - 25), 5)
            if 342 < self.numero < 362:
                pygame.draw.line(surface, (235, 0, 0), (self.x - 17, self.y + 15), (self.x, self.y + 25), 5)
                pygame.draw.line(surface, (235, 0, 0), (self.x + 17, self.y + 15), (self.x, self.y + 25), 5)
            if self.numero % 19 == 1:
                if self.numero != 343:
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 21, self.y - 7), (self.x - 21, self.y + 12), 5)
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 21, self.y + 12), (self.x - 4, self.y + 22), 5)
                else:
                    pygame.draw.line(surface, (0, 0, 235), (self.x - 21, self.y - 7), (self.x - 21, self.y + 12), 5)
            if self.numero % 19 == 0:
                if self.numero != 343 and self.numero != 19:
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 5, self.y - 22), (self.x + 22, self.y - 11), 5)
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 22, self.y - 12), (self.x + 22, self.y + 8), 5)
                else:
                    pygame.draw.line(surface, (0, 0, 235), (self.x + 22, self.y - 7), (self.x + 22, self.y + 8), 5)


    def contains_point(self, point):
        """Vérifie si le point spécifié est contenu dans l'hexagone.

        Args:
            point (tuple): Coordonnées (x, y) du point à vérifier.

        Returns:
            bool: True si le point est contenu dans l'hexagone, False sinon.
        """
        rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
        return rect.collidepoint(point)


class HexagonGrid:
    def __init__(self, width, height, main_menu, grid_size, turn, game_mode, ia_tree_depth):
        """Initialise une instance de la classe HexagonGrid.

        Args:
            width (int): Largeur de la fenêtre du jeu.
            height (int): Hauteur de la fenêtre du jeu.
            main_menu (MainMenu): Instance du menu principal du jeu.
            grid_size (int): Taille de la grille de jeu.
            turn (int): Joueur actuel (0 pour le joueur bleu, 1 pour le joueur rouge).
            game_mode (str): Mode de jeu (par exemple, "Player vs Player", "Player vs AI", etc.).
            ia_tree_depth (int): Profondeur maximale de l'arbre de recherche pour l'IA.
        """
        self.width = width
        self.height = height
        self.main_menu = main_menu
        self.grid_size = grid_size
        self.turn = turn 
        self.game_mode = game_mode
        self.ia_tree_depth = ia_tree_depth

        # Détermine la taille des hexagones en fonction de la taille de la grille
        if self.grid_size == 9 or self.grid_size == 11:
            self.hex_size = 30
        elif self.grid_size == 13:
            self.hex_size = 25
        elif self.grid_size == 19:
            self.hex_size = 18
        
        # Initialise la fenêtre de jeu et son titre
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Hexagon Grid")

        # Liste des noms des joueurs
        self.nom_joueurs = ["Bleu", "Rouge"]
        # Liste des hexagones sur la grille
        self.hexagons = []
        # Indique si le jeu est en pause ou non
        self.is_paused = False
        # Joueur actuel (0 pour le joueur bleu, 1 pour le joueur rouge)
        self.first_turn = turn 
        # Indique si la partie est gagnée
        self.victory = False
        # Mode de jeu (par exemple, "Player vs Player", "Player vs AI")
        self.setup_hexagons()
        # Profondeur maximale de l'arbre de recherche pour l'IA
        self.logic = logic.Logic(self.grid_size)
              

    def setup_hexagons(self):
        """Initialise les hexagones sur la grille de jeu."""
        # Coordonnées de départ pour placer les hexagones en fonction de la taille de la grille
        x = {9: 135, 11: 55, 13: 57, 19: 32}
        y = {9: 210, 11: 165, 13: 160, 19: 147}
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.hexagons.append(Hexagon(x[self.grid_size] + self.calculate_offset(i, j),
                                             y[self.grid_size] + self.hex_size * 1.5 * i, 
                                             i * self.grid_size + j + 1, 
                                             (70, 70, 70), 
                                             self.hex_size, 
                                             (255, 255, 255), 
                                             self.grid_size))


    def calculate_offset(self, i, j):
        """Calcule le décalage pour positionner correctement un hexagone sur la grille.

        Args:
            i (int): Indice de ligne de l'hexagone.
            j (int): Indice de colonne de l'hexagone.

        Returns:
            float: Décalage en pixels pour positionner l'hexagone.
        """
        if i >= 2:
            return (self.hex_size * math.sqrt(3) * j + self.hex_size * 
                    math.sqrt(3) / 2 + (self.hex_size - 3) * (i - 2) + (self.hex_size / 2) + 10)
        else:
            return self.hex_size * math.sqrt(3) * j + (i % 2) * (self.hex_size * math.sqrt(3) / 2)
        
    def draw_pause_menu(self):
        """Dessine le menu de pause."""
        global save_button, resume_button, main_menu_button

        # Définition des coordonnées pour le menu de pause
        menu_x1 = self.width // 7
        menu_y1 = self.height // 4
        menu_x2 = self.width // 7 * 6
        menu_y2 = self.height // 4 * 3

        # Dessine un fond semi-transparent pour le menu
        transparent_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 100))
        self.screen.blit(transparent_surface, (0, 0))

        # Dessine le cadre du menu de pause
        menu_rect = pygame.Rect(menu_x1, menu_y1, menu_x2 - menu_x1, menu_y2 - menu_y1)
        pygame.draw.rect(self.screen, (220, 220, 220), menu_rect, border_radius=15)
        pygame.draw.rect(self.screen, (70, 70, 70), menu_rect, 2, border_radius=15)
        
        # Affiche le texte "Partie en pause"
        paused_game_text = pygame.font.SysFont(None, 30).render("Partie en pause", True, (70, 70, 70))
        paused_game_text_rect = paused_game_text.get_rect(center=(self.width // 2, self.height // 10 * 3 + 20))
        self.screen.blit(paused_game_text, paused_game_text_rect)
        
        # Définition des coordonnées des boutons et dessin des boutons
        save_button_x1 = self.width // 12 * 4
        save_button_y1 = self.height // 10 * 5
        save_button_x2 = self.width // 12 * 4
        save_button_y2 = self.height // 10

        # Dessine le bouton "Sauvegarder"
        save_button = pygame.draw.rect(
            self.screen, (220, 220, 220), (save_button_x1, save_button_y1, save_button_x2, save_button_y2)
            )
        pygame.draw.rect(self.screen, (70, 70, 70), save_button, 2, border_radius=15)
        save_text = pygame.font.SysFont(None, 30).render("Sauvegarder", True, (70, 70, 70))
        save_button_center = save_button.center
        save_text_center = save_text.get_rect(center=save_button_center)
        self.screen.blit(save_text, save_text_center)

        # Dessine le bouton "Reprendre"
        resume_button = pygame.draw.rect(
            self.screen, (220, 220, 220), (save_button_x1, save_button_y1 - 80, save_button_x2, save_button_y2)
            )
        pygame.draw.rect(self.screen, (70, 70, 70), resume_button, 2, border_radius=15)
        resume_text = pygame.font.SysFont(None, 30).render("Reprendre", True, (70, 70, 70))
        resume_button_center = resume_button.center
        resume_text_center = resume_text.get_rect(center=resume_button_center)
        self.screen.blit(resume_text, resume_text_center)        

        # Dessine le bouton "Retour au menu principal"
        main_menu_button = pygame.draw.rect(
            self.screen, (220, 220, 220), (save_button_x1, save_button_y1 + 80, save_button_x2, save_button_y2)
            )
        pygame.draw.rect(self.screen, (70, 70, 70), main_menu_button, 2, border_radius=15)
        main_menu_text = pygame.font.SysFont(None, 30).render("Retour au menu principal", True, (70, 70, 70))
        main_menu_button_center = main_menu_button.center
        main_menu_text_center = main_menu_text.get_rect(center=main_menu_button_center)
        self.screen.blit(main_menu_text, main_menu_text_center)   


    def draw_victory_menu(self):
        """Dessine le menu de victoire."""
        global play_again_button, main_menu_button

        # Définition des coordonnées pour le menu de victoire
        menu_x1 = self.width // 7
        menu_y1 = self.height // 4
        menu_x2 = self.width // 7 * 6
        menu_y2 = self.height // 4 * 3

        # Dessine un fond semi-transparent pour le menu
        transparent_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 100))
        self.screen.blit(transparent_surface, (0, 0))

        # Dessine le cadre du menu de victoire
        menu_rect = pygame.Rect(menu_x1, menu_y1, menu_x2 - menu_x1, menu_y2 - menu_y1)
        pygame.draw.rect(self.screen, (220, 220, 220), menu_rect, border_radius=15)
        pygame.draw.rect(self.screen, (70, 70, 70), menu_rect, 2, border_radius=15)
        
        # Affiche le texte "Victoire du joueur X", où X est le joueur gagnant
        victory_game_text = pygame.font.SysFont(None, 30).render(
            f"Victoire du joueur {self.nom_joueurs[self.turn]}", True, (70, 70, 70)
            )
        victory_game_text_rect = victory_game_text.get_rect(center=(self.width // 2, self.height // 10 * 3 + 20))
        self.screen.blit(victory_game_text, victory_game_text_rect)
        
        # Définition des coordonnées des boutons et dessin des boutons
        victory_button_x1 = self.width // 12 * 4
        victory_button_y1 = self.height // 10 * 5
        victory_button_x2 = self.width // 12 * 4
        victory_button_y2 = self.height // 10

        # Dessine le bouton "Rejouer"
        play_again_button = pygame.draw.rect(
            self.screen, (220, 220, 220), (victory_button_x1, victory_button_y1 - 80, victory_button_x2, victory_button_y2)
            )
        pygame.draw.rect(self.screen, (70, 70, 70), play_again_button, 2, border_radius=15)
        play_again_text = pygame.font.SysFont(None, 30).render("Rejouer", True, (70, 70, 70))
        play_again_button_center = play_again_button.center
        play_again_text_center = play_again_text.get_rect(center=play_again_button_center)
        self.screen.blit(play_again_text, play_again_text_center)        

        # Dessine le bouton "Retour au menu principal"
        main_menu_button = pygame.draw.rect(
            self.screen, (220, 220, 220), (victory_button_x1, victory_button_y1, victory_button_x2, victory_button_y2)
            )
        pygame.draw.rect(self.screen, (70, 70, 70), main_menu_button, 2, border_radius=15)
        main_menu_text = pygame.font.SysFont(None, 30).render("Retour au menu principal", True, (70, 70, 70))
        main_menu_button_center = main_menu_button.center
        main_menu_text_center = main_menu_text.get_rect(center=main_menu_button_center)
        self.screen.blit(main_menu_text, main_menu_text_center)


    def play_music1(self):
        """Joue la musique pour placer les pions."""
        # Charge et joue la musique de fond
        pygame.mixer.music.load('music pion.mp3')
        pygame.mixer.music.play()


    def handle_click(self, mouse_pos):
        """Gère le clic de la souris sur les hexagones du plateau."""
        # Parcours tous les hexagones pour détecter le clic sur l'un d'eux
        for hexagon in self.hexagons:
            if hexagon.contains_point(mouse_pos):
                # Vérifie si l'hexagone est vide et change sa couleur en fonction du tour du joueur
                if hexagon.color == (255, 255, 255):
                    if self.turn == 0:
                        hexagon.color = (235, 0, 0)
                        # Place la pièce sur le plateau et vérifie s'il y a un gagnant
                        self.logic.place_piece(((hexagon.numero - 1) // self.grid_size, (hexagon.numero - 1) % self.grid_size), self.turn + 1)
                        if self.logic.check_winner(self.turn + 1):
                            self.victory = True
                        self.turn = 1
                        # Joue la musique correspondante
                        self.play_music1()
                    elif self.turn == 1 and self.game_mode == 'pvp':
                        hexagon.color = (0, 0, 235)
                        # Place la pièce sur le plateau et vérifie s'il y a un gagnant
                        self.logic.place_piece(((hexagon.numero - 1) // self.grid_size, (hexagon.numero - 1) % self.grid_size), self.turn + 1)
                        if self.logic.check_winner(self.turn + 1):
                            self.victory = True
                        self.turn = 0
                        # Joue la musique correspondante
                        self.play_music1()
                break

    def make_ai_move(self):
        """Fait jouer l'IA."""
        # Si aucune pièce n'est connectée, l'IA joue un coup aléatoire
        if len(self.logic.connected_pieces[2]) == 0:
            # Génère des coordonnées aléatoires dans la zone centrale du plateau
            (x,y) = (random.randint(4, self.grid_size - 4), random.randint(3, self.grid_size - 3))
            hexagon = self.hexagons[x * self.grid_size + y]
            # Vérifie si la case est vide et place la pièce de l'IA
            if hexagon.color == (255, 255, 255):
                hexagon.color = (0, 0, 235)
                self.logic.place_piece((x, y), 2)
            # Passe au tour du joueur 1 et joue la musique correspondante
            self.turn = 0
            self.play_music1()
        else:
            # Utilise l'algorithme minimax pour choisir le meilleur coup
            _, best_move = self.logic.minimax(self.ia_tree_depth, float('-inf'), float('inf'), True)
            if best_move is not None:
                x, y = best_move
            else:
                # Si aucun meilleur coup n'est trouvé, choisit un coup aléatoire parmi les coups possibles
                x, y = random.choice(self.logic.possible_moves())
            hexagon = self.hexagons[x * self.grid_size + y]
            # Vérifie si la case est vide et place la pièce de l'IA
            if hexagon.color == (255, 255, 255):
                hexagon.color = (0, 0, 235)
                self.logic.place_piece((x, y), self.turn + 1)
                # Vérifie s'il y a un gagnant après le coup de l'IA
                if self.logic.check_winner(self.turn + 1):
                    self.victory = True
                # Passe au tour du joueur 1 et joue la musique correspondante
                self.turn = 0
                self.play_music1()
     
    '''
    def save_game(self, file_path='game_save.json'):
            """Sauvegarde l'état actuel du jeu dans un fichier JSON.

        Args:
            file_path (str, optional): Le chemin du fichier de sauvegarde. Par défaut, 'game_save.json'.
        """
        # Crée un dictionnaire représentant l'état du jeu à sauvegarder
            game_state = {
                'hexagons': [(hexagon.numero, hexagon.color) for hexagon in self.hexagons],
                'turn': self.turn, 
                'grid_size': self.grid_size,
                'game_mode': self.game_mode
            }
            # Ajoute la profondeur de l'arbre pour l'IA si le mode de jeu est 'pve'
            if self.game_mode == 'pve':
                game_state['ia_tree_depth'] = self.ia_tree_depth

            # Crée le fichier de sauvegarde s'il n'existe pas
            if not os.path.exists(file_path):
                open(file_path, 'w').close() 
            # Écrit le dictionnaire dans le fichier JSON 
            with open(file_path, 'w') as file:
                json.dump(game_state, file)
    '''

    def run(self):
        """
        Lance la boucle de jeu
        """
        
        start_ticks = pygame.time.get_ticks()  # L'instant où le chronomètre démarre
        paused_ticks = 0  # Temps lors de la pause
        seconds = 0  # Initialiser les secondes à 0

        running = True
        while running:
            # Dessine des lignes et des boutons
            self.screen.fill((220, 220, 220))
            pygame.draw.line(self.screen, (70, 70, 70), (0, 80), (self.width, 80), 2)
            pygame.draw.line(self.screen, (70, 70, 70), (self.width // 3, 0), (self.width // 3, 80), 2)
            pygame.draw.line(self.screen, (70, 70, 70), ((self.width // 3) * 2, 0), ((self.width // 3) * 2, 80), 2)
            pygame.draw.line(self.screen, (70, 70, 70), ((self.width // 3) * 3, 0), ((self.width // 3) * 3, 80), 2)
            
            # Dessin du bouton de pause
            pause_button = pygame.draw.rect(self.screen, (220, 220, 220), (10, 10, self.width // 3 - 20, 60))
            pygame.draw.rect(self.screen, (70, 70, 70), pause_button, 2, border_radius=15)
            pause_text = pygame.font.SysFont(None, 30).render("Mettre en pause", True, (70, 70, 70))
            pause_button_center = pause_button.center
            pause_text_center = pause_text.get_rect(center=pause_button_center)
            self.screen.blit(pause_text, pause_text_center)

            # Affiche le joueur en cours et du temps écoulé
            turn_text = pygame.font.SysFont(None, 30).render(f"Au tour de : {self.nom_joueurs[1 - self.turn]}", True, (70, 70, 70))
            turn_text_center = turn_text.get_rect(center=((self.width // 2), 40))
            self.screen.blit(turn_text, turn_text_center)
            if self.is_paused == False:
                seconds = (pygame.time.get_ticks() - start_ticks) // 1000  # Convertir millisecondes en secondes
            timer_text = pygame.font.SysFont(None, 30).render(f"Temps écoulé : {seconds} secondes", True, (70, 70, 70))
            timer_text_center = timer_text.get_rect(center=((self.width // 6) * 5, 40))
            self.screen.blit(timer_text, timer_text_center)

            # Dessin des hexagones du jeu
            for hexagon in self.hexagons:
                hexagon.draw(self.screen)

            # Affichage des menus de pause et de victoire si nécessaire
            if self.is_paused:
                self.draw_pause_menu()
            if self.victory:
                self.is_paused = True
                self.draw_victory_menu()
            
            # Mouvement de l'IA en mode joueur contre environnement
            if self.game_mode == "pve" and self.turn == 1 and not self.victory:
                pygame.display.flip()
                self.make_ai_move()
                   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.victory:
                        if play_again_button.collidepoint(event.pos):
                            # Réinitialisation du jeu si le joueur veut rejouer
                            self.victory = False
                            self.is_paused = False  
                            self.turn = self.first_turn  
                            start_ticks = pygame.time.get_ticks()  
                            for hexagon in self.hexagons:
                                hexagon.color = (255, 255, 255)
                            self.logic = logic.Logic(self.grid_size)
                            continue  # Continue pour éviter d'exécuter d'autres contrôles
                        elif main_menu_button.collidepoint(event.pos):
                            # Retour au menu principal si le joueur le souhaite
                            self.main_menu()
                            continue
                    if self.is_paused:
                        if save_button.collidepoint(event.pos):
                            # Sauvegarde de la partie si le joueur appuie sur le bouton de sauvegarde
                            #self.save_game()
                            print("Sauvegarde")
                        elif resume_button.collidepoint(event.pos):
                            # Reprise de la partie si le joueur appuie sur le bouton de reprise
                            self.is_paused = False
                            start_ticks += (pygame.time.get_ticks() - paused_ticks)  # Ajuster le temps de pause
                        elif main_menu_button.collidepoint(event.pos):
                            # Retour au menu principal si le joueur appuie sur le bouton correspondant
                            self.main_menu()
                    elif pause_button.collidepoint(event.pos):
                        # Mise en pause du jeu si le joueur appuie sur le bouton de pause
                        self.is_paused = True
                        paused_ticks = pygame.time.get_ticks()  # Enregistrer le temps de la pause
                    else:
                        # Gestion du clic de la souris dans le jeu
                        self.handle_click(event.pos) 
            
            pygame.display.flip()
        pygame.quit()