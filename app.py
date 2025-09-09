import sys
import ZODB, ZODB.FileStorage
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabWidget, QFrame,
                             QGridLayout, QSizePolicy, QFormLayout)
from PyQt6.QtGui import QPixmap, QMovie, QIntValidator, QFont
from PyQt6.QtCore import Qt, QSize
from typing import List
import os

# Import project files
import functions
import pokemon_ddl
import pokemon_dml
import version_control

# --- Database Setup ---
dml_required = False

db_exists = os.path.exists('./data/PokeData.fs')
if not db_exists:
    dml_required = True
else:
    try:
        temp_storage = ZODB.FileStorage.FileStorage('./data/PokeData.fs')
        temp_db = ZODB.DB(temp_storage)
        temp_conn = temp_db.open()
        temp_root = temp_conn.root
        db_version = getattr(temp_conn.root, 'dml_version', None)
        temp_conn.close()
        temp_db.close()
        temp_storage.close()

        with open('dml_version.txt', 'r') as f:
            target_version = f.read().strip()

        if db_version != target_version:
            dml_required = True
    except (FileNotFoundError, Exception) as e:
        dml_required = True
if dml_required:
    os.makedirs('./data', exist_ok=True)
    pokemon_dml.runDML()

try:
    STORAGE = ZODB.FileStorage.FileStorage('./data/PokeData.fs')
    DB = ZODB.DB(STORAGE)
    CONNECTION = DB.open()
    DB_ROOT = CONNECTION.root
except Exception as e:
    print(
        f"Error: Could not open the database file at './data/PokeData.fs'. Please ensure the file exists and is not corrupt. Details: {e}")
    sys.exit(1)

# --- Asset Paths ---
ASSET_PATHS = {
    "types": "./assets/icons/{}.gif",
    "categories": "./assets/icons/{}.png",
    "stats": "./assets/icons/{}.gif",
    "pokeballs": "./assets/pokeballs/{}",
    "sprites": "./assets/PokemonSprites/{}",
    "shiny_star": "./assets/icons/ShinyVIStar.png",
    "item_icon": "./assets/icons/item.png",
    # --- FIX START: Add paths for gender icons ---
    "male_icon": "./assets/icons/male.png",
    "female_icon": "./assets/icons/female.png"
    # --- FIX END ---
}


class ClickableLabel(QLabel):
    """A QLabel that emits a clicked signal with its index."""

    def __init__(self, index, parent=None):
        super().__init__(parent)
        self.index = index
        self.clicked_signal = None

    def connect_signal(self, func):
        self.clicked_signal = func

    def mousePressEvent(self, event):
        if self.clicked_signal:
            self.clicked_signal(self.index)


class PokemonGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokémon Generator")
        self.setGeometry(100, 100, 700, 400)
        self.setFixedSize(700, 400)

        self.team: List[pokemon_ddl.PokemonIndiv] = []
        self.pokemon_sets: List[pokemon_ddl.PokemonSet] = []
        self.current_pokemon_index = -1
        self.active_movie = None

        self.init_ui()
        self.clear_display()  # Start with a clean slate

    def init_ui(self):
        # --- Main Layout ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # --- Top Section (Display) ---
        display_frame = QFrame()
        display_frame.setFrameShape(QFrame.Shape.StyledPanel)
        display_layout = QHBoxLayout(display_frame)

        # Left side: Tabs
        self.tabs = QTabWidget()
        self.battle_tab = QWidget()
        self.stats_tab = QWidget()
        self.tabs.addTab(self.battle_tab, "Battle")
        self.tabs.addTab(self.stats_tab, "Stats")
        self.init_battle_tab()
        self.init_stats_tab()

        left_panel_layout = QVBoxLayout()
        left_panel_layout.addWidget(self.tabs)
        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        left_panel_layout.addWidget(self.copy_button)

        # Right side: Sprite and Info
        right_panel_layout = QVBoxLayout()
        right_panel_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.sprite_label = QLabel()
        self.sprite_label.setFixedSize(128, 128)
        self.sprite_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.shiny_star_label = QLabel()
        self.shiny_star_label.setPixmap(QPixmap(ASSET_PATHS['shiny_star']))
        self.shiny_star_label.setFixedSize(20, 20)
        self.shiny_star_label.setScaledContents(True)

        sprite_layout = QGridLayout()
        sprite_layout.addWidget(self.sprite_label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        sprite_layout.addWidget(self.shiny_star_label, 0, 1, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        self.name_label = QLabel("Machamp")
        self.name_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))

        item_layout = QHBoxLayout()
        self.item_icon_label = QLabel()
        self.item_name_label = QLabel()
        item_layout.addStretch()
        item_layout.addWidget(self.item_icon_label)
        item_layout.addWidget(self.item_name_label)
        item_layout.addStretch()

        self.ability_label = QLabel("Ability: No Guard")

        self.type1_label = QLabel()
        self.type2_label = QLabel()
        types_layout = QHBoxLayout()
        types_layout.addStretch()
        types_layout.addWidget(self.type1_label)
        types_layout.addWidget(self.type2_label)
        types_layout.addStretch()

        self.gender_label = QLabel()

        right_panel_layout.addLayout(sprite_layout)
        right_panel_layout.addWidget(self.name_label, alignment=Qt.AlignmentFlag.AlignCenter)
        right_panel_layout.addLayout(item_layout)
        right_panel_layout.addWidget(self.ability_label, alignment=Qt.AlignmentFlag.AlignCenter)
        right_panel_layout.addLayout(types_layout)
        right_panel_layout.addWidget(self.gender_label, alignment=Qt.AlignmentFlag.AlignCenter)
        right_panel_layout.addStretch()

        display_layout.addLayout(left_panel_layout, 1)
        display_layout.addLayout(right_panel_layout, 1)

        # --- Middle Section (Pokeballs) ---
        pokeball_frame = QFrame()
        self.pokeball_layout = QHBoxLayout(pokeball_frame)
        self.pokeball_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # --- Bottom Section (Controls) ---
        control_layout = QHBoxLayout()
        create_label = QLabel("Create:")
        self.num_input = QLineEdit("6")
        self.num_input.setValidator(QIntValidator(1, 999))
        self.num_input.setFixedWidth(30)
        self.go_button = QPushButton("Go!")
        self.go_button.clicked.connect(self.generate_team)

        control_layout.addStretch()
        control_layout.addWidget(create_label)
        control_layout.addWidget(self.num_input)
        control_layout.addWidget(self.go_button)
        control_layout.addStretch()

        # --- Assemble Main Layout ---
        main_layout.addWidget(display_frame, 1)
        main_layout.addWidget(pokeball_frame)
        main_layout.addLayout(control_layout)

    def init_battle_tab(self):
        layout = QGridLayout(self.battle_tab)
        layout.setColumnStretch(1, 1)
        headers = ["", "Move", "Pow.", "", "Acc."]
        for i, header in enumerate(headers):
            label = QLabel(header)
            label.setFont(QFont("Arial", 8, QFont.Weight.Bold))
            layout.addWidget(label, 0, i, Qt.AlignmentFlag.AlignCenter)

        self.move_widgets = []
        for i in range(4):
            widgets = {
                "type": QLabel(), "name": QLabel(), "power": QLabel(),
                "cat": QLabel(), "acc": QLabel()
            }
            widgets['type'].setFixedSize(32, 15)
            widgets['cat'].setFixedSize(32, 15)
            widgets['name'].setWordWrap(True)
            widgets['name'].setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

            layout.addWidget(widgets['type'], i + 1, 0, Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(widgets['name'], i + 1, 1)
            layout.addWidget(widgets['power'], i + 1, 2, Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(widgets['cat'], i + 1, 3, Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(widgets['acc'], i + 1, 4, Qt.AlignmentFlag.AlignCenter)
            self.move_widgets.append(widgets)

    def init_stats_tab(self):
        layout = QFormLayout(self.stats_tab)
        self.stat_labels = {
            "nature": QLabel(), "hp": QLabel(), "attack": QLabel(),
            "defense": QLabel(), "sp_att": QLabel(), "sp_def": QLabel(), "speed": QLabel()
        }
        layout.addRow(QLabel("Nature"), self.stat_labels["nature"])
        layout.addRow(QLabel("HP"), self.stat_labels["hp"])
        layout.addRow(QLabel("ATTACK"), self.stat_labels["attack"])
        layout.addRow(QLabel("DEFENSE"), self.stat_labels["defense"])
        layout.addRow(QLabel("SP. ATT"), self.stat_labels["sp_att"])
        layout.addRow(QLabel("SP. DEF"), self.stat_labels["sp_def"])
        layout.addRow(QLabel("SPEED"), self.stat_labels["speed"])

    def generate_team(self):
        try:
            num = int(self.num_input.text())
        except (ValueError, TypeError):
            num = 0

        if num >= 1:
            self.clear_display()
            _, pokemon_set_objects = functions.getPokemonTeam(num, DB_ROOT)

            if not pokemon_set_objects:
                print("Generation failed. getPokemonTeam returned an empty list.")
                return

            self.pokemon_sets = pokemon_set_objects
            self.team = functions.createIndivPokemon(self.pokemon_sets, DB_ROOT)
            self.update_pokeballs()

    def update_pokeballs(self):
        for i in reversed(range(self.pokeball_layout.count())):
            item = self.pokeball_layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()

        for i, pk in enumerate(self.team):
            container = QWidget()
            vbox = QVBoxLayout(container)
            vbox.setSpacing(0)
            vbox.setContentsMargins(0, 0, 0, 0)
            icon_label = QLabel()
            icon_label.setFixedSize(40, 30)
            icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            vbox.addWidget(icon_label, alignment=Qt.AlignmentFlag.AlignCenter)
            pokeball_label = ClickableLabel(i)
            pixmap = QPixmap(ASSET_PATHS['pokeballs'].format(pk.pokeball))
            pokeball_label.setPixmap(pixmap.scaled(QSize(32, 32), Qt.AspectRatioMode.KeepAspectRatio))
            pokeball_label.connect_signal(self.select_pokemon)
            vbox.addWidget(pokeball_label, alignment=Qt.AlignmentFlag.AlignCenter)
            self.pokeball_layout.addWidget(container)

    def select_pokemon(self, index):
        if not (0 <= index < len(self.team)):
            return
        self.current_pokemon_index = index
        pokemon = self.team[index]
        pokemon_set = self.pokemon_sets[index]
        for i in range(self.pokeball_layout.count()):
            container = self.pokeball_layout.itemAt(i).widget()
            icon_label = container.findChild(QLabel)
            if i == index:
                try:
                    self.active_movie = QMovie(ASSET_PATHS['sprites'].format(pokemon_set.images[0]))
                    icon_label.setMovie(self.active_movie)
                    self.active_movie.start()
                except Exception as e:
                    print(f"Could not load icon GIF: {pokemon_set.images[0]}. Error: {e}")
                    icon_label.setText("?")
            else:
                if icon_label.movie():
                    icon_label.movie().stop()
                icon_label.clear()
        self.update_display(pokemon, pokemon_set)

    def update_display(self, pokemon: pokemon_ddl.PokemonIndiv, pokemon_set: pokemon_ddl.PokemonSet):
        is_shiny = pokemon.shiny == 'Yes'
        sprite_path = pokemon_set.images[2] if is_shiny else pokemon_set.images[1]
        self.sprite_label.setPixmap(QPixmap(ASSET_PATHS['sprites'].format(sprite_path)).scaled(
            QSize(128, 128), Qt.AspectRatioMode.KeepAspectRatio
        ))
        self.shiny_star_label.setVisible(is_shiny)
        self.name_label.setText(pokemon.name)

        if pokemon.item:
            pixmap = QPixmap(ASSET_PATHS['item_icon'])
            self.item_icon_label.setPixmap(pixmap.scaled(QSize(10, 10), Qt.AspectRatioMode.KeepAspectRatio))
            self.item_name_label.setText(pokemon.item)
        else:
            self.item_icon_label.clear()
            self.item_name_label.setText("No Item")

        self.ability_label.setText(f"Ability: {pokemon.ability}")
        self.type1_label.setPixmap(QPixmap(ASSET_PATHS['types'].format(pokemon_set.pkTypes[0].lower())))
        if len(pokemon_set.pkTypes) > 1:
            self.type2_label.setPixmap(QPixmap(ASSET_PATHS['types'].format(pokemon_set.pkTypes[1].lower())))
            self.type2_label.show()
        else:
            self.type2_label.hide()

        self.gender_label.clear()  # Clear previous icon first
        if pokemon.gender == '(M)':
            pixmap = QPixmap(ASSET_PATHS['male_icon'])
            self.gender_label.setPixmap(pixmap.scaled(QSize(20, 20), Qt.AspectRatioMode.KeepAspectRatio))
        elif pokemon.gender == '(F)':
            pixmap = QPixmap(ASSET_PATHS['female_icon'])
            self.gender_label.setPixmap(pixmap.scaled(QSize(20, 20), Qt.AspectRatioMode.KeepAspectRatio))

        for i in range(4):
            widgets = self.move_widgets[i]
            for widget in widgets.values():
                widget.clear()

        for i, move_name in enumerate(pokemon.moves):
            if i >= 4: break
            move_obj = DB_ROOT.moves.get(move_name)
            widgets = self.move_widgets[i]
            if move_obj:
                widgets['type'].setPixmap(QPixmap(ASSET_PATHS['types'].format(move_obj.moveType.lower())))
                widgets['name'].setText(move_obj.name)
                widgets['power'].setText(str(move_obj.power) if move_obj.power > 0 else '—')
                widgets['acc'].setText(str(int(move_obj.accuracy * 100)) if move_obj.accuracy > 0 else '—')
                cat_path = ""
                if move_obj.category == 'Phys':
                    cat_path = ASSET_PATHS['categories'].format('physical')
                elif move_obj.category == 'Spec':
                    cat_path = ASSET_PATHS['categories'].format('special')
                else:
                    cat_path = ASSET_PATHS['categories'].format('status')
                widgets['cat'].setPixmap(QPixmap(cat_path).scaled(QSize(32, 15)))
                widgets['cat'].setToolTip(move_obj.category)
        self.stat_labels["nature"].setText(f"{pokemon.nature} Nature")
        self.stat_labels["hp"].setText(str(pokemon.hpStat))
        self.stat_labels["attack"].setText(str(pokemon.atkStat))
        self.stat_labels["defense"].setText(str(pokemon.defStat))
        self.stat_labels["sp_att"].setText(str(pokemon.spaStat))
        self.stat_labels["sp_def"].setText(str(pokemon.spdStat))
        self.stat_labels["speed"].setText(str(pokemon.speStat))
        self.copy_button.setEnabled(True)

    def clear_display(self):
        self.sprite_label.clear()
        self.shiny_star_label.setVisible(False)
        self.name_label.setText("?")
        self.item_icon_label.clear()
        self.item_name_label.clear()
        self.ability_label.setText("Ability: ?")
        self.type1_label.clear()
        self.type2_label.clear()
        self.gender_label.clear()
        for row in self.move_widgets:
            for widget in row.values():
                widget.clear()
        for label in self.stat_labels.values():
            label.clear()
        self.copy_button.setEnabled(False)
        self.current_pokemon_index = -1

    def copy_to_clipboard(self):
        if 0 <= self.current_pokemon_index < len(self.team):
            pokemon = self.team[self.current_pokemon_index]
            clipboard = QApplication.clipboard()
            clipboard.setText(pokemon.toString())
            print(f"Copied {pokemon.name} data to clipboard.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PokemonGeneratorApp()
    window.show()
    app.exec()
    CONNECTION.close()
    DB.close()
    STORAGE.close()