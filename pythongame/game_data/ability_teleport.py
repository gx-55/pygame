from pythongame.core.ability_effects import register_ability_effect
from pythongame.core.common import translate_in_direction, Millis, AbilityType
from pythongame.core.game_data import register_ability_data, AbilityData, UiIconSprite, register_ui_icon_sprite_path
from pythongame.core.game_state import GameState
from pythongame.core.visual_effects import VisualCircle, VisualRect, VisualLine


def _apply_teleport(game_state: GameState):
    player_entity = game_state.player_entity
    previous_position = player_entity.get_center_position()
    new_position = translate_in_direction((player_entity.x, player_entity.y), player_entity.direction, 140)
    player_entity.set_position(new_position)
    new_center_position = player_entity.get_center_position()

    color = (140, 140, 230)
    game_state.visual_effects.append(VisualCircle(color, previous_position, 17, 35, Millis(150), 1))
    game_state.visual_effects.append(VisualRect(color, previous_position, 37, 50, Millis(150), 1))
    game_state.visual_effects.append(VisualLine(color, previous_position, new_center_position, Millis(200), 1))
    game_state.visual_effects.append(VisualCircle(color, new_center_position, 25, 50, Millis(300), 2, player_entity))


def register_teleport_ability():
    register_ability_effect(AbilityType.TELEPORT, _apply_teleport)
    register_ability_data(
        AbilityType.TELEPORT,
        AbilityData("Teleport", UiIconSprite.ABILITY_TELEPORT, 2, Millis(500), "Teleport a short distance"))
    register_ui_icon_sprite_path(UiIconSprite.ABILITY_TELEPORT, "resources/graphics/teleport_icon.png")
