from battle.models import Unit

def calculate_attack_power(warrior1, warrior2, warrior3):

    attack1 = warrior1 * Unit.objects.get(name="warrior1").attack_power
    attack2 = warrior2 * Unit.objects.get(name="warrior2").attack_power
    attack3 = warrior3 * Unit.objects.get(name="warrior3").attack_power

    return attack1 + attack2 + attack3