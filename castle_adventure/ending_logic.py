"""
Ending determination logic for Castle Adventure.
"""


def determine_ending(game_state):
    """
    Determine which ending player reaches based on game state.
    Returns ending_id (E1-E5).

    Priority order (most specific first):
    E5: Secret ending - True King
    E4: Castle Collapse
    E3: Mutual Escape
    E2: Tragic Betrayal
    E1: Heroic Rescue (default)
    """
    items = game_state.inventory
    flags = game_state.flags

    if len(items) == 8 and all_npcs_befriended(flags) and flags.get('sat_on_throne'):
        return 'E5'

    if flags.get('chaos_level', 0) > 10:
        return 'E4'

    if ('ITEM_004' in items and
        flags.get('dragon_befriended') and
        flags.get('troll_befriended') and
        flags.get('wizard_helped')):
        return 'E3'

    if flags.get('npc_relations', 0) < 0 or flags.get('killed_npcs'):
        return 'E2'

    return 'E1'


def all_npcs_befriended(flags):
    """Check if all NPCs were befriended."""
    return (flags.get('dragon_befriended') and
            flags.get('troll_befriended') and
            flags.get('wizard_helped'))
