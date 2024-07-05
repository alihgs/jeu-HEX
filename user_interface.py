# Import
import pygame
import pygame_menu
import hex_grid
import json
import os
import pygame.mixer

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()


class GameMenu:
    """
    Classe représentant le menu principal du jeu Hex.

    Attributes:
        surface (pygame.Surface): Surface de la fenêtre du jeu.
        largeur (int): Largeur de la fenêtre du jeu.
        longueur (int): Longueur de la fenêtre du jeu.
        main_menu (pygame_menu.Menu): Menu principal du jeu.
        ia_tree_depth (int): Profondeur de l'arbre de recherche pour l'IA.
        game_mode (str): Mode de jeu sélectionné.
        selected_starting_player (int): Joueur qui commence la partie.
        selected_grid_size (int): Taille du quadrillage sélectionnée.
    """
    def __init__(self):
        """
        Initialise une instance de la classe GameMenu.

        """
        self.surface = pygame.display.set_mode((900, 700))
        self.largeur, self.longueur = 900, 700
        self.main_menu = pygame_menu.Menu('Menu Principal', self.largeur, self.longueur)
        self.ia_tree_depth = 0
        self.set_main_menu()
        self.game_mode = ''
        self.selected_starting_player = 0
        self.selected_grid_size = 9

    # Menu principal
    
    def play_music(self):
        """Charge et lance la musique de fond du menu."""
        pygame.mixer.music.load('music hex2.mp3')
        pygame.mixer.music.play(-1)
    
    def stop_music(self):
        """Arrête la musique de fond."""
        pygame.mixer.music.stop()
        self.music_playing = False

    def set_main_menu(self):
        """Affiche le menu principal."""
        self.main_menu.clear()
        self.main_menu.add.button('Créer une nouvelle partie', self.create_new_game)
        #self.main_menu.add.button('Charger une sauvegarde', self.load_saved_game)
        self.main_menu.add.button('Quitter', pygame_menu.events.EXIT)
        self.play_music()
        self.main_menu.mainloop(self.surface)
        

    def mainloop(self):
        """Boucle principale du menu."""
        self.main_menu.mainloop(self.surface)

    def create_new_game(self):
        """Affiche le menu pour créer une nouvelle partie."""
        new_game_menu = pygame_menu.Menu('Nouvelle Partie', self.largeur, self.longueur)
        new_game_menu.add.button('Joueur contre joueur', self.pvp)
        new_game_menu.add.button('Joueur contre IA', self.pve)
        new_game_menu.add.button('Retour', self.set_main_menu)
        new_game_menu.mainloop(self.surface)

    '''
    def load_saved_game(self, file_path="game_save.json"):
        """Affiche le menu pour charger une partie sauvegardée."""
        saved_game_menu = pygame_menu.Menu('Charger une sauvegarde', self.largeur, self.longueur)
        saved_game_menu.add.button('Charger la sauvegarde', lambda: self.load_game(file_path))  # Ne pas passer self.ia_tree_depth
        saved_game_menu.add.button('Retour', self.set_main_menu)
        saved_game_menu.mainloop(self.surface)

    def load_game(self, file_path):
        """Charge une partie sauvegardée à partir d'un fichier JSON."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                game_state = json.load(file)
                grid_size = game_state['grid_size']
                game_mode = game_state['game_mode']
                turn = game_state['turn']
                self.ia_tree_depth = game_state.get('ia_tree_depth', self.ia_tree_depth)
                if not hasattr(self, 'hexagon_grid'):
                    self.hexagon_grid = hex_grid.HexagonGrid(
                        self.largeur, self.longueur, self.set_main_menu, grid_size, turn, game_mode, self.ia_tree_depth
                        )
                else:
                    self.hexagon_grid.grid_size = grid_size
                    self.hexagon_grid.turn = turn
                    self.hexagon_grid.game_mode = game_mode
                    self.hexagon_grid.ia_tree_depth = self.ia_tree_depth
                for hexagon, (numero, color) in zip(self.hexagon_grid.hexagons, game_state['hexagons']):
                    hexagon.numero = numero
                    hexagon.color = tuple(color)
            self.hexagon_grid.run()
            print("Partie chargée avec succès.")
        else:
            print("Le fichier de sauvegarde n'existe pas.")
    '''

    # Créer une nouvelle partie
    def set_grid_size(self, grid_size):
        """Définit la taille du quadrillage."""        
        self.selected_grid_size = grid_size

    def set_starting_player(self, starting_player):
        """Définit le joueur qui commence."""
        if starting_player == 'Bleu':
            self.selected_starting_player = 0
        else:
            self.selected_starting_player = 1

    def ia_difficulty(self, difficulty):
        """Définit la difficulté de l'IA."""
        if difficulty == 'Facile':
            self.ia_tree_depth = 2
        elif difficulty == 'Moyen':
            self.ia_tree_depth = 3
        else:
            self.ia_tree_depth = 4

    # Joueur contre joueur
    def pvp(self):
        """Affiche le menu pour joueur contre joueur."""
        pvp_menu = pygame_menu.Menu('Joueur contre joueur', self.largeur, self.longueur)
        self.game_mode = 'pvp'
        self.selected_starting_player = 0
        self.selected_grid_size = 9
        self.ia_tree_depth = 0

        pvp_menu.add.label('Taille du quadrillage', align=pygame_menu.locals.ALIGN_CENTER)
        pvp_menu.add.button('9x9', self.set_grid_size, 9)
        pvp_menu.add.button('11x11', self.set_grid_size, 11)
        pvp_menu.add.button('13x13', self.set_grid_size, 13)
        pvp_menu.add.button('19x19', self.set_grid_size, 19)
        pvp_menu.add.label('Joueur qui commence', align=pygame_menu.locals.ALIGN_CENTER)
        pvp_menu.add.button('Bleu', self.set_starting_player, 'Bleu')
        pvp_menu.add.button('Rouge', self.set_starting_player, 'Rouge')
        pvp_menu.add.button('Lancer la partie', self.start_game_2)
        pvp_menu.add.button('Retour', self.create_new_game)

        pvp_menu.mainloop(self.surface)

    # Joueur contre IA
    def pve(self):
        """Affiche le menu pour joueur contre IA."""
        pve_menu = pygame_menu.Menu('Joueur contre IA', self.largeur, self.longueur)
        self.game_mode = 'pve'
        self.selected_starting_player = 0
        self.selected_grid_size = 9
        self.ia_tree_depth = 2

        pve_menu.add.label('Taille du quadrillage', align=pygame_menu.locals.ALIGN_CENTER)
        pve_menu.add.button('9x9', self.set_grid_size, 9)
        pve_menu.add.button('11x11', self.set_grid_size, 11)
        pve_menu.add.label('Difficulté de l\'IA', align=pygame_menu.locals.ALIGN_CENTER)
        pve_menu.add.button('Facile', self.ia_difficulty, 'Facile')
        pve_menu.add.button('Moyen', self.ia_difficulty, 'Moyen')
        pve_menu.add.button('Difficile', self.ia_difficulty, 'Difficile')
        pve_menu.add.button('Lancer la partie', self.start_game_2)
        pve_menu.add.button('Retour', self.create_new_game)
        pve_menu.mainloop(self.surface)

    # En jeu
    def start_game_2(self):
        """Démarre une nouvelle partie du jeu Hex."""
        self.stop_music()
        game = hex_grid.HexagonGrid(900, 700, main_menu=self.set_main_menu, grid_size=self.selected_grid_size, turn=1 - self.selected_starting_player, game_mode=self.game_mode, ia_tree_depth=self.ia_tree_depth)
        game = hex_grid.HexagonGrid(
            900, 
            700, 
            main_menu=self.set_main_menu, 
            grid_size=self.selected_grid_size, 
            turn=1 - self.selected_starting_player, 
            game_mode=self.game_mode, 
            ia_tree_depth=self.ia_tree_depth
            )
        game.run()