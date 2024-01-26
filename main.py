#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import django_setup
from project.models import Genre, Game

def inserts():
    shooter = Genre(
        name="Shooter"
    ).save()
    
    
    adventure = Genre(
        name="Adventure"
    ).save()
    
    
    rogue_like = Genre(
        name="Rogue-like"
    ).save()
    
    
    ror2 = Game(
        name = "Risk of Rain 2",
        release_date = "2020-08-11",
        rating = 4.8
    )
    ror2.save()
    ror2.genres.add(shooter)
    ror2.genres.add(rogue_like)
    ror2.save()
    hades = Game(
        name = "Hades",
        release_date = "2020-09-17",
        rating = 4.6
    )
    hades.save()
    hades.genres.add(adventure)
    hades.genres.add(rogue_like)
    hades.save()
    dishonored = Game(
        name = "Dishonored",
        release_date = "2012-10-09",
        rating = 4.9
    )
    dishonored.save()
    dishonored.genres.add(adventure)
    dishonored.save()
    isaac = Game(
        name = "The Binding of Isaac",
        release_date = "2011-09-28",
        rating = 5
    )
    isaac.save()
    isaac.genres.add(rogue_like)
    isaac.save()
    
def relations(): 
    shooter = Genre.objects.get(id=1)
    adventure = Genre.objects.get(id=2)
    rogue_like = Genre.objects.get(id=3)
    
    ror2 = Game.objects.get(id=1)
    ror2.genres.add(shooter)
    ror2.genres.add(rogue_like)

    hades = Game.objects.get(id=2)
    hades.genres.add(adventure)
    hades.genres.add(rogue_like)

    dishonored = Game.objects.get(id=3)
    dishonored.genres.add(adventure)

    isaac = Game.objects.get(id=4)
    isaac.genres.add(rogue_like)
       

def selects():
    game = Game.objects.get(id=1)
    print(game.name)
    print(game.genres.all())
    
    
def main():
    selects()
    


if __name__ == '__main__':
    main()
