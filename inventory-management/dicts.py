def create_inventory(items):
    
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """    
    return {i : items.count(i) for i in items}


def add_items(inventory, items):
    
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.    
    """
    for i in items:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1
    return inventory

def decrement_items(inventory, items):
    
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    for i in items:
        if i in inventory and inventory[i] > 0:
            inventory[i] = inventory[i] - 1
    return inventory


def remove_item(inventory, item):
    
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory

def list_inventory(inventory):
    
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(key, value) for (key, value) in inventory.items() if value > 0]