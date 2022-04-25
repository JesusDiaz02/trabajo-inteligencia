def eat_ghost(power_pellet_active, touching_ghost):
   
    """

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    return bool(power_pellet_active and touching_ghost)


def score(touching_power_pellet, touching_dot):
    """

    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    return bool(touching_power_pellet or touching_dot)


def lose(power_pellet_active, touching_ghost):
    if touching_ghost and not power_pellet_active:
        return True
    else:
        return False
    """

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    lost = lose(power_pellet_active, touching_ghost)
    if not lost and has_eaten_all_dots:
        return True
    else:
        return False


