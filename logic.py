from copy import deepcopy

class Logic:
    """Classe représentant la logique du jeu Hex."""

    def __init__(self, size):
        """Initialise une instance de la classe Logic.

        Args:
            size (int): Taille du plateau de jeu.
        """
        self.board_size = size
        self.board = [[0] * self.board_size for _ in range(self.board_size)]  # Crée un plateau de taille size x size avec des cases vides.
        self.connected_pieces = {1: [], 2: []}  # Initialise les ensembles de pièces connectées pour chaque joueur.
        self.boarders = {
            1: [{(0, col) for col in range(self.board_size)}, {(self.board_size - 1, col) for col in range(self.board_size)}],  # Initialise les bords du plateau pour le joueur 1.
            2: [{(row, 0) for row in range(self.board_size)}, {(row, self.board_size - 1) for row in range(self.board_size)}]  # Initialise les bords du plateau pour le joueur 2.
        }
        

    def place_piece(self, move, player):
        """Place une pièce pour un joueur donné et met à jour les pièces connectées.

        Args:
            move (tuple): Coordonnées de la pièce à placer.
            player (int): Joueur qui place la pièce (1 ou 2).
        """
        x, y = move
        self.board[x][y] = player  # Place la pièce du joueur sur le plateau.
        self.update_connected_pieces(player, move)  # Met à jour les pièces connectées après avoir placé la pièce.


    def update_connected_pieces(self, player, new_piece):
        """Met à jour les ensembles de pièces connectées après avoir placé une nouvelle pièce.

        Args:
            player (int): Joueur auquel appartient la pièce placée.
            new_piece (tuple): Coordonnées de la nouvelle pièce placée.
        """
        neighbors = self.get_neighbors(new_piece, 'coord')  # Récupère les voisins de la nouvelle pièce.
        new_set = {new_piece}  # Crée un nouvel ensemble contenant uniquement la nouvelle pièce.

        merged_set = set()
        # Fusionne les ensembles connectés qui partagent des voisins avec la nouvelle pièce.
        for existing_set in self.connected_pieces[player]:
            if existing_set.intersection(neighbors):
                merged_set.update(existing_set)

        merged_set.update(new_set)  # Ajoute la nouvelle pièce à l'ensemble fusionné.

        updated_sets = []
        # Ajoute les ensembles fusionnés ou les nouveaux ensembles connectés au joueur.
        for existing_set in self.connected_pieces[player]:
            if not existing_set.intersection(neighbors):
                updated_sets.append(existing_set)
        updated_sets.append(merged_set)

        self.connected_pieces[player] = updated_sets  # Met à jour les ensembles connectés pour le joueur donné.


    def get_neighbors(self, piece, needed):
        """Renvoie les voisins d'une pièce donnée sur le plateau.

        Args:
            piece (tuple): Coordonnées de la pièce dont on cherche les voisins.
            needed (str): Spécifie le format dans lequel renvoyer les voisins 
            ('coord' pour les coordonnées ou 'val' pour les valeurs des pièces).

        Returns:
            set or list: Les voisins de la pièce, soit sous forme de coordonnées (set), soit sous forme de valeurs de pièces (list).
        """
        if needed == 'coord':
            neighbors = set()
        else:
            neighbors = []
        x, y = piece
        # Parcourt les offsets pour trouver les voisins de la pièce.
        for offset_x, offset_y in [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, -1)]:
            nx, ny = x + offset_x, y + offset_y
            # Vérifie que les coordonnées des voisins sont valides et que la case n'est pas vide.
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] != 0:
                # Ajoute les coordonnées ou les valeurs des pièces des voisins en fonction de ce qui est nécessaire.
                if needed == 'coord':
                    neighbors.add((nx, ny))
                else:
                    neighbors.append(self.board[nx][ny])
        return neighbors


    def check_winner(self, player):
        """Vérifie si le joueur donné a gagné en reliant ses pièces des deux bords opposés du plateau.

        Args:
            player (int): Le joueur dont on vérifie s'il a gagné (1 ou 2).

        Returns:
            bool: True si le joueur a gagné, False sinon.
        """
        player_set = self.connected_pieces[player]
        for set in player_set:
            # Si un ensemble de pièces du joueur intersecte les deux bords opposés du plateau, le joueur a gagné.
            if set.intersection(self.boarders[player][0]) and set.intersection(self.boarders[player][1]):
                return True
        return False
        

    def possible_moves(self):
        """Renvoie une liste des mouvements possibles sous forme de coordonnées pour le joueur actif.

        Returns:
            list: Liste des coordonnées des mouvements possibles.
        """
        moves = []
        for x in range(self.board_size):
            for y in range(self.board_size):
                # Ajoute les coordonnées des cases vides du plateau à la liste des mouvements possibles.
                if self.board[x][y] == 0:
                    moves.append((x, y))
        return moves


    def evaluate_player(self, player):
        """Évalue le score d'un joueur en fonction de ses pièces connectées sur le plateau.

        Args:
            player (int): Le joueur dont on évalue le score (1 ou 2).

        Returns:
            int: Le score du joueur.
        """
        if player == 1:
            # Si le joueur est le joueur 1, évalue ses pièces.
            sets = self.connected_pieces[1]
            score = 0
            bonus_bord = 0
            # Parcourt tous les ensembles de pièces connectées du joueur.
            for set in sets:
                ind_min = float('inf')
                ind_max = float('-inf')
                bonus = 0
                # Trouve les coordonnées minimales et maximales des pièces de l'ensemble.
                for elem in set:
                    if elem[0] < ind_min:
                        ind_min = elem[0]
                    if elem[0] > ind_max:
                        ind_max = elem[0]
                # Calcule le score basé sur la différence entre les coordonnées minimales et maximales des pièces.
                score += (ind_max - ind_min) * 5
                # Vérifie s'il y a un bonus pour les pièces connectées aux bords du plateau.
                if (set.intersection(self.boarders[1][0]) or set.intersection(self.boarders[1][1])) and len(set) > 2:
                    bonus_bord += 40
            return score + bonus_bord
        else:
            # Si le joueur est le joueur 2, évalue ses pièces.
            sets = self.connected_pieces[2]
            opponent = 1
            score = 0
            bonus_bord = 0
            # Parcourt tous les ensembles de pièces connectées du joueur.
            for set in sets:
                ind_min = float('inf')
                ind_max = float('-inf')
                bonus = 0
                bonus_ligne = 0
                # Trouve les coordonnées minimales et maximales des pièces de l'ensemble.
                for elem in set:
                    if elem[1] < ind_min:
                        ind_min = elem[1]
                    if elem[1] > ind_max:
                        ind_max = elem[1]
                    x, y = elem
                    # Vérifie s'il y a une configuration de pièces spécifique pour un bonus de ligne.
                    if (0 <= x + 3 < self.board_size) and (0 <= y - 1 < self.board_size):
                        if self.board[x + 2][y - 1] == opponent and self.board[x + 3][y - 1] == opponent:
                            bonus_ligne += 8
                    if (0 <= x + 3 < self.board_size) and (0 <= y - 2 < self.board_size):
                        if self.board[x + 2][y - 1] == opponent and self.board[x + 3][y - 2] == opponent:
                            bonus_ligne += 8
                    if (0 <= x - 3 < self.board_size) and (0 <= y + 1 < self.board_size):
                        if self.board[x - 2][y + 1] == opponent and self.board[x - 3][y + 1] == opponent:
                            bonus_ligne += 8
                    if (0 <= x - 3 < self.board_size) and (0 <= y + 2 < self.board_size):
                        if self.board[x - 2][y + 1] == opponent and self.board[x - 3][y + 2] == opponent:
                            bonus_ligne += 8
                    # Calcule le bonus basé sur la configuration des pièces voisines.
                    neighbors = self.get_neighbors(elem, 'val')
                    count = neighbors.count(opponent)
                    if count == 1 and neighbors.count(player) <= 3:
                        bonus += 4
                # Vérifie s'il y a un bonus pour les pièces connectées aux bords du plateau.
                if (len(set) > 4 and set.intersection(self.boarders[2][0])) or (
                        len(set) > 4 and set.intersection(self.boarders[2][1])):
                    bonus_bord += 60
                # Calcule le score basé sur la différence entre les coordonnées minimales et maximales des pièces,
                # les bonus pour les configurations de pièces spécifiques et les bonus pour les pièces connectées aux bords.
                score += (ind_max - ind_min) * 8 + bonus * 3 + bonus_ligne * 5

            return score + bonus_bord


    def evaluate_board(self):
        """Évalue la position actuelle sur le plateau en renvoyant un score représentant
        l'avantage du joueur 2 par rapport au joueur 1.

        Returns:
            float: Le score de la position actuelle.
        """
        if self.check_winner(1):
            return float('-inf')
        elif self.check_winner(2):
            return float('inf')
        else:
            return self.evaluate_player(2) - self.evaluate_player(1) * 2


    def game_over(self):
        """Vérifie si le jeu est terminé en vérifiant s'il y a un vainqueur pour l'un des joueurs.

        Returns:
            bool: True si un joueur a gagné, False sinon.
        """
        if self.check_winner(1) or self.check_winner(2):
            return True
        else:
            return False


    def minimax(self, depth, alpha, beta, maximizing_player):
        """Algorithme du minimax avec élagage alpha-bêta pour trouver le meilleur mouvement à une profondeur donnée.

        Args:
            depth (int): La profondeur de recherche restante.
            alpha (float): La meilleure valeur pour le joueur maximisant.
            beta (float): La meilleure valeur pour le joueur minimisant.
            maximizing_player (bool): True si c'est le tour du joueur 2 (maximisant), False sinon (minimisant).

        Returns:
            tuple: Le score évalué et le meilleur mouvement trouvé.
        """
        if depth == 0 or self.game_over():
            return self.evaluate_board(), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in self.possible_moves():
                temp_game = deepcopy(self)
                temp_game.place_piece(move, 2)
                eval, _ = temp_game.minimax(depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.possible_moves():
                temp_game = deepcopy(self)
                temp_game.place_piece(move, 1)
                eval, _ = temp_game.minimax(depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move